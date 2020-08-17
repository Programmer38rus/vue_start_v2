<template>
  <div>
    <div>
      <b-alert ref="hider" variant="success"
        show
        dismissible
      >{{ message }}
        <b-button
          type="hider"
          class="close"
          data-dismiss="alert"
          aria-label="Close"
        >
          <b
            aria-hidden="true"
          >
            &times;
          </b>
        </b-button>
      </b-alert>
    </div>
  </div>
</template>

<script>
// import Todos from './Todos.vue';
export default {
  name: 'Confirmation',
  props: ['message'],
  methods: {
  },
};
</script>
