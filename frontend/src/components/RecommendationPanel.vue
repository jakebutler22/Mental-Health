<script setup>
import { computed } from 'vue';
import { recommendationActions } from '../controllers/recommendation.js';
const props = defineProps({ result: Object, requestId: String });
const emit = defineEmits(['choose', 'decline']);
const actions = computed(() => recommendationActions(props.result, props.requestId));
const names = { breathing: 'breathing', grounding: 'grounding' };
</script>
<template>
  <section v-if="actions.primary" class="recommendation" aria-label="Your optional recommendation">
    <span class="eyebrow">A pause for this moment</span>
    <h3>{{ result.recommended_skill === 'breathing' ? 'A little rhythm.' : 'A little here and now.' }}</h3>
    <p>{{ result.reason }}</p>
    <div class="recommendation-actions">
      <button class="primary" @click="emit('choose', actions.primary)">Begin {{ names[actions.primary.skill] }} <span aria-hidden="true">→</span></button>
      <button class="text-button" @click="emit('choose', actions.alternative)">Try {{ names[actions.alternative.skill] }} instead</button>
    </div>
    <button class="text-button decline-button" @click="emit('decline')">Neither right now</button>
  </section>
  <section v-else-if="result.action === 'clarify'" class="clarification">
    <span class="eyebrow">Only if you’d like</span>
    <p>{{ result.clarification }}</p>
    <p class="fine">No reply needed. Both exercises are ready whenever you are.</p>
  </section>
  <section v-else class="decline-note"><p>{{ result.action === 'decline' ? 'No exercise needed. We can leave it here.' : result.reason }}</p></section>
</template>
