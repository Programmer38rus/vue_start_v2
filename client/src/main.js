import Bootstrap from 'bootstrap/dist/css/bootstrap.css';
import BootstrapVue from 'bootstrap-vue/dist/bootstrap-vue';
import Vue from 'vue';
import App from './App.vue';
import router from './router';

Vue.use(BootstrapVue);
Vue.use(Bootstrap);

Vue.config.productionTip = false;

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
