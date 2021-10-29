import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: window.sessionStorage.getItem('user' || '[]') == null ? '' : JSON.parse(window.sessionStorage.getItem('user' || '[]')),
    resultShow:false
  },
  mutations: {
    login(state, user) {
      state.user = user
      window.sessionStorage.setItem('user', JSON.stringify(user))
    },
    show(state) {
      state.resultShow = true
    },
    hide(state) {
      state.resultShow=false
    }
  }
})
