<template>
  <div class="col-sm-6 mx-auto">
    <h2>Saque</h2>

    <div class="form-floating">
      <input v-model="password" @input="errors = ''" type="password" class="form-control" id="floatingPassword" placeholder="senha">
      <label for="floatingPassword">Digite sua senha</label>
    </div>
    <div class="mb-3 mt-3">
      <input v-model="amount" type="number" class="form-control form-control-lg" id="amount" placeholder="R$ 0,00">
      <label for="amount" class="form-label mt-3 text">Valor do saque {{ amountCurrency }}</label>
    </div>

    <div class="alert alert-danger" role="alert" v-if="errors.length">
      <span v-for="error in errors" :key="error">{{ error }}</span>
    </div>

    <button @click="handleClick" class="btn btn-lg btn-dark">Sacar</button>
  </div>
</template>

<script setup>
import { computed, ref } from 'vue';

const amount = ref()
const errors = ref('')
const password = ref('')

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
}
</script>

<style scoped>
.text {
  font-weight: bold;
  font-size: 14pt;
}
</style>
