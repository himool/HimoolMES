export default [
  {
    key: "board",
    name: "看板管理",
    icon: "dashboard",
    submenus: [
      { key: "/board/production", name: "生产看板" },
      { key: "/board/quality_inspection", name: "质检看板" },
      { key: "/board/device", name: "设备看板" },
    ],
  },
  {
    key: "data",
    name: "基础数据",
    icon: "table",
    submenus: [
      { key: "/data/material_category", name: "物料分类" },
      { key: "/data/material", name: "物料管理" },
      { key: "/data/material_bill", name: "BOM管理" },
      { key: "/data/process", name: "工序管理" },
      { key: "/data/process_route", name: "工艺路线" },
    ],
  },
  {
    key: "production",
    name: "生产管理",
    icon: "schedule",
    submenus: [
      { key: "/production/plan", name: "生产计划" },
      { key: "/production/task", name: "生产任务" },
      { key: "/production/record", name: "报工记录" },
    ],
  },
  {
    key: "quality",
    name: "质量管理",
    icon: "safety-certificate",
    submenus: [
      { key: "/quality/quality_inspection_task", name: "质检任务" },
      { key: "/quality/quality_inspection_record", name: "质量巡检" },
    ],
  },
  {
    key: "device",
    name: "设备管理",
    icon: "database",
    submenus: [
      { key: "/device/info", name: "设备信息" },
      { key: "/device/spare_part", name: "备品备件" },
      { key: "/device/patrol_inspection", name: "巡检任务" },
      // { key: "/device/patrol_inspection_record", name: "巡检记录" },
      { key: "/device/repair", name: "维修任务" },
      // { key: "/device/repair_record", name: "维修记录" },
      { key: "/device/maintenance", name: "维保任务" },
      // { key: "/device/maintenance_record", name: "维保记录" },
      { key: "/device/status", name: "设备状态" },
    ],
  },
  {
    key: "system",
    name: "系统管理",
    icon: "team",
    submenus: [
      { key: "/system/role", name: "角色管理" },
      { key: "/system/user", name: "员工账号" },
    ],
  },
];
