<template>
  <nav class="navbar navbar-expand-md navbar-dark bg-dark">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Logo</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarCollapse">
        <ul class="navbar-nav me-auto mb-2 mb-md-0">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Início</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Extrato</a>
          </li>
        </ul>
        <div class="d-flex">
          <p class="text-white-50 p-2 mb-0">Olá, {{ pageStore.user.name }}</p>
          <p class="text-white-50 p-2 mb-0">Saldo: {{ pageStore.user.balance }}</p>
          <button @click="logout" class="btn btn-outline-light" type="button">Sair</button>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup>
import axios from 'axios';
import { useRouter } from 'vue-router';
import { usePageStore } from '../stores/page';


const pageStore = usePageStore()
const router = useRouter()

function logout() {
  
  const token = localStorage.getItem("token")

  localStorage.removeItem("token")
  axios.post('/api/v1/token/logout/', token)
    .catch((error) => {
      console.log(error)
    })
  
  axios.defaults.headers.common["Authorization"] = ""
  pageStore.removeToken()
  router.push('/login')
}
</script>