<template>
  <div class="container">
    <div>
      <h1>TASKS</h1>
      <transition
        name="slide-fade"
      >
        <confirmation
                :message='confirmationMessage'
                v-if='showConfirmation'>
        </confirmation>
      </transition>
      <div class="container row row-cols-2 align-items-center">
        <button type="button" v-on:click="addTodoConfigureModal()"
                id="task-add" class="btn btn-success btn-sm align-left d-block"
          v-b-modal.merge-todo-modal>
          Добавить задачу
        </button>
        <div class="ml-md-3">
          <span class="font-weight-bold">Всего задачь: </span>{{tasksCount.all}} |
          <span class="font-weight-bold">Выполненых: </span>{{tasksCount.complete}} |
          <span class="font-weight-bold">Невыполненых: </span>{{tasksCount.noComplete}}
        </div>
      </div>

      <table class="table table-dark table-table-stripped table-hover">

        <thead class="thead-light">
          <tr>
            <th>Uid</th>
            <th>Описание</th>
            <th>Выполнено?</th>
            <th></th>
          </tr>
        </thead>

        <tbody class="">
          <tr v-for="(todo, index) in todos" :key="index">
            <td class="todo-uid">{{ index + 1 }}</td>
            <td>{{ todo.description }} </td>
            <td>
              <span v-if="todo.is_completed">Выполнено</span>
              <span v-else>Не выполнена</span>
            </td>
            <td>
              <div class="btn-group" role="group">
<!--                -->
<!--                -->
                <button type="button" @click="updateTodoConfigureModal(todo)"
                        v-b-modal.merge-todo-modal
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

<!--    Merge modal window-->
   <b-modal ref="mergeModal"
             id="merge-todo-modal"
             :title="modal.message"
             hide-footer>
      <b-form  class="w-100">
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
          <b-form-checkbox-group v-model="modal.formInput.is_completed" id="form-checks">
            <b-form-checkbox value="true">Задача выполнена?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
          <b-button @click="modal.func1" variant="primary">{{this.modal.btnName}}</b-button>
          <b-button @click="modal.func2" variant="danger">Сброс</b-button>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Confirmation from './Confirmation.vue';

const dataURL = 'http://localhost:5000/api/tasks/';
// const todoListURL = 'http://localhost:5000/api/tasks/';
const todoAddURL = 'http://localhost:5000/api/add-task/';
// const todoDeleted = 'http://localhost:5000/api/tasks/3';

export default {
  name: 'Todo',
  data() {
    return {
      todos: [],
      // addTodoForm: {
      //   description: '',
      //   is_completed: [],
      // },
      // updateTodoForm: {
      //   uid: 0,
      //   description: '',
      //   is_completed: [],
      // },
      shower: 1,
      confirmationMessage: '',
      showConfirmation: false,
      modal: {
        message: '',
        formInput: {
          description: '',
          is_completed: '',
          uid: '',
        },
        func1: '',
        func2: '',
        btnName: '',
      },
      tasksCount: {
        all: null,
        complete: null,
        noComplete: null,
      },
    };
  },

  methods: {
    getTodos() {
      axios.get(dataURL)
        .then((response) => {
          this.todos = response.data.tasks;
          console.table(this.todos);
          localStorage.setItem('todos', JSON.stringify(this.todos));
          this.counterTodos();
        })
        .catch(() => {
          this.confirmationMessage = 'Сервер не доступен...';
          this.showConfirmation = 'true';
          this.getTodos();
        });
    },
    resetForm() {
      this.modal.formInput.description = '';
      this.modal.formInput.is_completed = '';
    },
    onSubmit(event) {
      event.preventDefault();
      this.$refs.mergeModal.hide();
      const requestData = {
        description: this.modal.formInput.description,
        is_completed: Boolean(this.modal.formInput.is_completed[0]),
      };
      axios.post(todoAddURL, requestData)
        .then(() => {
          this.getTodos();
          this.confirmationMessage = `Задача "${requestData.description}" добавлена`;
          this.showConfirmation = true;
        })
        .catch((error) => {
          alert(error);
        });
      this.resetForm();
    },
    onReset(event) {
      event.preventDefault();
      this.$refs.mergeModal.hide();
      this.resetForm();
    },
    addTodoConfigureModal() {
      this.modal.message = 'Добавить задачу';
      this.modal.func1 = this.onSubmit;
      this.modal.func2 = this.onReset;
      this.modal.btnName = 'Добавить';
    },
    updateTodoConfigureModal(todo) {
      this.modal.message = 'Изменить задачу';
      this.modal.formInput = todo;
      this.modal.func1 = this.onUpdateSubmit;
      this.modal.func2 = this.onUpdateReset;
      this.modal.btnName = 'Изменить';
    },
    onUpdateSubmit(event) {
      event.preventDefault();
      this.$refs.mergeModal.hide();
      const requestData = {
        description: this.modal.formInput.description,
        is_completed: Boolean(this.modal.formInput.is_completed[0]),
      };
      const todoURL = dataURL + this.modal.formInput.uid;
      console.log(requestData);
      axios.put(todoURL, requestData)
        .then(() => {
          this.getTodos();
          this.confirmationMessage = 'Задача обновлена';
          this.showConfirmation = true;
        });
      this.resetForm();
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
          this.resetForm();
          this.getTodos();
          this.confirmationMessage = 'Задача удалена';
          this.showConfirmation = true;
        });
    },
    counterTodos() {
      localStorage.setItem('todos', JSON.stringify(this.todos));
      const json = JSON.parse(localStorage.getItem('todos'));
      this.tasksCount.all = json.length;
      const complete = json.filter((item) => item.is_completed === true);
      this.tasksCount.complete = complete.length;
      this.tasksCount.noComplete = this.tasksCount.all - this.tasksCount.complete;
    },
    // Экспериментальная часть
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

/*эксперементальная часть*/
#buttoncolum {
  display: block;
  /*flex-direction: column;*/
  width: 100px;
  margin-top: 1rem;
  /*justify-content: right;*/
}
.slide-fade-enter-active {
  /*transition: all .3s ease;*/
  transition: all .8s cubic-bezier(1.0, 0.5, 0.8, 1.0);
}
.slide-fade-leave-active {
  transition: all .8s cubic-bezier(1.0, 0.5, 0.8, 1.0);
}
.slide-fade-enter, .slide-fade-leave-to
  /* .slide-fade-leave-active below version 2.1.8 */ {
  transform: translateX(10px);
  opacity: 0;
}
</style>
