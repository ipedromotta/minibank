<template>
  <div class="col-sm-6 mx-auto">
    <h2>Deposito</h2>

    <div class="mb-3 mt-3">
      <label for="amount" class="form-label">Valor do deposito {{ amountCurrency }}</label>
      <input v-model="amount" type="text" class="form-control" id="amount" placeholder="R$ 0,00">

    </div>

    <button @click="handleClick" class="btn btn-dark">Depositar</button>
  </div>
</template>

<script setup>
import { computed, ref } from 'vue';

const amount = ref()
const error = ref('')

const amountCurrency = computed(() => {
  if (!amount.value) {
    return parseFloat(0).toLocaleString('pt-br',{style: 'currency', currency: 'BRL'})
  }
  return parseFloat(amount.value).toLocaleString('pt-br',{style: 'currency', currency: 'BRL'})
})

function handleClick() {
  error.value = ''
  if (!amount.value) {
    error.value = 'Digite algum valor antes de continuar'
  }
  console.log(error.value)
}

</script>