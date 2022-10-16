import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'
import SignUpView from '@/views/SignUpView.vue'
import { usePageStore } from '../stores/page'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
      meta: {
        requireLogin: true
      }
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
      meta: {
        isLogin: true
      }
    },
    {
      path: '/cadastro',
      name: 'cadastro',
      component: SignUpView,
      meta: {
        isLogin: true
      }
    }
  ]
})

router.beforeEach((to, from, next) => {
  const pageStore = usePageStore()

  if (to.matched.some(record => record.meta.requireLogin) && !pageStore.isAuthenticated) {
    next({ name: 'login', query: { to: to.path }})
  } else if (to.matched.some(record => record.meta.isLogin) && pageStore.isAuthenticated) {
    next({ name: 'home', query: { to: to.path }})
  } else {
    next()
  }
})

export default router
