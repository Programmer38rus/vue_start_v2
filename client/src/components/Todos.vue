<template>
  <div class="container">
    <div class="col-sm-10">
      <h1>TASKS</h1>
      <confirmation></confirmation>
      <button type="button" id="task-add" class="btn btn-success btn-sm align-left d-block"
        v-b-modal.todo-modal>
        Добавить задачу
      </button>
      <table class="table table-dark table-table-stripped table-hover">

        <thead class="thead-light">
          <tr>
            <th>Uid</th>
            <th>Описание</th>
            <th>Выполнена?</th>
            <th></th>
          </tr>
        </thead>

        <tbody>
          <tr v-for="(todo, index) in todos" :key="index">
            <td class="todo-uid">{{ todo.uid }}</td>
            <td>{{ todo.description }} </td>
            <td>
              <span v-if="todo.is_completed">Выполнено</span>
              <span v-else>Не выполнена</span>
            </td>
            <td>
              <div class="btn-group" role="group">
                <button type="button" class="btn btn-secondary btn-sm">Обновить</button>
                &nbsp;
                <button type="button" class="btn btn-danger btn-sm">X</button>
              </div>
            </td>
          </tr>
        </tbody>

      </table>

    </div>
    <b-modal ref="addTodoModal"
      id="todo-modal"
      title="Добавить задачу"
      hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-description-group"
          label="Описание"
          label-for="form-description-input">
        <b-form-input id="form-description-input"
          type="text"
          v-model="addTodoForm.description"
          required
          placeholder="Завести задачу">
        </b-form-input>
        </b-form-group>
        <b-form-group id="form-complete-group">
          <b-form-checkbox-group v-model="addTodoForm.is_completed" id="form-checks">
            <b-form-checkbox value="true">Задача выполнена?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button type="submit" variant="primary">Добавить</b-button>
        <b-button type="reset" variant="danger">Сброс</b-button>
      </b-form>
    </b-modal>
    <div class="d-flex justify-content-center mt-5">
      <b-button variant="danger" id="testbtn">RELLYTi</b-button>
      <b-col lg="4"><b-button variant="success">RELLYTi</b-button></b-col>
      <b-textarea v-model="texts"></b-textarea>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Confirmation from './Confirmation.vue';

const todoListURL = 'http://localhost:5000/api/tasks';
const todoAddURL = 'http://localhost:5000/api/add-task/';
export default {
  name: 'Todo',
  data() {
    return {
      todos: [],
      addTodoForm: {
        description: '',
        is_completed: [],
      },
      texts: 'текст как есть',
    };
  },

  methods: {
    getTodos() {
      axios.get(todoListURL)
        .then((response) => {
          this.todos = response.data.tasks;
          console.table(this.todos);
        });
    },
    resetForm() {
      this.addTodoForm.description = '';
      this.addTodoForm.is_completed = [];
    },
    onSubmit(event) {
      event.preventDefault();
      this.$refs.addTodoModal.hide();

      // this.$refs.addTodoModal.toggle('#testbtn');
      const requestData = {
        description: this.addTodoForm.description,
        is_completed: this.addTodoForm.is_completed[0],
      };
      if (requestData.is_completed) {
        requestData.is_completed = true;
      } else {
        requestData.is_completed = false;
      }
      axios.post(todoAddURL, requestData)
        .then(() => {
          this.getTodos();
        });
      this.resetForm();
    },
    onReset(event) {
      event.preventDefault();
      this.$refs.addTodoModal.hide();
      this.resetForm();
    },
    // тестовая функция
    textViewer() {
      console.log('Работает функция');
    },
  },
  components: {
    confirmation: Confirmation,
  },
  created() {
    this.getTodos();
  },
};
</script>

<style>
button#task-add{
  margin-top: 20px;
  margin-bottom: 20px;
}
h2, td {
  text-align: left;
}
  .todo-uid {
    text-align: right;
  }
</style>
