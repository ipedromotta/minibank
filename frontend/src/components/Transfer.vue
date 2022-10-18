<template>
  <div class="col-sm-6 mx-auto">
    <h2>Transferencia</h2>

    <div class="mb-3 mt-3">
      <label for="amount" class="form-label">Valor</label>
      <input type="number" class="form-control" id="amount" placeholder="R$ 0,00">
    </div>
    <div class="mb-3 mt-3">
      <label for="accountNumber" class="form-label">Número da conta</label>
      <input type="number" class="form-control" id="accountNumber" placeholder="00.0000-00">
    </div>
    <div class="mb-3 mt-3">
      <label for="password" class="form-label">Senha</label>
      <input type="password" class="form-control" id="password" placeholder="Digite sua senha">
    </div>

    <button class="btn btn-dark">Transferir</button>
  </div>
</template>

<script setup>

</script>