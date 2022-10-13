<template>
  <nav class="navbar navbar-expand-md navbar-dark bg-dark">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Logo</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarCollapse">
        <ul class="navbar-nav me-auto mb-2 mb-md-0">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Início</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Extrato</a>
          </li>
        </ul>
        <form class="d-flex">
          <p class="text-white-50 p-2 mb-0">Olá, Usuário</p>
          <p class="text-white-50 p-2 mb-0">Saldo: R$ 0,00</p>
          <button class="btn btn-outline-light" type="submit">Sair</button>
        </form>
      </div>
    </div>
  </nav>
</template>

<script setup>

</script>