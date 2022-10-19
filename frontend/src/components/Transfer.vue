<template>
  <div class="col-sm-6 mx-auto">
    <h2>Transferencia</h2>

    <div class="form-floating mb-3">
      <input v-model="accountNumber" @input="errors = ''" type="number" class="form-control" id="accountNumber" placeholder="0000">
      <label for="accountNumber">Número da conta destinatária</label>
    </div>
    <div class="form-floating">
      <input v-model="password" @input="errors = ''" type="password" class="form-control" id="floatingPassword" placeholder="senha">
      <label for="floatingPassword">Digite sua senha</label>
    </div>
    <div class="mb-3 mt-3">
      <input v-model="amount" type="number" class="form-control form-control-lg" id="amount" placeholder="R$ 0,00">
      <label for="amount" class="form-label mt-3 text">Valor da transferencia {{ amountCurrency }}</label>
    </div>

    <div class="alert alert-danger" role="alert" v-if="errors.length">
      <span v-for="error in errors" :key="error">{{ error }}</span>
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
          Tem certeza que deseja transferir <strong>{{ amountCurrency }}</strong> para a conta <strong>{{ accountNumber }}</strong> ?
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
import { computed, ref } from 'vue';

const amount = ref()
const errors = ref('')
const password = ref('')
const accountNumber = ref('')

const amountCurrency = computed(() => {
  errors.value = ''
  if (!amount.value) {
    return parseFloat(0).toLocaleString('pt-br',{style: 'currency', currency: 'BRL'})
  }
  return parseFloat(amount.value).toLocaleString('pt-br',{style: 'currency', currency: 'BRL'})
})

function handleClick() {
  errors.value = ''
  if (!amount.value) {
    errors.value = 'Digite algum valor antes de continuar'
  }
  if (!password.value.length) {
    errors.value = 'Digite sua senha'
  }
  if (accountNumber.value === '') {
    errors.value = 'Digite o número da conta destinatária'
  }
  if (!errors.value.length) {
    $('#staticBackdrop').modal('show')
  }
}

function handleConfirmClick(refs) {
  console.log('Confirmação')
  refs.click()
}
</script>

<style scoped>
.text {
  font-weight: bold;
  font-size: 14pt;
}
</style>