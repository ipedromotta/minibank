import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const usePageStore = defineStore('page', () => {
  const isAuthenticated = ref(false)
  const token = ref('')
  const router = useRouter()

  function initializeStore() {
    if (localStorage.getItem('token')) {
      token.value = localStorage.getItem('token')

      axios.defaults.headers.common["Authorization"] = `Token ${token.value}`

      axios.get('/api/v1/users/me/')
        .then((res) => {
          console.log(res)
        })
        .catch((err) => {
          router.push('/login')
          removeToken()
          localStorage.removeItem('token')
        })
      setToken(token.value)
    } else {
      removeToken()
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
