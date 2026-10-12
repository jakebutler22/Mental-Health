// A monotonic active-time clock: paused wall time is never counted.
export function createExerciseClock(now = () => performance.now()) {
  let accumulated = 0, anchor = null, state = 'ready';
  const elapsed = () => accumulated + (anchor === null ? 0 : Math.max(0, now() - anchor));
  return {
    start() { if (state !== 'ready') return false; anchor = now(); state = 'active'; return true; },
    pause() { if (state !== 'active') return false; accumulated = elapsed(); anchor = null; state = 'paused'; return true; },
    resume() { if (state !== 'paused') return false; anchor = now(); state = 'active'; return true; },
    finish(outcome = 'completed') { if (!['active','paused'].includes(state)) return false; accumulated = elapsed(); anchor = null; state = outcome; return true; },
    snapshot() { return { state, elapsedMs: elapsed() }; },
  };
}
export function breathingAt(elapsedMs) {
  const elapsed = Math.max(0, Math.min(60000, elapsedMs));
  if (elapsed === 60000) return {phase:'done',cycle:6,cycles:6,inflation:0,remaining:0,elapsedMs:elapsed};
  const position = elapsed % 10000, inhale = position < 4000;
  const progress = inhale ? position / 4000 : 1 - (position - 4000) / 6000;
  // Smoothstep preserves continuous shape and zero velocity at phase boundaries.
  return {phase:inhale?'inhale':'exhale', cycle:Math.floor(elapsed / 10000)+1,cycles:Math.floor(elapsed / 10000), inflation:progress*progress*(3-2*progress),remaining:Math.ceil((inhale ? 4000-position : 10000-position)/1000),elapsedMs:elapsed};
}
export const groundingSteps = [
  {count:5,sense:'see',text:'Notice five things you can see.',icon:'◉'},
  {count:4,sense:'feel',text:'Notice four things you can feel.',icon:'◇'},
  {count:3,sense:'hear',text:'Notice three things you can hear.',icon:'≈'},
  {count:2,sense:'smell',text:'Notice two things you can smell.',icon:'❋'},
  {count:1,sense:'taste',text:'Notice one thing you can taste.',icon:'○'},
];

export function breathingRecordTime(elapsedMs){const active_elapsed_ms=Math.floor(Math.max(0,Math.min(60000,elapsedMs)));return {active_elapsed_ms,cycles:Math.min(6,Math.floor(active_elapsed_ms/10000))};}
