export const SKILLS = ['breathing', 'grounding'];
export function validateRecommendation(result) {
  if (!result || typeof result.reflection !== 'string' || !result.reflection.trim() || result.reflection.length > 400) {
    throw new Error('No usable reflection was returned. Both exercises are available.');
  }
  if (result.recommended_skill !== null && !SKILLS.includes(result.recommended_skill)) {
    throw new Error('The suggested exercise is unavailable. You can choose either exercise directly.');
  }
  if (typeof result.reason !== 'string' || result.reason.length > 300) {
    throw new Error('No usable reason was returned. Both exercises are available.');
  }
  if (result.recommended_skill && !result.reason.trim()) throw new Error('No recommendation reason was returned.');
  if (result.clarification !== null && result.clarification !== undefined && (typeof result.clarification !== 'string' || result.clarification.length > 250)) {
    throw new Error('The optional question was unreadable. You can choose either exercise directly.');
  }
  if (!['offer', 'clarify', 'decline'].includes(result.action)) throw new Error('No usable recommendation action was returned.');
  if (result.action !== 'offer' && result.recommended_skill !== null) throw new Error('The recommendation contradicts the selected action.');
  if (result.action === 'decline' && result.clarification) throw new Error('A declined exercise cannot require another answer.');
  if (result.action === 'clarify' && !result.clarification) throw new Error('No optional question was returned.');
  return result;
}
export function recommendationActions(result, requestId) {
  validateRecommendation(result);
  if (!result.recommended_skill) return { primary: null, alternative: null };
  return {
    primary: { skill: result.recommended_skill, recommendation_request_id: requestId },
    alternative: { skill: result.recommended_skill === 'breathing' ? 'grounding' : 'breathing', recommendation_request_id: requestId },
  };
}
