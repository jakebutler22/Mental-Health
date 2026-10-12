<script setup>
import { ref, computed, onMounted, onUnmounted, nextTick } from 'vue';
import { createExerciseClock, breathingAt, groundingSteps, breathingRecordTime } from './controllers/exerciseClock.js';
import { api } from './lib/api.js';
import { createSessionPersistence } from './controllers/sessionPersistence.js';
import GuacMark from './components/GuacMark.vue';
import ChatPanel from './components/ChatPanel.vue';
import BreathingExercise from './components/BreathingExercise.vue';
import GroundingExercise from './components/GroundingExercise.vue';
import SupportPanel from './components/SupportPanel.vue';
import HistoryPanel from './components/HistoryPanel.vue';

const view = ref('home');
const support = ref(false);
const simple = ref(false);
const reduced = ref(false);
const color = ref('avocado');
const recent = ref(null);
const state = ref('ready');
const elapsed = ref(0);
const step = ref(0);
const skipped = ref([]);
const preferenceError = ref('');
const busy = ref(false);
const saveRevision = ref(0);
const currentRecord = ref(null);
const conversationId = ref(null);
const chatKey = ref(0);
const clearingHistory = ref(false);
const timing = ref({ entry: null, firstFrame: null, finalFrame: null });
const settingsOpen = ref(false);
const skill = ref(null);
let clock = null;
let frame = null;
let lastPersist = 0;
let preferenceRevision = 0;

const persistence = createSessionPersistence(api, () => saveRevision.value++);
const saved = computed(() => { saveRevision.value; return currentRecord.value?.saved; });
const unsaved = computed(() => { saveRevision.value; return persistence.pending; });
const breathing = computed(() => breathingAt(elapsed.value));

function tick() {
  if (clock) {
    elapsed.value = clock.snapshot().elapsedMs;
    if (state.value === 'active' && elapsed.value - lastPersist >= 5000) {
      lastPersist = elapsed.value;
      persist();
    }
    if (skill.value === 'breathing' && state.value === 'active' && elapsed.value >= 60000) {
      clock.finish();
      elapsed.value = 60000;
      state.value = 'completed';
      markFrame(true);
      persist();
    }
  }
  frame = requestAnimationFrame(tick);
}

function sessionBody() {
  const duration = skill.value === 'breathing'
    ? breathingRecordTime(elapsed.value)
    : { active_elapsed_ms: Math.floor(elapsed.value), cycles: 0 };
  return { state: state.value, ...duration, step: step.value, skipped_steps: [...skipped.value] };
}

function persist() {
  if (currentRecord.value) persistence.update(currentRecord.value, sessionBody());
}

function markFrame(final = false) {
  const target = timing.value;
  nextTick(() => requestAnimationFrame(() => requestAnimationFrame(timestamp => {
    if (timing.value !== target) return;
    if (final) target.finalFrame = timestamp;
    else target.firstFrame = timestamp;
  })));
}

function start(selection) {
  const which = typeof selection === 'string' ? selection : selection.skill;
  if (clearingHistory.value || busy.value || (['active', 'paused'].includes(state.value) && view.value === which)) return;
  if (!['breathing', 'grounding'].includes(which)) return;
  if (['active', 'paused'].includes(state.value)) navigate('home');
  timing.value = { entry: performance.now(), firstFrame: null, finalFrame: null };
  skill.value = which;
  lastPersist = 0;
  step.value = 0;
  skipped.value = [];
  elapsed.value = 0;
  state.value = 'active';
  settingsOpen.value = false;
  clock = createExerciseClock();
  clock.start();
  view.value = which;
  const request = { request_id: crypto.randomUUID(), skill: which, conversation_id: conversationId.value };
  if (typeof selection === 'object' && selection.recommendation_request_id) {
    request.recommendation_request_id = selection.recommendation_request_id;
  }
  currentRecord.value = persistence.create(request);
  markFrame();
}

async function retrySave() {
  busy.value = true;
  await persistence.retryAll();
  busy.value = false;
}

function pause() {
  if (state.value !== 'active') return;
  clock.pause();
  elapsed.value = clock.snapshot().elapsedMs;
  state.value = 'paused';
  persist();
}

function resume() {
  if (state.value !== 'paused') return;
  clock.resume();
  state.value = 'active';
  persist();
}

function stop() {
  if (!['active', 'paused'].includes(state.value)) return;
  clock.finish('stopped');
  elapsed.value = clock.snapshot().elapsedMs;
  state.value = 'stopped';
  persist();
}

function navigate(where) {
  if (clearingHistory.value) return;
  if (['active', 'paused'].includes(state.value)) {
    clock.finish('interrupted');
    elapsed.value = clock.snapshot().elapsedMs;
    state.value = 'interrupted';
    persist();
  }
  view.value = where;
  settingsOpen.value = false;
  loadRecent();
}

function next(skip = false) {
  if (state.value !== 'active') return;
  if (skip) skipped.value.push(step.value);
  step.value++;
  elapsed.value = clock.snapshot().elapsedMs;
  if (step.value === 5) {
    clock.finish();
    state.value = 'completed';
    markFrame(true);
  }
  persist();
}

async function preferences() {
  const revision = preferenceRevision;
  try {
    const preference = await api('/preferences');
    if (revision !== preferenceRevision) return;
    color.value = preference.explicit_balloon_color || 'avocado';
    simple.value = preference.simple_view;
    reduced.value = preference.reduced_motion || matchMedia('(prefers-reduced-motion: reduce)').matches;
  } catch {
    reduced.value = matchMedia('(prefers-reduced-motion: reduce)').matches;
  }
}

async function preference(key, value) {
  preferenceRevision++;
  try {
    await api('/preferences', { method: 'PATCH', body: { [key]: value } });
    preferenceError.value = '';
  } catch {
    preferenceError.value = 'Changed for this visit, but this preference could not be saved.';
  }
}

async function resetPreferences() {
  preferenceRevision++;
  try {
    await api('/preferences', { method: 'DELETE' });
    await preferences();
    preferenceError.value = '';
  } catch {
    preferenceError.value = 'Preferences could not be reset. Try again.';
  }
}

async function loadRecent() {
  try {
    const sessions = await api('/sessions');
    recent.value = sessions.items[0]?.skill || null;
  } catch {
    recent.value = null;
  }
}

async function beforeClearHistory() {
  clearingHistory.value = true;
  await persistence.discardAll();
  conversationId.value = null;
  chatKey.value++;
  currentRecord.value = null;
}

function visibility() {
  if (document.hidden) pause();
}

function openSupport() {
  pause();
  support.value = true;
}

function viewportChanged() {
  const viewport = window.visualViewport;
  const inset = viewport && viewport.scale === 1 ? Math.max(0, window.innerHeight - viewport.height - viewport.offsetTop) : 0;
  document.documentElement.style.setProperty('--keyboard-inset', `${inset}px`);
}

onMounted(() => {
  preferences();
  loadRecent();
  frame = requestAnimationFrame(tick);
  document.addEventListener('visibilitychange', visibility);
  window.visualViewport?.addEventListener('resize', viewportChanged);
  window.visualViewport?.addEventListener('scroll', viewportChanged);
  viewportChanged();
});

onUnmounted(() => {
  cancelAnimationFrame(frame);
  document.removeEventListener('visibilitychange', visibility);
  window.visualViewport?.removeEventListener('resize', viewportChanged);
  window.visualViewport?.removeEventListener('scroll', viewportChanged);
});
</script>

<template>
  <div class="app-shell" :class="{ simple }">
    <header class="site-header">
      <button :disabled="clearingHistory" class="brand" aria-label="Guac home" @click="navigate('home')">
        <GuacMark /><span class="wordmark">Guac<span class="wordmark-dot">.</span></span>
      </button>
      <nav aria-label="Main navigation">
        <button :disabled="clearingHistory" class="nav-button" @click="navigate('home')">Your pause</button>
        <button :disabled="clearingHistory" class="nav-button" @click="navigate('history')">History</button>
        <button class="nav-button" :aria-pressed="simple" @click="simple = !simple; preference('simple_view', simple)">{{ simple ? 'Full view' : 'Simpler view' }}</button>
      </nav>
    </header>

    <main>
      <div v-show="view === 'home'" class="home-layout">
        <section class="intro">
          <div class="hero-copy">
            <span class="eyebrow"><span class="tiny-seed" aria-hidden="true"></span> A little space for yourself</span>
            <h1>Big day?<br><em>Small pause.</em></h1>
            <p class="lead">Tell Guac what’s on your mind. Or skip the chat and find your own moment.</p>
          </div>
          <ChatPanel :key="chatKey" :active="view === 'home'" @choose="start" @conversation="conversationId = $event" @support="openSupport" />
        </section>

        <aside class="choices" aria-label="Begin without chatting">
          <div class="choice-heading"><span class="eyebrow">Go straight to a pause</span><p>No words needed.</p></div>
          <button class="skill-card" :disabled="clearingHistory" @click="start('breathing')">
            <span class="skill-symbol breath-symbol" aria-hidden="true">◌</span>
            <span class="eyebrow">01 / Find a rhythm</span>
            <h2>Paced breathing</h2>
            <p>Four seconds in. Six seconds out.<br>A steady rhythm to follow.</p>
            <span class="skill-footer">60 seconds <span aria-hidden="true">→</span></span>
          </button>
          <button class="skill-card" :disabled="clearingHistory" @click="start('grounding')">
            <span class="skill-symbol" aria-hidden="true">✳</span>
            <span class="eyebrow">02 / Notice this moment</span>
            <h2>Sensory grounding</h2>
            <p>One sense at a time.<br>A little attention to the here and now.</p>
            <span class="skill-footer">About a minute <span aria-hidden="true">→</span></span>
          </button>
          <div v-if="recent && !simple" class="recent">
            <span class="fine">Your last pause, if you’d like</span>
            <button class="text-button" :disabled="clearingHistory" @click="start(recent)">Repeat {{ recent === 'breathing' ? 'breathing' : 'grounding' }} →</button>
          </div>
          <button v-if="!simple" class="settings-toggle" :aria-expanded="settingsOpen" @click="settingsOpen = !settingsOpen">Make it yours <span aria-hidden="true">{{ settingsOpen ? '−' : '+' }}</span></button>
          <section v-if="settingsOpen && !simple" class="settings" aria-label="Your preferences">
            <label>Balloon color
              <select v-model="color" @change="preference('explicit_balloon_color', color)">
                <option value="avocado">Avocado green</option><option value="red">Red</option><option value="sage">Sage</option><option value="blue">Blue</option><option value="plum">Plum</option>
              </select>
            </label>
            <label class="check-label"><input type="checkbox" v-model="reduced" @change="preference('reduced_motion', reduced)"> Reduced motion</label>
            <button class="text-button" @click="resetPreferences">Reset preferences</button>
          </section>
          <div v-if="!simple" class="aside-note"><span class="seed-doodle" aria-hidden="true">✦</span><p>No perfect way to pause.<br>Pick what feels right for this moment.</p></div>
        </aside>
      </div>

      <BreathingExercise v-if="view === 'breathing'" :snapshot="breathing" :timing="timing" :state="state" :color="color" :reduced="reduced" @pause="pause" @resume="resume" @stop="stop" @home="navigate('home')" />
      <GroundingExercise v-if="view === 'grounding'" :timing="timing" :elapsed="elapsed" :step="groundingSteps[Math.min(step, 4)]" :index="step" :state="state" :skipped="skipped" @next="next()" @skip="next(true)" @pause="pause" @resume="resume" @stop="stop" @home="navigate('home')" />
      <HistoryPanel v-if="view === 'history'" :before-clear="beforeClearHistory" :unsaved-count="unsaved.length" @repeat="start" @refresh="loadRecent" @clear-finished="clearingHistory = false" />
      <div v-if="preferenceError" class="save-status" role="status">{{ preferenceError }}</div>
      <div v-if="unsaved.length" class="save-status" role="status">
        {{ unsaved.length }} exercise record(s) awaiting saved history. You can continue.
        <button class="text-button" :disabled="busy" @click="retrySave">Retry saving</button>
        <p class="fine"><span v-for="record in unsaved" :key="record.start.request_id" class="unsaved-record">{{ record.start.skill }} · {{ record.operations.at(-1)?.state || record.saved?.state || 'active' }} · {{ record.error || 'saving' }}</span>Unsaved records remain for this visit; closing or reloading can lose them.</p>
      </div>
      <p v-if="['breathing', 'grounding'].includes(view) && saved && !currentRecord?.operations.length && !currentRecord?.error" class="saved-note fine">Saved locally · {{ saved.state }}</p>
    </main>

    <footer class="site-footer">
      <p>Fictional coursework prototype <span aria-hidden="true">·</span> Not monitored</p>
      <button class="support-button" @click="openSupport"><span aria-hidden="true">♡</span> Support resources <span aria-hidden="true">↗</span></button>
    </footer>
    <SupportPanel v-if="support" @close="support = false" />
  </div>
</template>
