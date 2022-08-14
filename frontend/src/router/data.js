export default {
  path: "/data",
  component: () => import("@/layouts/BaseLayout"),
  redirect: "/",
  children: [
    {
      path: "category",
      component: () => import("@/views/data/category"),
    },
    {
      path: "material",
      component: () => import("@/views/data/material"),
    },
    {
      path: "bom",
      component: () => import("@/views/data/bom"),
    },
    {
      path: "process_route",
      component: () => import("@/views/data/processRoute"),
    },
    {
      path: "process",
      component: () => import("@/views/data/process"),
    },
    {
      path: "station",
      component: () => import("@/views/data/station"),
    },
  ],
};
