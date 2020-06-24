<template>
  <div>
    <div>
      <b-alert ref="hider" variant="success" show>{{ message }}
        <b-button type="hider" class="close" data-dismiss="alert"
          aria-label="Close"
          @click="hider(false)">
          <span aria-hidden="true">&times;</span>
        </b-button>
      </b-alert>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Confirmation',
  props: ['message'],
  methods: {
    hider(atr) {
      // console.log(this.$refs);
      this.$refs.hider.show = atr;
    },
  },
};
</script>
