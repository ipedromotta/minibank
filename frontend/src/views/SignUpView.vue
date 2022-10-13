<template>
  <div class="text-center body">
    <main class="form-signin">
      <form class="space-between">
        <img class="mb-4" src="/docs/5.0/assets/brand/bootstrap-logo.svg" alt="" width="72" height="57">
        <h1 class="h3 mb-3 fw-normal">Cadastre-se</h1>

        <div class="form-floating mb-2">
          <input type="text" maxlength="15" class="form-control" id="floatingInput" placeholder="seu-usuario">
          <label for="floatingInput">Nome</label>
        </div>

        <div class="form-floating mb-2">
          <input type="email" maxlength="15" class="form-control" id="floatingInput" placeholder="seu-usuario">
          <label for="floatingInput">Email</label>
        </div>

        <div class="form-floating mb-2">
          <input type="text" maxlength="15" class="form-control" id="floatingInput" placeholder="seu-usuario">
          <label for="floatingInput">Usuário</label>
        </div>

        <div class="form-floating mb-2">
          <input type="password" class="form-control" id="floatingPassword" placeholder="Password">
          <label for="floatingPassword">Senha</label>
        </div>

        <div class="form-floating">
          <input type="password" class="form-control" id="floatingPassword2" placeholder="senha">
          <label for="floatingPassword2">Confirme sua senha</label>
        </div>

        <button class="w-100 btn btn-lg btn-dark mt-5" type="submit">Cadastrar</button>
        
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

/* .form-signin .form-floating:focus-within {
  z-index: 2;
}

.form-signin input[type="text"] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}

.form-signin input[type="password"] {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
} */

.link {
  text-decoration: none;
}
.link:hover{
  cursor: pointer;
  color: #aaaaaa!important;
  transition: ease-in 0.2s;
}
</style>