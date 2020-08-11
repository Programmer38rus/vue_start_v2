<template>
  <div>
    <template v-if="show == 1">
      <h1>Это компонентик!</h1>
      <h1>{{show}}</h1>
    </template>
  </div>
</template>

<script>
export default {
  name: 'Modal',
  props: ['show'],
};
</script>
