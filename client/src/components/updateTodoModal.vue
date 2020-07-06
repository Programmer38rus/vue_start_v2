<template>
  <div>
    <b-modal ref="updateTodoModal"
      id="todo-update-modal"
      title="Update"
      hide-footer>
      <b-form @submit="onUpdateSubmit" @reset="onUpdateReset" class="w-100">
        <b-form-group id="from-update-description-group"
          label="Описание"
          label-for="form-update-description-input">
          <b-form-input id="form-update-description-input"
            type="text"
            v-model="updateTodoForm.description"
            required>
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-update-complete-group">
          <b-form-checkbox-group v-model="updateTodoForm.is_completed" id="from-update-checks">
            <b-form-checkbox value="true">Task is completed</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
export default {
  name: 'updateTodoModal',
  data() {
    return {
      updateTodoForm: {
        uid: 0,
        description: '',
        is_completed: [],
      },
    };
  },
};
</script>
