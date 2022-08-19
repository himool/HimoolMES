export default {
  path: "/data",
  component: () => import("@/layouts/BaseLayout"),
  redirect: "/",
  children: [
    {
      path: "material_category",
      component: () => import("@/views/data/materialCategory"),
    },
    {
      path: "material",
      component: () => import("@/views/data/material"),
    },
    {
      path: "material_bill",
      component: () => import("@/views/data/materialBill"),
    },
    {
      path: "process_route",
      component: () => import("@/views/data/processRoute"),
    },
  ],
};
