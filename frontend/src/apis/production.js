import request from "@/utils/request";

// ProcessRoute
export function processRouteList(params) {
  return request({ url: `/process_routes/`, method: "get", params });
}

export function processRouteCreate(data) {
  return request({ url: `/process_routes/`, method: "post", data });
}

export function processRouteUpdate(data) {
  return request({ url: `/process_routes/${data.id}/`, method: "put", data });
}

export function processRouteDestroy(data) {
  return request({ url: `/process_routes/${data.id}/`, method: "delete", data });
}
