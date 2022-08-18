import request from "@/utils/request";

// System
export function roleOption(params) {
  return request({ url: `/roles/options/`, method: "get", params });
}

export function materialCategoryOption(params) {
  return request({ url: `/material_categories/options/`, method: "get", params });
}
