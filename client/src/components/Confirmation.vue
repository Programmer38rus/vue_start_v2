<template>
  <div>
    <div>
      <b-alert ref="hider" variant="success"
        show
        dismissible
        fade
      >{{ message }}
          <b>
          </b>
      </b-alert>
    </div>
  </div>
</template>

<script>
// import Todos from './Todos.vue';
export default {
  name: 'Confirmation',
  props: ['message'],
  data() {
    return {
      dismissSecs: 5,
      dismissCountDown: 0,
      showDismissibleAlert: false
    };
  },
  methods: {

  },
};
</script>
