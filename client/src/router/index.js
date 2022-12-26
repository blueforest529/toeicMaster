import Vue from 'vue'
import VueRouter from 'vue-router'
import Word from '../components/Word.vue';
import Idiom from '../components/Idiom.vue';
import Test from '../components/Test.vue';

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Word',
    component: Word,
  },
  {
    path: '/idiom',
    name: 'Idiom',
    component: Idiom,
  },
  {
    path: '/test',
    name: 'Test',
    component: Test,
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
