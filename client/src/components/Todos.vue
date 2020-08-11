<template>
  <div class="container">
    <div class="col-sm-10">
      <h1>TASKS</h1>
      <confirmation
              :message='confirmationMessage'
              v-if='showConfirmation'>
      </confirmation>
      <button type="button" v-on:click="addTodoModal()"
              id="task-add" class="btn btn-success btn-sm align-left d-block"
        v-b-modal.merge-todo-modal>
        Добавить задачу
      </button>
      <table class="table table-dark table-table-stripped table-hover">

        <thead class="thead-light">
          <tr>
            <th>Uid</th>
            <th>Описание</th>
            <th>Выполнено?</th>
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
<!--                -->
<!--                -->
                <button type="button" @click="updateTodo(todo)" v-b-modal.merge-todo-modal
                        class="btn btn-secondary btn-sm">Обновить</button>
                &nbsp;
<!--                -->
                <b-button id="del" class="btn btn-danger btn-sm"
                          @click="onDeleted(todo)">X</b-button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

<!--    Модальное окно добавления задач-->
<!--    <b-modal ref="addTodoModal"-->
<!--      id="todo-modal"-->
<!--      title="Добавить задачу"-->
<!--      hide-footer>-->
<!--      <b-form @submit="onSubmit" @reset="onReset" class="w-100">-->
<!--        <b-form-group id="form-description-group"-->
<!--          label="Описание"-->
<!--          label-for="form-description-input">-->
<!--        <b-form-input id="form-description-input"-->
<!--          type="text"-->
<!--          v-model="addTodoForm.description"-->
<!--          required-->
<!--          placeholder="Завести задачу">-->
<!--        </b-form-input>-->
<!--        </b-form-group>-->
<!--        <b-form-group id="form-complete-group">-->
<!--          <b-form-checkbox-group v-model="addTodoForm.is_completed" id="form-checks">-->
<!--            <b-form-checkbox value="true">Задача выполнена?</b-form-checkbox>-->
<!--          </b-form-checkbox-group>-->
<!--        </b-form-group>-->
<!--        <b-button type="submit" variant="primary">Добавить</b-button>-->
<!--        <b-button type="reset" variant="danger">Сброс</b-button>-->
<!--      </b-form>-->
<!--    </b-modal>-->

<!--&lt;!&ndash;        Модальное окно изменения задач&ndash;&gt;-->
<!--    <b-modal ref="updateTodoModal"-->
<!--             id="todo-update-modal"-->
<!--             title="Update"-->
<!--             hide-footer>-->
<!--      <b-form @submit="onUpdateSubmit" @reset="onUpdateReset" class="w-100">-->
<!--        <b-form-group id="from-update-description-group"-->
<!--                      label="Описание"-->
<!--                      label-for="form-update-description-input">-->
<!--          <b-form-input id="form-update-description-input"-->
<!--                        type="text"-->
<!--                        v-model="updateTodoForm.description"-->
<!--                        required>-->
<!--          </b-form-input>-->
<!--        </b-form-group>-->
<!--        <b-form-group id="form-update-complete-group">-->
<!--          <b-form-checkbox-group v-model="updateTodoForm.is_completed"
              id="from-update-checks">-->
<!--            <b-form-checkbox value="true">Task is completed</b-form-checkbox>-->
<!--          </b-form-checkbox-group>-->
<!--        </b-form-group>-->
<!--        <b-button-group>-->
<!--          <b-button type="submit" variant="primary">Submit</b-button>-->
<!--          <b-button type="reset" variant="danger">Reset</b-button>-->
<!--        </b-button-group>-->
<!--      </b-form>-->
<!--    </b-modal>-->

<!--    Экспериментальная часть-->
    <div class="d-flex justify-content-center mt-5">
      <b-button variant="danger" id="testbtn" type="hider">RELLYTi</b-button>
      <b-col lg="4"><b-button variant="success" type="hider">RELLYTi</b-button></b-col>
      <b-textarea v-for="(todo, index) in todos"
                  :key="index"
                  v-model="todo.description"></b-textarea>
    </div>
    <div>
      <b-button id="buttoncolum"
                variant="outline-primary"
                  v-for="(todo, index) in todos"
                  :key="index"
                  v-model="todo.description"
                  @click="viewTodo(todo)">{{todo.uid}}</b-button>
    </div>

<!--    Merge modal window-->
    <b-modal ref="mergeModal"
             id="merge-todo-modal"
             :title="modal.title"
             hide-footer>
      <b-form :@submit="onSubmit" :@reset="onReset" class="w-100">
        <b-form-group id="form-description-group"
                      label="Описание"
                      label-for="form-description-input">
          <b-form-input id="form-description-input"
                        type="text"
                        v-model="modal.formInput.description"
                        required>
<!--                        placeholder="Завести задачу">-->

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
    <modal
      :show=shower></modal>
  </div>
</template>

<script>
import axios from 'axios';
import Confirmation from './Confirmation.vue';
import Modal from './Modal.vue';

const dataURL = 'http://localhost:5000/api/tasks/';
// const todoListURL = 'http://localhost:5000/api/tasks/';
const todoAddURL = 'http://localhost:5000/api/add-task/';
// const todoDeleted = 'http://localhost:5000/api/tasks/3';

export default {
  name: 'Todo',
  data() {
    return {
      todos: [],
      addTodoForm: {
        description: '',
        is_completed: [],
      },
      // updateTodoForm: {
      //   uid: 0,
      //   description: '',
      //   is_completed: [],
      // },
      confirmationMessage: '',
      showConfirmation: false,
      texts: 'текст как есть',
      shower: 1,
      modal: {
        title: '',
        formInput: {},
        func1: '',
        func2: '',
      },
    };
  },

  methods: {
    getTodos() {
      axios.get(dataURL)
        .then((response) => {
          this.todos = response.data.tasks;
          console.table(this.todos);
        });
    },
    resetForm() {
      this.addTodoForm.description = '';
      this.addTodoForm.is_completed = [];
      this.updateTodoForm.description = '';
      this.updateTodoForm.is_completed = [];
    },
    onSubmit(event) {
      event.preventDefault();
      this.$refs.addTodoModal.hide();
      console.log(this.$refs);
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
          this.confirmationMessage = `Задача "${requestData.description}" добавлена`;
          this.showConfirmation = true;
          // Confirmation.methods.hider(true);
          // console.log(this);
        });
      this.resetForm();
    },
    onReset(event) {
      event.preventDefault();
      this.$refs.addTodoModal.hide();
      this.resetForm();
    },
    updateTodo(todo) {
      // this.updateTodoForm = todo;
      this.modal.title = 'Изменить задачу';
      this.modal.formInput = todo;
      // this.modal.formInput =
      //   update: this.updateTodoForm.description,
      // };
    },
    onUpdateSubmit(event) {
      event.preventDefault();
      // this.$refs.updateTodoModal.hide();
      this.$refs.mergeModal.hide();
      const requestData = {
        description: this.modal.formInput.description,
        is_completed: this.modal.formInput.is_completed[0],
      };
      const todoURL = dataURL + this.modal.formInput.uid;
      axios.put(todoURL, requestData)
        .then(() => {
          // console.log(todoURL);
          this.getTodos();
          this.confirmationMessage = 'Задача обновлена';
          this.showConfirmation = true;
        });
    },
    onUpdateReset(event) {
      event.preventDefault();
      this.resetForm();
      this.confirmationMessage = 'Задача обновлена';
      this.showConfirmation = true;
    },
    onDeleted(todo) {
      const todoURL = dataURL + todo.uid;
      axios.delete(todoURL)
        .then(() => {
          this.getTodos();
          this.confirmationMessage = 'Задача удалена';
          this.showConfirmation = true;
        });
    },
    addTodoModal() {
      this.modal.title = 'Добавить задачу';
      this.modal.formInput = 'addTodoModal.description';
    },
    // Экспериментальная часть
    viewTodo(todo) {
      console.log(todo);
    },
  },
  components: {
    confirmation: Confirmation,
    modal: Modal,
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

/*эксперементальная часть*/
#buttoncolum {
  display: block;
  /*flex-direction: column;*/
  width: 100px;
  margin-top: 1rem;
  /*justify-content: right;*/
}
</style>
