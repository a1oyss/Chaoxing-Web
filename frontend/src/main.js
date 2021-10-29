import Vue from 'vue'
import './plugins/axios'
import App from './App.vue'
import './plugins/element.js'
import router from './router'
import store from './store'

Vue.config.productionTip = false
router.beforeEach((to, from, next) => {
  if (to.meta.requireAuth) {
    if (store.state.user.username) {
      next()
    } else {
      next({
        path: 'login',
        query: { redirect: to.fullPath }
      })
    }
  } else {
    next()
  }
})

new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
})