// Each exercise owns its write queue, so a late response cannot replace another session.
export function createSessionPersistence(api, changed=()=>{}) {
 const records=[];let clearPromise=null;
 function record(start){const value={start,saved:null,operations:[],error:'',running:false,discarded:false,queue:Promise.resolve()};records.push(value);return value;}
 function flush(value){if(value.discarded)return Promise.resolve();if(value.running)return value.queue;value.running=true;value.queue=(async()=>{
  try{if(!value.saved)value.saved=await api('/sessions',{method:'POST',body:value.start});changed();
   while(value.operations.length&&!value.discarded){const operation=value.operations[0];try{value.saved=await api(`/sessions/${value.saved.id}`,{method:'PATCH',body:{...operation,version:value.saved.version}});}catch(error){if(error.status!==409)throw error;const actual=await api(`/sessions/${value.saved.id}`);const matches=['state','active_elapsed_ms','step','cycles'].every(key=>actual[key]===operation[key])&&JSON.stringify(actual.skipped_steps)===JSON.stringify(operation.skipped_steps);value.saved=actual;if(!matches)throw Error('Saved session changed unexpectedly. Reload history to inspect it; queued changes were retained.');}value.operations.shift();changed();}
   value.error='';
  }catch(error){value.error=error.message;}finally{value.running=false;changed();}
 })();return value.queue;}
 return {records,get clearing(){return clearPromise!==null;},create(start){if(clearPromise)return null;const value=record(start);flush(value);changed();return value;},update(value,body){if(clearPromise||!value||value.discarded)return false;value.operations.push({...body,skipped_steps:[...body.skipped_steps]});if(!value.error)flush(value);changed();},retry(value){return flush(value);},async retryAll(){for(const value of records.filter(r=>!r.saved||r.operations.length||r.error))await flush(value);},discardAll(){if(clearPromise)return clearPromise;const old=[...records];for(const record of old)record.discarded=true;clearPromise=(async()=>{try{await Promise.all(old.map(r=>r.queue));for(const record of old){const index=records.indexOf(record);if(index>=0)records.splice(index,1);}changed();}finally{clearPromise=null;}})();return clearPromise;},get pending(){return records.filter(r=>!r.saved||r.operations.length||r.error);}};
}
