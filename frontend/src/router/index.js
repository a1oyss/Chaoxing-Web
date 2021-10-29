import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../components/Login.vue'
import Index from '../components/Index.vue'

Vue.use(VueRouter)

const routes = [
  {
    path:'/',
    redirect:'/index'
  },
  {
    path:'/login',
    name:'Login',
    component: Login 
  },
  {
    path:'/index',
    name:'Index',
    component:Index,
    meta:{
      requireAuth:true
    }
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
