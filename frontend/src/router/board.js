export default {
  path: "/board",
  component: () => import("@/layouts/BaseLayout"),
  redirect: "/",
  children: [
    {
      path: "production",
      component: () => import("@/views/board/production"),
    },
    {
      path: "quality_inspection",
      component: () => import("@/views/board/qualityInspection"),
    },
    {
      path: "device",
      component: () => import("@/views/board/device"),
    },
  ],
};
