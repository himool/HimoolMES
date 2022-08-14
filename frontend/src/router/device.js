export default {
  path: "/device",
  component: () => import("@/layouts/BaseLayout"),
  redirect: "/",
  children: [
    {
      path: "info",
      component: () => import("@/views/device/info"),
    },
    {
      path: "spare_part",
      component: () => import("@/views/device/sparePart"),
    },
    {
      path: "patrol_inspection",
      component: () => import("@/views/device/patrolInspection"),
    },
    // {
    //   path: "patrol_inspection_record",
    //   component: () => import("@/views/device/patrolInspectionRecord"),
    // },
    {
      path: "repair",
      component: () => import("@/views/device/repair"),
    },
    // {
    //   path: "repair_record",
    //   component: () => import("@/views/device/repairRecord"),
    // },
    {
      path: "maintenance",
      component: () => import("@/views/device/maintenance"),
    },
    // {
    //   path: "maintenance_record",
    //   component: () => import("@/views/device/maintenanceRecord"),
    // },
    {
      path: "status",
      component: () => import("@/views/device/status"),
    },
  ],
};
