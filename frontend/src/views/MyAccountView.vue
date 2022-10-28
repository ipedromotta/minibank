<template>
  <div class="container text-center mx-auto mt-5">
    <h1>Detalhes da conta</h1>

    <form class="row g-3 w-50 mx-auto mt-3">
      <div class="col-md-6">
        <label for="inputName" class="form-label">Nome</label>
        <input v-model="usernameSets.name" type="text" max="15" class="form-control" :disabled="disableForm" id="inputName" placeholder="Seu nome">
      </div>
      <div class="col-md-6">
        <label for="inputUser" class="form-label">Usuario</label>
        <input v-model="usernameSets.username" type="text" max="15" class="form-control" id="inputUser" :disabled="disableForm" placeholder="Seu usuario">
      </div>
      <div class="col-12">
        <label for="inputEmail" class="form-label">Email</label>
        <input v-model="usernameSets.email" :disabled="disableForm" type="email" class="form-control" id="inputEmail" placeholder="seuemail@exemplo.com">
      </div>



      <div class="col-12" v-if="disableForm">
        <button @click="enableForm" type="button" class="btn btn-dark">Alterar dados</button>
      </div>
      <div class="col-12" v-else>
        <div class="btn-group" role="group">
          <button @click="enableForm" type="button" class="btn btn-secondary">Cancelar</button>
          <button type="button" class="btn btn-dark"  @click="validateForm">Salvar Alterações</button>
        </div>
      </div>

      <div v-if="errors.length" class="alert alert-danger" role="alert">
        {{ errors }}
      </div>
      <div v-if="success.length" class="alert alert-success" role="alert">
        {{ success }}
      </div>
    </form>

    <div class="border border-danger w-25 mx-auto p-2 mt-5">
      <p class="text-danger fw-bold fs-5">Zona de perigo</p>
      <div class="btn-group" role="group">
        <button type="button" class="btn btn-dark" data-bs-toggle="modal" data-bs-target="#passwordModal">Alterar senha</button>
        <button type="button" class="btn btn-danger" data-bs-toggle="modal" data-bs-target="#deleteModal">Excluir conta</button>
      </div>
    </div>
  </div>

  <!-- Delete Modal -->
  <div class="modal fade" id="deleteModal" tabindex="-1" aria-labelledby="deleteModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="deleteModalLabel">Confirmação de exclusão</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">

          <div class="col-12">
            <label for="deletePassword" class="form-label">Digite sua senha</label>
            <input v-model="deletePassword.current_password" type="password" class="form-control" id="deletePassword">
          </div>
          
        </div>
        <div v-if="errors.length" class="alert alert-danger w-75 mx-auto text-center" role="alert">
          {{ errors }}
        </div>
        <div class="modal-footer">
          <button @click="setDeleteForm" ref="closeDeleteModal" type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
          <button type="button" @click="deleteUser" class="btn btn-danger">Confirmar exclusão</button>
        </div>
      </div>
    </div>
  </div>

  <!-- Change Modal -->
  <div class="modal fade" id="changeModal" tabindex="-1" aria-labelledby="changeModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="changeModalLabel">Confirmar alterações</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          
          <div class="col-12">
            <label for="inputPassword" class="form-label">Digite sua senha</label>
            <input v-model="usernameSets.current_password" :disabled="disableForm" type="password" class="form-control" id="inputPassword">
          </div>

        </div>
        <div class="modal-footer">
          <button ref="closeModal" type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
          <button @click="updateUser($refs.closeModal)" type="button" class="btn btn-dark">Confirmar</button>
        </div>
      </div>
    </div>
  </div>

  <!-- Password Modal -->
  <div class="modal fade" id="passwordModal" tabindex="-1" aria-labelledby="passwordModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="passwordModalLabel">Alterar senha</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          
          <div class="col-12">
            <label for="currentPassword" class="form-label">Senha atual</label>
            <input v-model="passwordSets.current_password" type="password" class="form-control" id="currentPassword">
          </div>
          <div class="col-12 mt-2">
            <label for="newPassword" class="form-label">Digite sua nova senha</label>
            <input v-model="passwordSets.new_password" type="password" class="form-control" id="newPassword">
          </div>
          <div class="col-12 mt-2">
            <label for="reNewPassword" class="form-label">Confirme sua nova senha</label>
            <input v-model="passwordSets.re_new_password" type="password" class="form-control" id="reNewPassword">
          </div>

        </div>
        <div v-if="errors.length" class="alert alert-danger w-75 mx-auto text-center" role="alert">
          {{ errors }}
        </div>
        <div class="modal-footer">
          <button @click="setPasswordForm" ref="closeModal" type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
          <button @click="updatePassword($refs.closeModal)" type="button" class="btn btn-dark">Confirmar</button>
        </div>
      </div>
    </div>
  </div>

</template>

<script setup>
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';
import { usePageStore } from '../stores/page';


const pageStore = usePageStore()
const disableForm = ref(true)
const success = ref('')
const errors = ref('')
const router = useRouter()
const deletePassword = ref({
  current_password: ''
})
const usernameSets = ref({
  username: '',
  email: '',
  name: '',
  current_password: ''
})
const passwordSets = ref({
  new_password: '',
  re_new_password: '',
  current_password: ''
})

function updateUser(closeModal) {
  axios.post(`/api/v1/update/`,  usernameSets.value)
  .then((res) => {
    if (res.data.status === 200) {
      success.value = res.data.response
      pageStore.initializeStore()
      usernameSets.value.current_password = ''
    } else {
      errors.value = res.data.response
      setForm()
    }
  })
  .catch((error) => {
    errors.value = "Algo deu errado!"
    setForm()
    console.log(error.response.data)
  })
  setTimeout(() => {
    errors.value = ''
    success.value = ''
  }, 2500)

  closeModal.click()
  disableForm.value = true
}

function enableForm() {
  disableForm.value = !disableForm.value
  setForm()
}

function setForm() {
  usernameSets.value.username = pageStore.user.username
  usernameSets.value.email = pageStore.user.email
  usernameSets.value.name = pageStore.user.name
  usernameSets.value.current_password = ''
}

function validateForm() {
  if (!usernameSets.value.username || !usernameSets.value.name || !usernameSets.value.email) {
    errors.value = "Preencha todos os campos"
    setTimeout(() => {
      errors.value = ''
    }, 2500)
    return
  }
  $('#changeModal').modal('show')
}

function updatePassword(closeModal) {
  console.log(passwordSets.value)

  if (passwordSets.value.new_password !== passwordSets.value.re_new_password) {
    errors.value = 'Senhas não correspondem'
    return
  }
  if (!passwordSets.value.new_password || !passwordSets.value.re_new_password || !passwordSets.value.current_password) {
    errors.value = 'Preencha todos os campos'
    return
  }

  axios.post('/api/v1/users/set_password/', passwordSets.value)
    .then((res) => {
      success.value = 'Senha alterada com sucesso'
      closeModal.click()
      setTimeout(() =>{
        success.value = ''
      }, 2500)
    })
    .catch((error) => {
      if (error.response) {
        for (const property in error.response.data) {
          errors.value = `${error.response.data[property]}`
        }
      } else {
        errors.value = 'Algo deu errado. Por favor tente novamente'
      }
    })

}

function setPasswordForm() {
  passwordSets.value.new_password = ''
  passwordSets.value.re_new_password = ''
  passwordSets.value.current_password = ''
  errors.value = ''
}

function deleteUser() {
  if (!deletePassword.value.current_password.length) {
    errors.value = 'Digite sua senha'
    return
  }
  axios.delete('/api/v1/users/me/', {data:deletePassword.value})
  .then((res) => {
    router.go()
  })
  .catch((error) => {
    if (error.response) {
      for (const property in error.response.data) {
        errors.value = `${error.response.data[property]}`
      }
    } else {
      errors.value = 'Algo deu errado. Por favor tente novamente'
    }
  })
}

function setDeleteForm() {
  errors.value = ''
  deletePassword.value.current_password = ''
}

onMounted(() => {
  setForm()
})

</script>