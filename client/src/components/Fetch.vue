<template>
  <div>
    <h1>Todos</h1>
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
