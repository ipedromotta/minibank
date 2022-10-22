<template>
  <Header v-if="pageStore.isAuthenticated" />
  <RouterView />
</template>

<script setup>
import { onMounted, watch } from 'vue';
import { RouterView, useRouter } from 'vue-router'
import Header from './components/Header.vue';
import { usePageStore } from './stores/page';

const pageStore = usePageStore()
const router = useRouter()

watch(() => router.currentRoute.value.path, () => {
  pageStore.initializeStore()
})

onMounted(() => {
  pageStore.initializeStore()
})
</script>
