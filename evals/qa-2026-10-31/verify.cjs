// Isolated controller checks, not browser, layout, accessibility-tree, or playback tests.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const html = fs.readFileSync(path.join(__dirname, 'index.corrected.html'), 'utf8');
const source = html.match(/<script>([\s\S]*?)<\/script>/)[1];
new vm.Script(source, { filename: 'index.corrected.html:inline-script' });

function harness({ reduced = false, animationSupport = true, animationFailure = false, legacyMedia = false } = {}) {
  const timers = new Map();
  const animations = [];
  const operations = [];
  let nextTimer = 0;
  let visual = null;
  const eventTarget = () => ({
    listeners: {},
    addEventListener(type, fn) { (this.listeners[type] ||= []).push(fn); },
    emit(type, event = {}) { for (const fn of this.listeners[type] || []) fn(event); }
  });
  const document = eventTarget();
  const element = (id) => Object.assign(eventTarget(), {
    id, hidden: id !== 'details', disabled: false, inert: false, dataset: {}, attributes: {},
    setAttribute(name, value) { this.attributes[name] = value; operations.push(`${id}:${name}=${value}`); },
    getAttribute(name) { return this.attributes[name]; },
    contains(target) { return target === this || (id === 'details' && target === close); },
    focus() { document.activeElement = this; operations.push(`focus:${id}`); }
  });
  const toggle = element('toggle');
  const details = element('details');
  const close = element('close');
  const outside = element('outside');
  const elements = { toggle, details, close };
  document.getElementById = id => elements[id];
  document.activeElement = toggle;
  if (animationSupport) {
    details.animate = (frames, options) => {
      if (animationFailure) throw new Error('Simulated optional animation failure');
      const animation = {
        frames, options, canceled: false,
        sample(opacity) { this.opacity = String(opacity); this.transform = `translateY(${8 * (1 - opacity)}px)`; },
        cancel() { this.canceled = true; if (visual === this) visual = null; },
        finish() { this.onfinish?.(); }
      };
      animation.opacity = String(frames[0].opacity);
      animation.transform = frames[0].transform;
      animations.push(animation);
      visual = animation;
      return animation;
    };
  }
  const preference = Object.assign(eventTarget(), { matches: reduced });
  if (legacyMedia) {
    preference.addListener = fn => preference.listeners.change = [fn];
    preference.addEventListener = undefined;
  }
  const window = Object.assign(eventTarget(), { matchMedia: () => preference });
  vm.runInNewContext(source, {
    document, window,
    getComputedStyle: () => visual || {
      opacity: details.dataset.open === 'true' ? '1' : '0',
      transform: details.dataset.open === 'true' ? 'translateY(0)' : 'translateY(8px)'
    },
    setTimeout: (fn, delay) => { timers.set(++nextTimer, { fn, delay }); return nextTimer; },
    clearTimeout: id => timers.delete(id)
  }, { filename: 'index.corrected.html:inline-script' });
  return {
    toggle, details, close, outside, document, window, preference, animations, timers, operations,
    click(element) { if (!element.disabled) element.emit('click'); },
    latest() { return animations.at(-1); },
    flush() { for (const [id, task] of [...timers]) { timers.delete(id); task.fn(); } },
    escape(target, defaultPrevented = false) {
      const event = { key: 'Escape', target, defaultPrevented, preventDefault() { this.defaultPrevented = true; } };
      document.emit('keydown', event);
      return event;
    },
    state(open, settled = false) {
      assert.equal(toggle.getAttribute('aria-expanded'), String(open));
      assert.equal(toggle.textContent, open ? 'Hide notebook details' : 'Show notebook details');
      assert.equal(details.dataset.open, String(open));
      assert.equal(details.getAttribute('aria-hidden'), String(!open));
      assert.equal(details.inert, !open);
      assert.equal(close.disabled, !open);
      if (open || settled) assert.equal(details.hidden, !open);
    }
  };
}

let count = 0;
function check(name, fn) { fn(); count += 1; console.log(`PASS ${name}`); }

check('Initial collapsed state; opening changes semantics immediately without moving focus', () => {
  const h = harness();
  h.state(false, true);
  assert.equal(h.toggle.hidden, false);
  h.click(h.toggle);
  h.state(true);
  assert.equal(h.document.activeElement, h.toggle);
  assert.equal(h.latest().options.duration, 180);
  h.latest().finish();
  h.state(true, true);
  assert.equal(h.timers.size, 0);
});

check('Rapid reversal retargets the sampled position; obsolete finish/timer callbacks are harmless', () => {
  const h = harness();
  h.click(h.toggle);
  h.latest().sample(0.4);
  const oldOpen = h.latest();
  const oldFinish = oldOpen.onfinish;
  const oldTimeout = [...h.timers.values()][0].fn;
  h.click(h.toggle);
  h.state(false);
  assert.equal(oldOpen.canceled, true);
  assert.equal(h.latest().frames[0].opacity, '0.4');
  assert.equal(h.latest().options.duration, 72);
  h.latest().sample(0.2);
  const oldCloseFinish = h.latest().onfinish;
  h.click(h.toggle);
  h.state(true);
  assert.equal(h.latest().frames[0].opacity, '0.2');
  const newest = h.latest();
  oldFinish(); oldTimeout(); oldCloseFinish();
  h.state(true);
  assert.equal(newest.canceled, false);
  newest.finish();
  h.state(true, true);
});

check('Immediate second activation closes without waiting for an opening frame', () => {
  const h = harness();
  h.click(h.toggle); h.click(h.toggle);
  h.state(false, true);
  assert.equal(h.timers.size, 0);
});

check('Close returns focus before hiding semantics and disables the closing control immediately', () => {
  const h = harness();
  h.click(h.toggle); h.latest().finish(); h.close.focus();
  h.operations.length = 0;
  h.click(h.close);
  h.state(false);
  assert.equal(h.operations[0], 'focus:toggle');
  assert.equal(h.document.activeElement, h.toggle);
  h.latest().finish();
  h.state(false, true);
});

check('Later animation completion cannot steal focus after the user moves elsewhere', () => {
  const h = harness();
  h.click(h.toggle); h.outside.focus(); h.latest().finish();
  assert.equal(h.document.activeElement, h.outside);
  h.click(h.close); h.latest().finish();
  assert.equal(h.document.activeElement, h.outside);
});

check('Escape works within the disclosure and respects unrelated or already-handled input', () => {
  const h = harness();
  h.click(h.toggle); h.latest().finish();
  assert.equal(h.escape(h.outside).defaultPrevented, false);
  h.state(true);
  h.escape(h.toggle, true); h.state(true);
  h.close.focus();
  assert.equal(h.escape(h.close).defaultPrevented, true);
  h.state(false);
  assert.equal(h.document.activeElement, h.toggle);
});

check('Reduced motion uses immediate states and creates no animation or cleanup timer', () => {
  const h = harness({ reduced: true });
  h.click(h.toggle); h.state(true, true);
  h.click(h.toggle); h.state(false, true);
  assert.equal(h.animations.length, 0);
  assert.equal(h.timers.size, 0);
});

check('A live preference change cancels active motion and settles the latest target', () => {
  const h = harness();
  h.click(h.toggle); h.latest().sample(0.5); h.click(h.toggle);
  const stale = h.latest().onfinish;
  h.preference.matches = true; h.preference.emit('change');
  h.state(false, true);
  assert.equal(h.timers.size, 0);
  h.click(h.toggle); stale(); h.state(true, true);
});

check('Legacy media-query listener also handles preference changes', () => {
  const h = harness({ legacyMedia: true });
  h.click(h.toggle);
  h.preference.matches = true; h.preference.emit('change');
  h.state(true, true);
  assert.equal(h.timers.size, 0);
});

check('Unsupported or failed animation API preserves both disclosure actions', () => {
  for (const options of [{ animationSupport: false }, { animationFailure: true }]) {
    const h = harness(options);
    h.click(h.toggle); h.state(true, true);
    h.click(h.close); h.state(false, true);
    assert.equal(h.timers.size, 0);
  }
});

check('Missing finish events fall back to cleanup of the current state', () => {
  const h = harness();
  h.click(h.toggle); h.flush(); h.state(true, true);
  h.click(h.toggle); h.state(false); h.flush(); h.state(false, true);
  assert.equal(h.timers.size, 0);
});

check('External animation cancellation settles without leaving pending work', () => {
  const h = harness();
  h.click(h.toggle); h.latest().finish(); h.click(h.toggle);
  h.latest().oncancel(); h.state(false, true);
  assert.equal(h.timers.size, 0);
});

check('Page exit cancels pending effects and leaves the latest state ready for return', () => {
  const h = harness();
  h.click(h.toggle); h.window.emit('pagehide'); h.state(true, true);
  h.click(h.toggle); h.window.emit('pagehide'); h.state(false, true);
  assert.equal(h.timers.size, 0);
});

check('1,000 rapid toggles retain the latest state with stale callbacks injected', () => {
  const h = harness();
  let oldCallback = () => {};
  for (let i = 0; i < 1000; i++) {
    h.click(h.toggle);
    oldCallback();
    h.state(i % 2 === 0);
    h.latest().sample(i % 2 === 0 ? 0.65 : 0.35);
    oldCallback = h.latest().onfinish || (() => {});
  }
  h.flush(); h.state(false, true);
  assert.equal(h.timers.size, 0);
});

check('Source preserves approved content and surface tokens with no external dependencies', () => {
  for (const text of ['Juniper notes', 'A small workspace for collecting ideas.', 'Show notebook details', 'Notebook details', 'Seven notes, gathered this week.', 'Close details']) assert.ok(html.includes(text));
  for (const color of ['#f4efd9', '#172c29', '#e9a389', '#d8dec0', '#f1d3ad']) assert.ok(html.includes(color));
  const css = html.match(/<style>([\s\S]*?)<\/style>/)[1].replace(/\s/g, '');
  for (const declaration of ['max-width:640px', 'margin:60pxauto', 'padding:32px', 'padding:14px24px', 'border-radius:20px', 'padding:24px', 'border-radius:24px', 'margin-top:24px']) assert.ok(css.includes(declaration));
  assert.ok(!/\b(?:src|href)\s*=/i.test(html));
  assert.match(html, /<section id="details" class="details" aria-labelledby="details-title">/);
  assert.match(css, /prefers-reduced-motion:reduce/);
  assert.equal((html.match(/type="button"/g) || []).length, 2);
});

console.log(`\n${count} isolated/source checks passed. No browser execution or visual/temporal QA performed.`);
