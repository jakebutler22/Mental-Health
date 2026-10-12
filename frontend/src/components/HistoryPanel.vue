<script setup>
import { ref, onMounted } from 'vue';
import { api } from '../lib/api.js';

const props = defineProps({ beforeClear: Function, unsavedCount: Number });
const emit = defineEmits(['repeat', 'refresh', 'clear-finished']);
const sessions = ref([]);
const conversations = ref([]);
const detail = ref(null);
const error = ref('');
const loading = ref(false);
const moreSessions = ref(false);
const moreConversations = ref(false);
const confirmDelete = ref(false);
const clearing = ref(false);
const name = skill => skill === 'breathing' ? 'breathing' : skill === 'grounding' ? 'grounding' : 'neither';
const date = value => new Date(value).toLocaleString(undefined, { dateStyle: 'medium', timeStyle: 'short' });

async function load() {
  loading.value = true;
  error.value = '';
  try {
    const [savedSessions, savedConversations] = await Promise.all([api('/sessions'), api('/conversations')]);
    sessions.value = savedSessions.items;
    conversations.value = savedConversations.items;
    moreSessions.value = savedSessions.items.length === 20;
    moreConversations.value = savedConversations.items.length === 20;
  } catch (failure) {
    error.value = failure.message;
  } finally {
    loading.value = false;
  }
}

async function more(kind) {
  loading.value = true;
  try {
    const records = kind === 'sessions' ? sessions : conversations;
    const response = await api(`/${kind}?limit=20&offset=${records.value.length}`);
    records.value.push(...response.items);
    if (kind === 'sessions') moreSessions.value = response.items.length === 20;
    else moreConversations.value = response.items.length === 20;
  } catch (failure) {
    error.value = failure.message;
  } finally {
    loading.value = false;
  }
}

async function open(id) {
  try { detail.value = await api(`/conversations/${id}`); }
  catch (failure) { error.value = failure.message; }
}

async function clear() {
  if (clearing.value) return;
  clearing.value = true;
  try {
    await props.beforeClear?.();
    await api('/history', { method: 'DELETE' });
    detail.value = null;
    confirmDelete.value = false;
    await load();
    emit('refresh');
  } catch (failure) {
    error.value = failure.message;
  } finally {
    clearing.value = false;
    emit('clear-finished');
  }
}

onMounted(load);
</script>

<template>
  <section class="card history">
    <span class="eyebrow">Your local history</span>
    <h2>Little moments, kept.</h2>
    <p class="fine">One local history for fictional coursework. Recommendations and choices describe activity, not clinical progress or a profile.</p>
    <p v-if="loading" role="status">Loading saved history…</p>
    <p v-if="error" class="error" role="alert">{{ error }} <button class="text-button" @click="load">Retry</button></p>
    <h3>Exercises</h3>
    <p v-if="!loading && !sessions.length" class="fine">No saved exercises yet.</p>
    <article v-for="session in sessions" :key="session.id" class="history-row">
      <div>
        <strong>{{ session.skill === 'breathing' ? 'Paced breathing' : 'Sensory grounding' }}</strong>
        <p class="fine">{{ date(session.started_at) }} · {{ Math.round(session.active_elapsed_ms / 1000) }}s active · {{ session.state }}<span v-if="session.skipped_steps.length"> · {{ session.skipped_steps.length }} skipped</span></p>
        <p class="fine"><template v-if="session.recommendation_request_id">Guac recommended {{ name(session.recommended_skill) }} · You chose {{ name(session.skill) }}<br>{{ session.recommendation_reason }}</template><template v-else>{{ session.conversation_id ? 'No linked recommendation' : 'Direct choice' }} · You chose {{ name(session.skill) }}</template></p>
        <button v-if="session.conversation_id" class="text-button" :disabled="clearing" @click="open(session.conversation_id)">View linked conversation</button>
      </div>
      <button class="secondary small" :disabled="clearing" @click="emit('repeat', session.skill)">Repeat</button>
    </article>
    <button v-if="moreSessions" class="text-button" :disabled="loading || clearing" @click="more('sessions')">Load more exercises</button>
    <h3>Conversations</h3>
    <button v-for="conversation in conversations" :key="conversation.id" class="conversation-row" :disabled="clearing" @click="open(conversation.id)"><span>{{ conversation.fictional_title || 'Fictional conversation' }}</span><small>{{ date(conversation.created_at) }}</small></button>
    <p v-if="!loading && !conversations.length" class="fine">No saved conversations yet.</p>
    <button v-if="moreConversations" class="text-button" :disabled="loading || clearing" @click="more('conversations')">Load more conversations</button>
    <section v-if="detail" class="transcript">
      <h3>Saved conversation</h3>
      <p v-if="!detail.messages.length" class="fine">No messages.</p>
      <article v-for="message in detail.messages" :key="message.id">
        <span class="eyebrow">{{ message.role === 'assistant' ? 'Guac' : 'Fictional student' }} · {{ message.status }} · {{ message.mode || '' }}</span>
        <p>{{ message.text }}</p>
        <div v-if="message.role === 'assistant' && message.recommendation" class="history-recommendation">
          <p class="fine">Recommendation: {{ name(message.recommendation.recommended_skill ?? message.recommendation.suggested_skill) }}<br>{{ message.recommendation.reason || 'Reason not stored in the earlier version.' }}</p>
          <p v-if="message.recommendation.clarification" class="fine">Optional question: {{ message.recommendation.clarification }}</p>
          <p class="fine">{{ detail.sessions.filter(session => session.recommendation_request_id === message.request_id).length ? 'A linked deliberate choice appears in the exercise history.' : 'No exercise choice is recorded for this recommendation.' }}</p>
        </div>
      </article>
      <button class="text-button" @click="detail = null">Close transcript</button>
    </section>
    <div class="history-delete">
      <button v-if="!confirmDelete" class="text-button" @click="confirmDelete = true">Clear local history…</button>
      <template v-else>
        <p>Delete saved conversations and exercises? Preferences stay as chosen. This also discards {{ unsavedCount || 0 }} unsaved exercise record(s) and resets the current chat.</p>
        <button class="secondary" :disabled="clearing" @click="clear">Delete history</button>
        <button class="text-button" :disabled="clearing" @click="confirmDelete = false">Cancel</button>
      </template>
    </div>
  </section>
</template>
