export default {
  path: "/production",
  component: () => import("@/layouts/BaseLayout"),
  redirect: "/",
  children: [
    {
      path: "plan",
      component: () => import("@/views/production/plan"),
    },
    {
      path: "detial",
      component: () => import("@/views/production/detial"),
    },
    {
      path: "picking_order",
      component: () => import("@/views/production/pickingOrder"),
    },
    {
      path: "task",
      component: () => import("@/views/production/task"),
    },
    {
      path: "record",
      component: () => import("@/views/production/record"),
    },
  ],
};
