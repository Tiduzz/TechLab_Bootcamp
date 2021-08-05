import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  // mode: 'hash',
  mode: 'history',
  base: process.env.BASE_URL,
  scrollBehavior: () => ({ y: 0 }),
  routes: [
    // Login
    {
      name: 'Login',
      path: '/login',
      component: () => import('@/views/Login'),
    },
    {
      path: '/',
      component: () => import('@/views/dashboard/Index'),
      children: [
        // Dashboard
        {
          name: 'Dashboard',
          path: '',
          component: () => import('@/views/dashboard/Dashboard'),
        },
        // Pages
        {
          name: 'Estatísticas',
          path: 'pages/estatisticas',
          component: () => import('@/views/dashboard/pages/Estatisticas'),
        },
        {
          name: 'User Profile',
          path: 'pages/user',
          component: () => import('@/views/dashboard/pages/UserProfile'),
        },
        {
          name: 'Gerenciar Salas',
          path: 'pages/gerenciar-salas',
          component: () => import('@/views/dashboard/pages/GerenciarSalas'),
        },
        {
          name: 'Gerenciar Câmeras',
          path: 'pages/gerenciar-cameras',
          component: () => import('@/views/dashboard/pages/GerenciarCameras'),
        },
        {
          name: 'Notifications',
          path: 'pages/notifications',
          component: () => import('@/views/dashboard/pages/Notifications'),
        },
      ],
    },
  ],
})
