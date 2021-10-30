// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from "./store";
import titleMixin from './mixins/titleMixin'
Vue.config.productionTip = false

import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'


import Vuex from 'vuex'
Vue.use(Vuex)


Vue.use(VueMaterial)

Vue.mixin(titleMixin)

new Vue({
  store,
  el: '#app',
  components: { App },
  template: '<App/>',
  router
})
