<template>
  <div class="col-sm-6 mx-auto">
    <h2>Saque</h2>

    <div class="form-floating">
      <input v-model="password" @input="errors = ''" type="password" class="form-control" id="floatingPassword" placeholder="senha">
      <label for="floatingPassword">Digite sua senha</label>
    </div>
    <div class="mb-3 mt-3">
      <input v-model="amount.amount" type="number" class="form-control form-control-lg" id="amount" placeholder="R$ 0,00" min="0">
      <label for="amount" class="form-label mt-3 text">Valor do saque {{ amountCurrency }}</label>
    </div>

    <div class="alert alert-danger" role="alert" v-if="errors.length">
      <span v-for="error, index in errors" :key="index">{{ error }}</span>
    </div>

    <div class="alert alert-success" role="alert" v-if="success.length">
      <span v-for="msg, index in success" :key="index">{{ msg }}</span>
    </div>

    <button @click="handleClick" class="btn btn-lg btn-dark">Sacar</button>
  </div>
  <!-- Modal -->
  <div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="staticBackdropLabel">Confirmação de saque</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          Tem certeza que deseja sacar <strong>{{ amountCurrency }}</strong> ?
        </div>
        <div class="modal-footer">
          <button ref="btnFechar" type="button" class="btn btn-outline-secondary" data-bs-dismiss="modal">Cancelar</button>
          <button @click="handleConfirmClick($refs.btnFechar)" type="button" class="btn btn-dark">Fazer saque</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { computed, ref } from 'vue';
import { usePageStore } from '../stores/page';

const amount = ref({
  amount: ''
})
const errors = ref('')
const success = ref('')
const password = ref('')
const pageStore = usePageStore()

const amountCurrency = computed(() => {
  errors.value = ''
  if (!amount.value.amount) {
    return parseFloat(0).toLocaleString('pt-br',{style: 'currency', currency: 'BRL'})
  }
  return parseFloat(amount.value.amount).toLocaleString('pt-br',{style: 'currency', currency: 'BRL'})
})

async function handleClick() {
  errors.value = ''
  if (!amount.value.amount) {
    errors.value = 'Digite algum valor antes de continuar'
  }
  if (!password.value.length) {
    errors.value = 'Digite sua senha'
  } else {
    await pageStore.verifyPassword(password.value)

    if (!pageStore.passwordIsValid) {
      errors.value = 'Senha incorreta'
    }
  }
  if ( pageStore.user.balance < amount.value.amount ) {
    errors.value = 'Saldo insuficiente'
  }

  if (!errors.value.length) {
    $('#staticBackdrop').modal('show')
  }
}

function handleConfirmClick(refs) {
  axios.post('/api/v1/withdraw/', amount.value)
    .then((res) => {
      if (res.data.status === 200) {
        pageStore.user.balance = parseFloat(res.data.accountBalance).toFixed(2)
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

function clearForm() {
  amount.value.amount = ''
  password.value = ''
}
}
</script>

<style scoped>
.text {
  font-weight: bold;
  font-size: 14pt;
}
</style>
