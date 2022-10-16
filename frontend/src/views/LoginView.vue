<template>
  <div class="text-center body">
    <main class="form-signin">
      <form @submit.prevent="onSubmit">
        <img class="mb-4" src="@/assets/logo.svg" alt="" width="150">
        <h1 class="h3 mb-3 fw-normal">Fazer login</h1>

        <div class="form-floating">
          <input v-model="form.username" type="text" required maxlength="15" class="form-control" id="floatingInput" placeholder="seu-usuario">
          <label for="floatingInput">Usuário</label>
        </div>

        <div class="form-floating">
          <input v-model="form.password" type="password" required class="form-control" id="floatingPassword" placeholder="senha">
          <label for="floatingPassword">Senha</label>
        </div>

        <p :class="`small pb-lg-2 ${errors.length? 'mb-0' : 'mb-5'}`"><a class="text-dark link" href="#!">Esqueceu sua senha?</a></p>

        <div class="alert alert-danger" role="alert" v-if="errors.length">
          <span v-for="error in errors" :key="error">{{ error }}</span>
        </div>
        
        <button class="w-100 btn btn-lg btn-dark" type="submit">Entrar</button>
        
        <div>
          <p class="mt-5">Não tem uma conta? <RouterLink to="/cadastro" class="text-dark fw-bold link">Cadastre-se</RouterLink>
          </p>
        </div>
      </form>
    </main>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { usePageStore } from '../stores/page';


const pageStore = usePageStore()
const router = useRouter()
const errors = ref('')
const form = ref({
  username: '',
  password: ''
})

function onSubmit() {
  axios.defaults.headers.common["Authorization"] = ""

  localStorage.removeItem("token")

  axios.post("/api/v1/token/login/", form.value)
    .then((res) => {
      const token = res.data.auth_token

      pageStore.setToken(token)

      axios.defaults.headers.common["Authorization"] = "Token" + token

      localStorage.setItem("token", token)

      const toPath = router.currentRoute.value.query.to || '/'

      router.push(toPath)
    })
    .catch((error) => {
      if (error.response) {
        for (const property in error.response.data) {
          errors.value = `${error.response.data[property]}`
        }
      } else {
        errors.value = 'Algo deu errado. Por favor tente novamente'
      }
      setTimeout(() => {
        errors.value = ''
      }, 2000)
    })
}

</script>


<style scoped>
.body {
  height: 100vh;
}

.body {
  display: flex;
  align-items: center;
  padding-top: 40px;
  padding-bottom: 40px;
  background-color: #f5f5f5;
}

.form-signin {
  width: 100%;
  max-width: 330px;
  padding: 15px;
  margin: auto;
}

.form-signin .form-floating:focus-within {
  z-index: 2;
}

.form-signin input[type="text"] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}

.form-signin input[type="password"] {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}

.link {
  text-decoration: none;
}
.link:hover{
  cursor: pointer;
  color: #aaaaaa!important;
  transition: ease-in 0.2s;
}
</style>