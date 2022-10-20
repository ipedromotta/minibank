import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const usePageStore = defineStore('page', () => {
  const isAuthenticated = ref(false)
  const token = ref('')
  const user = ref({
    name: '',
    email: '',
    username: '',
    balance: 0,
  })
  const router = useRouter()
  const passwordIsValid = ref(false)

  function initializeStore() {
    if (localStorage.getItem('token')) {
      token.value = localStorage.getItem('token')

      axios.defaults.headers.common["Authorization"] = `Token ${token.value}`

      axios.get('/api/v1/users/me/')
        .then((res) => {
          user.value.name = res.data.first_name
          user.value.username = res.data.username
          user.value.email = res.data.email
          user.value.balance = res.data.balance
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


  async function verifyPassword(password) {
    const password_ = {
      new_password: password,
      re_new_password: password,
      current_password: password
    }
    await axios.post('/api/v1/users/set_password/', password_)
      .then((res) => {
        passwordIsValid.value = true
      })
      .catch((error) => {
        passwordIsValid.value = false
      })
  }

  return { user, initializeStore, isAuthenticated, setToken, removeToken, verifyPassword, passwordIsValid }
})
