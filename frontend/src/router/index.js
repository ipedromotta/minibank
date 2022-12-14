import { createRouter, createWebHistory } from 'vue-router'
import { usePageStore } from '../stores/page'
import HomeView from '@/views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'
import SignUpView from '@/views/SignUpView.vue'
import BankStatementView from '@/views/BankStatementView.vue'
import MyAccountView from '@/views/MyAccountView.vue'
import ForgotPasswordView from '@/views/ForgotPasswordView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      alias: '/inicio',
      name: 'home',
      component: HomeView,
      meta: {
        requireLogin: true
      }
    },
    {
      path: '/extrato',
      name: 'extrato',
      component: BankStatementView,
      meta: {
        requireLogin: true
      }
    },
    {
      path: '/minha-conta',
      name: 'minha-conta',
      component: MyAccountView,
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
      path: '/esqueceu-senha',
      name: 'esqueceu-senha',
      component: ForgotPasswordView,
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
