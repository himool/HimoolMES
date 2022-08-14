export default {
  path: "/quality",
  component: () => import("@/layouts/BaseLayout"),
  redirect: "/",
  children: [
    {
      path: "quality_inspection_task",
      component: () => import("@/views/quality/qualityInspectionTask"),
    },
    {
      path: "quality_inspection_record",
      component: () => import("@/views/quality/qualityInspectionRecord"),
    },
  ],
};
