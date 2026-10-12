import test from 'node:test';
import assert from 'node:assert/strict';
import {createExerciseClock,breathingAt,groundingSteps,breathingRecordTime} from '../src/controllers/exerciseClock.js';
test('4/6 six cycles; endpoints continuous; terminal stays minimum',()=>{
 assert.equal(breathingAt(3999).phase,'inhale'); assert.equal(breathingAt(4000).phase,'exhale'); assert.equal(breathingAt(4000).inflation,1);
 assert.ok(breathingAt(9999).inflation < .00001); assert.equal(breathingAt(10000).inflation,0);
 assert.equal(breathingAt(59999).cycle,6); assert.equal(breathingAt(60000).phase,'done'); assert.equal(breathingAt(90000).inflation,0);
});
test('pause freezes clock and balloon in inhale and exhale; repeats ignored',()=>{
 let time=0;const clock=createExerciseClock(()=>time);assert.equal(clock.start(),true);assert.equal(clock.start(),false);
 time=2000;clock.pause();let frozen=clock.snapshot();time=100000;assert.deepEqual(clock.snapshot(),frozen);clock.resume();time+=3000;assert.equal(clock.snapshot().elapsedMs,5000);clock.pause();frozen=clock.snapshot();time+=50000;assert.deepEqual(clock.snapshot(),frozen);clock.resume();time+=1000;assert.equal(clock.snapshot().elapsedMs,6000);clock.finish('stopped');time+=1000;assert.equal(clock.snapshot().elapsedMs,6000);assert.equal(clock.resume(),false);
});
test('fixed sensory sequence',()=>assert.deepEqual(groundingSteps.map(s=>s.count),[5,4,3,2,1]));

test('stored elapsed and cycle counter agree at fractional10second boundary',()=>{assert.deepEqual(breathingRecordTime(9999.6),{active_elapsed_ms:9999,cycles:0});assert.deepEqual(breathingRecordTime(10000.1),{active_elapsed_ms:10000,cycles:1});assert.deepEqual(breathingRecordTime(60000.8),{active_elapsed_ms:60000,cycles:6});});
