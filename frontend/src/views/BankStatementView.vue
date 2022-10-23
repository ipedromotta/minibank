<template>
  <div class="container mt-3">
  <h1 class="text-center">Extrato</h1>
  <table class="table table-striped table-hover table-dark">
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
</div>
</template>

<script setup>
import axios from 'axios';
import { onMounted, ref } from 'vue';



const info = ref([])

async function update() {
  await axios.get('/api/v1/transactions/')
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

onMounted(() => {
  update()
})

</script>
