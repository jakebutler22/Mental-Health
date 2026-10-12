export class ApiError extends Error { constructor(message,status=0,code='unavailable'){super(message);this.status=status;this.code=code;} }
export function createApi(fetcher=fetch, timeoutMs=8000) {
 return async (path, options={}) => {
  const controller=new AbortController();const signal=options.signal ? AbortSignal.any([options.signal,controller.signal]) : controller.signal;let timer;
  const timeout=new Promise((_,reject)=>{timer=setTimeout(()=>{controller.abort();reject(new ApiError('The request timed out. Exercises and support still work.',0,'timeout'));},timeoutMs);});
  try{return await Promise.race([(async()=>{
   let response;try {response=await fetcher(`/api${path}`,{...options,signal,headers:{'Content-Type':'application/json',...options.headers},body:options.body === undefined ? undefined : JSON.stringify(options.body)});}
   catch(error){if(error.name==='AbortError'&&options.signal?.aborted)throw error;if(controller.signal.aborted)throw new ApiError('The request timed out. Exercises and support still work.',0,'timeout');throw new ApiError('Connection unavailable. Your exercises and support still work.');}
   let data;try{data=await response.json();}catch{throw new ApiError('No readable response. Try again.',response.status,'invalid_response');}
   if(!response.ok)throw new ApiError(data.detail?.message || (typeof data.detail === 'string' ? data.detail : 'The request could not be saved. Try again.'),response.status,data.detail?.code);
   if(data===null || typeof data!=='object')throw new ApiError('No result was returned.',response.status,'empty_response');
   return data;
  })(),timeout]);}finally{clearTimeout(timer);}
 };
}
// At most one request, generation check for late/stale responses after navigation.
export function createRequestGate(){let generation=0,busy=false,controller=null;return {
 invalidate(){generation++;controller?.abort();busy=false;},
 async run(task){if(busy)return {ignored:true};busy=true;const token=++generation;controller=new AbortController();try{const value=await task(controller.signal);return token===generation?{value}:{stale:true};}catch(error){if(token!==generation || error.name==='AbortError')return {stale:true};return {error};}finally{if(token===generation){busy=false;controller=null;}}},
 get busy(){return busy;}
};}
export const api=createApi();
