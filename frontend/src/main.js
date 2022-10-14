import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import axios from 'axios'

import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.min.js'

const host = window.location.hostname
const port = window.location.port
axios.defaults.baseURL = `http://${host}:${port}`

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
