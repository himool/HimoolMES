import request from "@/utils/request";

// System
export function roleOption(params) {
  return request({ url: `/roles/options/`, method: "get", params });
}
