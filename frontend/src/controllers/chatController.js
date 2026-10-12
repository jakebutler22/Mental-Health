import { validateRecommendation } from './recommendation.js';
import { createRequestGate } from '../lib/api.js';

export const crisisOffer = text => /\b(kill myself|suicide|hurt myself|immediate danger)\b/i.test(text);

export function validateChatResponse(data) {
  if (!data || !['succeeded', 'failed', 'pending', 'interrupted'].includes(data.status)
      || !['mock', 'live'].includes(data.mode) || !Array.isArray(data.messages)) {
    throw new Error('No usable chat result. Both exercises remain available.');
  }
  if (data.status === 'succeeded') {
    validateRecommendation(data.result);
    if (!Array.isArray(data.result.choices)
        || data.result.choices.length !== 2
        || !['breathing', 'grounding'].every(skill => data.result.choices.includes(skill))) {
      throw new Error('The exercise choices were unreadable. Both exercises remain available.');
    }
  }
  return data;
}

export function createChatController(api) {
  const gate = createRequestGate();
  let conversationId = null;
  let pending = null;

  return {
    get conversationId() { return conversationId; },
    get pending() { return pending; },
    invalidate() { gate.invalidate(); },
    reset() {
      gate.invalidate();
      conversationId = null;
      pending = null;
    },
    async send(text, retry = false) {
      const trimmed = text.trim();
      if (!trimmed || trimmed.length > 500) {
        return { error: new Error('Enter 1–500 characters, or choose an exercise directly.') };
      }
      return gate.run(async signal => {
        if (!conversationId) {
          const conversation = await api('/conversations', { method: 'POST', body: {}, signal });
          if (signal.aborted) return null;
          conversationId = conversation.id;
        }
        if (!retry || !pending) pending = { request_id: crypto.randomUUID(), text: trimmed };
        return validateChatResponse(await api(`/conversations/${conversationId}/messages`, {
          method: 'POST', body: pending, signal,
        }));
      });
    },
  };
}
