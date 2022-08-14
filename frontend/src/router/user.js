export default {
  path: '/user',
  redirect: "/user/login",
  component: () => import('@/layouts/UserLayout'),
  children: [
    {
      path: 'login',
      component: () => import('@/views/login'),
    },
    {
      path: 'set_password',
      component: () => import('@/views/setPassword'),
    },
  ],
}