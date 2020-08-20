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
export default {
  name: 'Confirmation',
  props: ['message'],
};
</script>
