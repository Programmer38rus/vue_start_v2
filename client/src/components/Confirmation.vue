<template>
  <div class="alert alert-success alert-dismissible fade show" role="alert">
    Бутстап подключен и работает
    <button type="button" class="close" data-dismiss="alert" aria-label="Close"
            @click="$on.hide('#alert')">
      <span aria-hidden="true">&times;</span>
    </button>
  </div>
</template>

<script>
export default {
  name: 'Confirmation',
};
</script>
