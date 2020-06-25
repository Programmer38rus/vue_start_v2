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
          <b-form-checkbox-group v-model="updateTodoFrom.is_completed" id="from-update-checks">

          </b-form-checkbox-group>

        </b-form-group>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
    export default {
        name: "updateTodoModal"
    }
</script>

<style scoped>

</style>