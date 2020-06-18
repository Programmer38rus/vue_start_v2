<template>
  <div  class="container">
    <h1>Todos</h1>
    <div class="alert alert-success alert-dismissible fade show" role="Close">
      Бутстрап подключен и работает
      <button type="button" class="close" data-dismiss="alert" aria-label="Close">
        <span aria-hidden="true">&times;</span>
      </button>
    </div>
    <table>
      <thead>
      <tr>
        <th>Uid</th>
        <th>Описание</th>
        <th>Выполнена?</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="(todo, index) in todos" :key="index">
        <td>{{ todo.uid }}</td>
        <td>{{ todo.description}}</td>
        <td>
          <span v-if="todo.is_completed">Выполнено</span>
          <span v-else>Невыполнено</span>
        </td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';

const dataURL = 'http://localhost:5000/api/tasks';

export default {
  name: 'Fetch',
  data() {
    return {
      todos: [],
    };
  },
  // created() {
  //   axios.get(dataURL)
  //     .then((response) => {
  //       this.msg = response.data.message;
  //       console.log(this);
  //     });
  // },
  methods: {
    getMessage() {
      console.log('функция запустилась');
      axios.get(dataURL)
        .then((response) => {
          // this.msg = response.data.message;
          this.todos = response.data.tasks;
          console.table(this.todos);
        });
    },
  },
  // тест
  created() {
    this.getMessage();
  },
};
</script>
