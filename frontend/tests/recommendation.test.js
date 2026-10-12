import test from 'node:test';
import assert from 'node:assert/strict';
import {validateRecommendation, recommendationActions} from '../src/controllers/recommendation.js';
const breathing={reflection:'That exam sounds like a keyed-up moment.',recommended_skill:'breathing',reason:'A steady rhythm offers something simple to follow.',clarification:null,action:'offer'};
test('one-action acceptance and easy alternative retain originating request',()=>{
 const actions=recommendationActions(breathing,'request-1');
 assert.deepEqual(actions.primary,{skill:'breathing',recommendation_request_id:'request-1'});
 assert.deepEqual(actions.alternative,{skill:'grounding',recommendation_request_id:'request-1'});
});
test('neither/stop produce no primary action or persuasive fallback',()=>{
 const declined={reflection:'You can leave it here.',recommended_skill:null,reason:'',clarification:null,action:'decline'};
 assert.deepEqual(recommendationActions(declined,'request-2'),{primary:null,alternative:null});
});
test('unsupported recommendations, missing reason and mandatory-shaped malformed question rejected',()=>{
 assert.throws(()=>validateRecommendation({...breathing,recommended_skill:'reframe'}));
 assert.throws(()=>validateRecommendation({...breathing,reason:''}));
 assert.throws(()=>validateRecommendation({...breathing,clarification:{required:true}}));
});

test('vague follow-up without a second question keeps both direct options',()=>{const result={reflection:'It can stay mixed.',recommended_skill:null,reason:'No reply is required.',clarification:null,action:'offer'};assert.deepEqual(recommendationActions(result,'request-3'),{primary:null,alternative:null});});
test('current alternative is deliberate and persists separately from original recommendation',async()=>{
 const {createSessionPersistence}=await import('../src/controllers/sessionPersistence.js');
 const calls=[];
 const store=createSessionPersistence(async(path,options)=>{calls.push(options.body);return {id:'chosen',version:0,...options.body};});
 const {alternative}=recommendationActions(breathing,'current-recommendation');
 const record=store.create({request_id:'session-current',conversation_id:'conversation-current',...alternative});
 await record.queue;
 assert.equal(calls[0].skill,'grounding');
 assert.equal(calls[0].recommendation_request_id,'current-recommendation');
 assert.equal(breathing.recommended_skill,'breathing');
});
