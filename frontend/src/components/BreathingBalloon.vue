<script setup>
import {computed,ref} from 'vue';
const props=defineProps({inflation:Number,color:{type:String,default:'red'},reduced:Boolean});const failed=ref(false);
const style=computed(()=>{const p=props.reduced?.55:props.inflation;return {transform:`scale(${.66+.34*p}, ${.75+.25*p})`,filter:({red:'none',sage:'hue-rotate(105deg) saturate(.42)',blue:'hue-rotate(205deg) saturate(.6)',plum:'hue-rotate(300deg) saturate(.65)'})[props.color]};});
</script>
<template><div class="balloon-stage" :data-inflation="inflation" aria-hidden="true"><div class="balloon-shadow"></div><img v-if="!failed" src="/balloon.png" alt="" class="balloon" :style="style" @error="failed=true"><div v-else class="balloon-fallback" :style="style"><span></span><small>Visual asset pending</small></div></div></template>
