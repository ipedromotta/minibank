<template>
  <Header v-if="pageStore.isAuthenticated" />
  <RouterView />
</template>

<script setup>
import { onMounted } from 'vue';
import { RouterView } from 'vue-router'
import Header from './components/Header.vue';
import { usePageStore } from './stores/page';

const pageStore = usePageStore()

onMounted(() => {
  pageStore.initializeStore()
})
</script>
