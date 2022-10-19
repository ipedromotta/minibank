<template>
  <div class="container text-center mt-5">
    <h1>
      Seja bem vindo!
    </h1>
    <h4 class="mt-5">
      Qual operação deseja fazer?
    </h4>
    <div class="col-sm-6 mx-auto mb-4">
      <select v-model="tipoOperacao" class="form-select form-select-lg" aria-label="Tipo de operacao">
        <option selected value="1">Deposito</option>
        <option value="2">Saque</option>
        <option value="3">Transferencia</option>
      </select>
    </div>
    
    <div class="row">
      <Deposit v-if="tipoOperacao === '1'" />
      <Withdraw v-else-if="tipoOperacao === '2'" />
      <Transfer v-else-if="tipoOperacao === '3'" />
    </div>

  </div>
</template>

<script setup>
import { ref } from 'vue';
import Deposit from '@/components/Deposit.vue';
import Withdraw from '@/components/Withdraw.vue';
import Transfer from '@/components/Transfer.vue';

const tipoOperacao = ref('1')

</script>
