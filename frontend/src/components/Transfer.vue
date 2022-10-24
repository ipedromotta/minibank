<template>
  <div class="col-sm-6 mx-auto">
    <h2>Transferencia</h2>

    <div class="form-floating mb-3">
      <input v-model="transferInfo.username_to" @input="errors = ''" type="text" class="form-control" id="username_to" placeholder="usuario">
      <label for="username_to">Usuário da conta destinatária</label>
    </div>
    <div class="form-floating">
      <input v-model="password" @input="errors = ''" type="password" class="form-control" id="floatingPassword" placeholder="senha">
      <label for="floatingPassword">Digite sua senha</label>
    </div>
    <div class="mb-3 mt-3">
      <input v-model="transferInfo.amount" type="number" class="form-control form-control-lg" id="amount" placeholder="R$ 0,00">
      <label for="amount" class="form-label mt-3 text">Valor da transferencia {{ amountCurrency }}</label>
    </div>

    <div class="alert alert-danger" role="alert" v-if="errors.length">
      <span v-for="error, index in errors" :key="index">{{ error }}</span>
    </div>

    <div class="alert alert-success" role="alert" v-if="success.length">
      <span v-for="msg, index in success" :key="index">{{ msg }}</span>
    </div>

    <button @click="handleClick" class="btn btn-lg btn-dark">Transferir</button>
  </div>
  <!-- Modal -->
  <div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="staticBackdropLabel">Confirmação de transferencia</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          Tem certeza que deseja transferir <strong>{{ amountCurrency }}</strong> para a conta <strong>{{ transferInfo.username_to }}</strong> ?
        </div>
        <div class="modal-footer">
          <button ref="btnFechar" type="button" class="btn btn-outline-secondary" data-bs-dismiss="modal">Cancelar</button>
          <button @click="handleConfirmClick($refs.btnFechar)" type="button" class="btn btn-dark">Fazer transferencia</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { computed, ref } from 'vue';
import { usePageStore } from '../stores/page';

const errors = ref('')
const success = ref('')
const password = ref('')
const pageStore = usePageStore()
const transferInfo = ref({
  username_to: '',
  amount: ''
})

const amountCurrency = computed(() => {
  errors.value = ''
  if (!transferInfo.value.amount) {
    return parseFloat(0).toLocaleString('pt-br',{style: 'currency', currency: 'BRL'})
  }
  return parseFloat(transferInfo.value.amount).toLocaleString('pt-br',{style: 'currency', currency: 'BRL'})
})

async function handleClick() {
  errors.value = ''
  if (!transferInfo.value.amount) {
    errors.value = 'Digite algum valor antes de continuar'
  }
  if (transferInfo.value.amount < 0) {
    errors.value = 'Digite um valor positivo'
  } 
  if (!password.value.length) {
    errors.value = 'Digite sua senha'
  } else {
    await pageStore.verifyPassword(password.value)
    if (!pageStore.passwordIsValid) {
      errors.value = 'Senha incorreta'
    }
  }
  if (transferInfo.value.username_to === '') {
    errors.value = 'Digite o usuario da conta destinatária'
  }
  if ( pageStore.user.balance < transferInfo.value.amount ) {
    errors.value = 'Saldo insuficiente'
  }
  if (!errors.value.length) {
    $('#staticBackdrop').modal('show')
  }
}

function handleConfirmClick(refs) {
  axios.post('/api/v1/transfer/', transferInfo.value)
    .then((res) => {
      if (res.data.status === 200) {
        pageStore.user.balance = parseFloat(res.data.accountBalance)
        success.value = res.data.response
        clearForm()
        setTimeout(() => {
          success.value = ''
        }, 2500)
      } else {
        errors.value = res.data.response
      }
    })
    .catch((error) => {
      console.log(error)
    })
  
  refs.click()
}

function clearForm() {
  transferInfo.value.amount = ''
  transferInfo.value.username_to = ''
  password.value = ''
}

</script>

<style scoped>
.text {
  font-weight: bold;
  font-size: 14pt;
}
</style>