import request from "@/utils/request";

// MaterialCategory
export function materialCategoryList(params) {
  return request({ url: `/material_categories/`, method: "get", params });
}

export function materialCategoryCreate(data) {
  return request({ url: `/material_categories/`, method: "post", data });
}

export function materialCategoryUpdate(data) {
  return request({ url: `/material_categories/${data.id}/`, method: "put", data });
}

export function materialCategoryDestroy(data) {
  return request({ url: `/material_categories/${data.id}/`, method: "delete", data });
}

// Material
export function materialList(params) {
  return request({ url: `/materials/`, method: "get", params });
}

export function materialCreate(data) {
  return request({ url: `/materials/`, method: "post", data });
}

export function materialUpdate(data) {
  return request({ url: `/materials/${data.id}/`, method: "put", data });
}

export function materialDestroy(data) {
  return request({ url: `/materials/${data.id}/`, method: "delete", data });
}

// MaterialBill
export function materialBillList(params) {
  return request({ url: `/material_bills/`, method: "get", params });
}

export function materialBillCreate(data) {
  return request({ url: `/material_bills/`, method: "post", data });
}

export function materialBillUpdate(data) {
  return request({ url: `/material_bills/${data.id}/`, method: "put", data });
}

export function materialBillDestroy(data) {
  return request({ url: `/material_bills/${data.id}/`, method: "delete", data });
}
