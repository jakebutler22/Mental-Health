<script setup>
import { ref, computed, watch, onMounted, onUnmounted } from 'vue';
import GuacMark from './GuacMark.vue';
import RecommendationPanel from './RecommendationPanel.vue';
import { createApi } from '../lib/api.js';
import { createChatController, crisisOffer } from '../controllers/chatController.js';

const emit = defineEmits(['choose', 'conversation', 'support']);
const props = defineProps({ active: Boolean });
const api = createApi(fetch, 25000);
const controller = createChatController(api);
const input = ref('');
const messages = ref([]);
const loading = ref(false);
const error = ref('');
const health = ref(null);
const offer = ref(false);
const recommendation = ref(null);
const recommendationRequest = ref(null);
const declined = ref(false);
const retrySame = ref(true);

const status = computed(() => {
  if (!health.value) return 'Chat status unavailable';
  if (health.value.mode === 'mock') return 'Mock mode · simulated replies';
  if (health.value.configuration_status === 'missing_configuration') return 'Live mode · missing configuration';
  return `Live mode · ${health.value.live_verified ? 'provider verified' : 'provider not yet verified'}`;
});
const hasPrimaryRecommendation = computed(() => recommendation.value?.recommended_skill && !declined.value);

watch(() => props.active, active => {
  if (!active) {
    controller.invalidate();
    loading.value = false;
  }
});

async function send(retry = false) {
  if (loading.value) return;
  offer.value = crisisOffer(input.value);
  loading.value = true;
  error.value = '';
  recommendation.value = null;
  declined.value = false;
  const outcome = await controller.send(input.value, retry);
  if (outcome.stale || outcome.ignored) return;
  loading.value = false;
  if (outcome.error) {
    error.value = outcome.error.message;
    retrySame.value = true;
    return;
  }
  const data = outcome.value;
  emit('conversation', controller.conversationId);
  for (const message of data.messages) {
    if (!messages.value.some(saved => saved.id === message.id)) {
      messages.value.push({ ...message, mode: data.mode });
    }
  }
  if (data.status === 'succeeded') {
    recommendation.value = data.result;
    recommendationRequest.value = data.request_id;
    input.value = '';
    if (health.value && data.mode === 'live') health.value.live_verified = true;
  } else {
    retrySame.value = false;
    error.value = `Chat ${data.status} (${data.error_code || 'no response'}). Both exercises are still available.`;
  }
}

function decline() {
  recommendation.value = null;
  declined.value = true;
}

function choose(selection) {
  emit('choose', selection);
}

function reset() {
  controller.reset();
  messages.value = [];
  error.value = '';
  input.value = '';
  recommendation.value = null;
  recommendationRequest.value = null;
  loading.value = false;
  offer.value = false;
  declined.value = false;
  emit('conversation', null);
}

onMounted(async () => {
  try { health.value = await api('/health'); }
  catch { error.value = 'Chat status is unavailable. Exercises and support still work.'; }
});
onUnmounted(() => controller.invalidate());
</script>

<template>
  <section class="chat-card card" aria-label="Optional fictional conversation">
    <div class="chat-top">
      <div class="chat-identity"><GuacMark /><div><strong>Guac</strong><span class="fine">A moment, your way.</span></div></div>
      <button class="text-button" @click="reset">New conversation</button>
    </div>
    <p v-if="!messages.length" class="chat-welcome">What’s taking up space today?</p>
    <div class="chat-messages" aria-live="polite">
      <article v-for="message in messages" :key="message.id" :class="message.role">
        <span class="eyebrow">{{ message.role === 'user' ? 'Fictional student' : 'Guac' }} · {{ message.mode }} · {{ message.status }}</span>
        <p>{{ message.text }}</p>
      </article>
    </div>
    <RecommendationPanel v-if="recommendation" :result="recommendation" :request-id="recommendationRequest" @choose="choose" @decline="decline" />
    <div v-if="declined" class="decline-note" role="status"><p>Neither is okay. We can leave it here.</p></div>
    <p v-if="offer" class="support-offer">Support is available independently of this chat. <button class="text-button" @click="emit('support')">Open support resources</button></p>
    <form @submit.prevent="send()">
      <label class="sr-only" for="chat-input">Optional fictional message</label>
      <textarea id="chat-input" v-model="input" maxlength="500" rows="2" placeholder="For example: I feel wound up about tomorrow’s exam…" :disabled="loading" />
      <div class="chat-actions">
        <span class="fine">{{ input.length }} / 500 · optional</span>
        <button :class="[hasPrimaryRecommendation ? 'secondary' : 'primary', 'small']" :disabled="loading || !input.trim()" type="submit">{{ loading ? 'Thinking…' : 'Send →' }}</button>
      </div>
    </form>
    <p v-if="loading" role="status" class="fine">Waiting for chat. You can begin either exercise now.</p>
    <p v-if="error" class="error" role="alert">{{ error }} <button v-if="controller.pending" class="text-button" :disabled="loading" @click="send(retrySame)">{{ retrySame ? 'Check same request' : 'Send again' }}</button></p>
    <p class="chat-status fine">{{ status }} · fictional scenarios only</p>
  </section>
</template>
