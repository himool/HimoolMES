export default {
  path: "/system",
  component: () => import("@/layouts/BaseLayout"),
  redirect: "/",
  children: [
    {
      path: "role",
      component: () => import("@/views/system/role"),
    },
    {
      path: "user",
      component: () => import("@/views/system/user"),
    },
  ],
};
