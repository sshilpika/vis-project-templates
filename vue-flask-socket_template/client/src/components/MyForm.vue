

<script setup>
import { ref } from 'vue'
import { socket } from "@/socket";
let isLoading = false,
    value=ref("test...");

socket.on("my response", function(data) {
  console.log("Got response from server! ",data)
  isLoading = false;
  value.value = data.message;
});

function onSubmit(elem) {
  isLoading = true;
  socket.emit('my event', {data: 'I\'m connected! '+value.value});
}
</script>

<template>
  <form @submit.prevent="onSubmit">
    <input v-model="value" />

    <button type="submit" :disabled="isLoading">Submit</button>
  </form>
</template>