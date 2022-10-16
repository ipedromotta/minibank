import { ref } from 'vue'
import { defineStore } from 'pinia'

export const usePageStore = defineStore('page', () => {
  const isAuthenticated = ref(false)
  const token = ref('')

  function initializeStore() {
    if (localStorage.getItem('token')) {
      token.value = localStorage.getItem('token')
      isAuthenticated.value = true
    } else {
      token.value = ''
      isAuthenticated.value = false
    }
  }

  function setToken(tokenValue) {
    token.value = tokenValue
    isAuthenticated.value = true
  }

  function removeToken() {
    token.value = ''
    isAuthenticated.value = false
  }

  return { initializeStore, isAuthenticated, setToken, removeToken }
})
