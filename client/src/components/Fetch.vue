<template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
import axios from 'axios';

const dataURL = 'https://api.jsonbin.io/b/5e90e8278e85c84370140777';

export default {
  name: 'Fetch',
  data() {
    return {
      msg: 'Запрос еще не прошел.',
    };
  },
  // created() {
  //   axios.get(dataURL)
  //     .then((response) => {
  //       this.msg = response.data.message;
  //       console.log(this);
  //     });
  // },
  methods: {
    getMessage() {
      axios.get(dataURL)
        .then((response) => {
          this.msg = response.data.message;
          // console.log(this);
        });
    },
  },
  // тест
  created() {
    this.getMessage();
  },
};
</script>
