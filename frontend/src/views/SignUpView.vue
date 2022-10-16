<template>
  <div class="text-center body">
    <main class="form-signin">
      <form class="space-between" @submit.prevent="onSubmit">
        <img class="mb-4" src="@/assets/logo.svg" alt="" width="150">
        <h1 class="h3 mb-3 fw-normal">Cadastre-se</h1>

        <div class="form-floating mb-2">
          <input v-model="form.name" required type="text" maxlength="15" class="form-control" id="floatingName" placeholder="Seu nome">
          <label for="floatingName">Nome</label>
        </div>

        <div class="form-floating mb-2">
          <input v-model="form.email" required type="email" maxlength="15" class="form-control" id="floatingEmail" placeholder="email@exemplo.com">
          <label for="floatingEmail">Email</label>
        </div>

        <div class="form-floating mb-2">
          <input v-model="form.username" required type="text" maxlength="15" class="form-control" id="floatingInput" placeholder="seu-usuario">
          <label for="floatingInput">Usuário</label>
        </div>

        <div class="form-floating mb-2">
          <input v-model="form.password" required type="password" class="form-control" id="floatingPassword" placeholder="senha">
          <label for="floatingPassword">Senha</label>
        </div>

        <div class="form-floating">
          <input v-model="form.password_confirm" required type="password" class="form-control" id="floatingPassword2" placeholder="confirme sua senha">
          <label for="floatingPassword2">Confirme sua senha</label>
        </div>

        <div class="alert alert-danger mt-3" role="alert" v-if="errors.length">
          <span v-for="error in errors" :key="error">{{ error }}</span>
        </div>

        <button :class="`w-100 btn btn-lg btn-dark ${errors.length?'mt-0': 'mt-5'}`" type="submit">Cadastrar</button>
        
        <div>
          <p class="mt-5">
            Ou <RouterLink to="/login" class="text-dark fw-bold link">clique aqui</RouterLink> para logar
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

const router = useRouter()
const errors = ref('')
const form = ref({
  first_name: '',
  email: '',
  username: '',
  password: '',
  password_confirm: '',
})

async function onSubmit() {
  errors.value = ''

  if (form.value.password !== form.value.password_confirm) {
    errors.value = 'As senhas não são iguais. Tente novamente'
  }

  if (!errors.value.length) {
    await axios.post('/api/v1/users/', form.value)
    .then((res) => {
      router.push('/login')
    })
    .catch((error) => {
      if ( error.response ) {
        for (const property in error.response.data) {
          errors.value += `${error.response.data[property]}\n`
        }

        console.log(JSON.stringify(error.response.data))
      } else if ( error.message ) {
        errors.value = 'Algo deu errado. Por favor tente novamente.'

        console.log(JSON.stringify(error))
      }
    })
  }
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

.link {
  text-decoration: none;
}
.link:hover{
  cursor: pointer;
  color: #aaaaaa!important;
  transition: ease-in 0.2s;
}
</style>