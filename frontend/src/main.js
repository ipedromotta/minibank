import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import axios from 'axios'

import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.min.js'

// axios.defaults.baseURL = 'http://localhost:8000'

axios.defaults.baseURL = import.meta.env.VITE_API_URL // Produção

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
