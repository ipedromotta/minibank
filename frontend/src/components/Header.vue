<template>
  <nav class="navbar navbar-expand-md navbar-dark bg-dark">
    <div class="container-fluid">
      <img src="@/assets/logo.svg" alt="logo" width="40">

      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarCollapse">
        <ul class="navbar-nav me-auto mb-2 mb-md-0">
          <li class="nav-item">
            <RouterLink to="/inicio" :class="`nav-link ${router.currentRoute.value.name === 'home'? 'active': ''}`">Início</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink to="/extrato" :class="`nav-link ${router.currentRoute.value.name === 'extrato'? 'active': ''}`">Extrato</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink to="/minha-conta" :class="`nav-link ${router.currentRoute.value.name === 'minha-conta'? 'active': ''}`">Minha conta</RouterLink>
          </li>
        </ul>
        <div class="d-flex">
          <p class="text-white-50 p-2 mb-0">Olá, {{ pageStore.user.name }}</p>
          <p class="text-white-50 p-2 mb-0">Saldo: {{ parseFloat(pageStore.user.balance).toLocaleString('pt-br',{style: 'currency', currency: 'BRL'}) }}</p>
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

<style scoped>
img {
  filter: invert(1);
  margin-right: 10px;
}
</style>
