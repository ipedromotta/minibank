<template>
  <div class="container mt-3">
    <h1 class="text-center">Extrato</h1>
      <label for="startDate">
        <input id="startDate" :class="`form-control ${!currentToSearch.date.length? 'border border-danger': ''}`" type="date" v-model="currentToSearch.date" />
      </label>
      <button @click="search" :class="`btn btn-secondary mx-2 mb-1 ${!currentToSearch.date.length? 'disabled': ''}`">Consultar</button>
    <table class="table table-striped table-hover table-dark mt-3" v-if="info.length">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">Valor</th>
          <th scope="col">Tipo de transação</th>
          <th scope="col">Data/Hora</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item, index in info" :key="index">
          <th scope="row">{{ index+1 }}</th>
          <td>{{ item.amount }}</td>
          <td>{{ item.type }}</td>
          <td>{{ item.created_at }}</td>
        </tr>
      </tbody>
    </table>
    <h3 class="text-center mt-3" v-else>Sem registro de transações</h3>
  </div>
</template>

<script setup>
import axios from 'axios';
import { onMounted, ref } from 'vue';


const info = ref([])
const currentToSearch = ref({
  date: ''
})

async function update() {
  await axios.post('/api/v1/transactions/', currentToSearch.value)
    .then((res) => {
      info.value = res.data
    })
    .catch((error) => {
      console.log(error.response.data)
    })
  format()
}

function format() {
  for (let item = 0; item < info.value.length; item++) {
    info.value[item].amount = parseFloat(info.value[item].amount).toLocaleString('pt-br',{style: 'currency', currency: 'BRL'})
    info.value[item].type = translateType(info.value[item].type)
    info.value[item].created_at = formatDate(info.value[item].created_at)
  }
}

function formatDate(date) { 
  const dateToFormat = new Date(date)

  var dateFormat = `${to2Decimal(dateToFormat.getDate())}/${to2Decimal(dateToFormat.getMonth()+1)}/${to2Decimal(dateToFormat.getFullYear())} ${to2Decimal(dateToFormat.getHours())}:${to2Decimal(dateToFormat.getMinutes())}:${to2Decimal(dateToFormat.getSeconds())}`

  return dateFormat
}

function to2Decimal(value) {
  if (value < 10 ) {
    return `0${value}`
  }
  return value
}

function translateType(type) {
  if (type === 'withdraw') {
    return 'Saque'
  } else if (type === 'deposit') {
    return 'Depósito'
  } else if (type === 'transfer') {
    return 'Transferencia'
  } else {
    return 'Desconhecida'
  }
}

function getToday() {
  let date = new Date()
  currentToSearch.value.date = `${to2Decimal(date.getFullYear())}-${to2Decimal(date.getMonth() + 1)}-${to2Decimal(date.getDate())}` 
}

function search() {
  if (!currentToSearch.value.date.length) {
    return
  }
  update()
}

onMounted(() => {
  getToday()
  search()
})

</script>
