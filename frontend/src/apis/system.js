import request from "@/utils/request";

export function permissionGroupList(params) {
  return request({ url: `/permission_groups/`, method: "get", params });
}

export function makeToken(data) {
  return request({ url: `/user/make_token/`, method: "post", data });
}

export function refreshToken(data) {
  return request({ url: `/user/refresh_token/`, method: "post", data });
}

export function logoffToken(data) {
  return request({ url: `/user/logoff_token/`, method: "post", data });
}

export function getInfo(params) {
  return request({ url: `/user/info/`, method: "get", params });
}

export function setPassword(data) {
  return request({ url: `/user/set_password/`, method: "post", data });
}

// Role
export function roleList(params) {
  return request({ url: `/roles/`, method: "get", params });
}

export function roleCreate(data) {
  return request({ url: `/roles/`, method: "post", data });
}

export function roleUpdate(data) {
  return request({ url: `/roles/${data.id}/`, method: "put", data });
}

export function roleDestroy(data) {
  return request({ url: `/roles/${data.id}/`, method: "delete", data });
}

// User
export function userList(params) {
  return request({ url: `/users/`, method: "get", params });
}

export function userCreate(data) {
  return request({ url: `/users/`, method: "post", data });
}

export function userUpdate(data) {
  return request({ url: `/users/${data.id}/`, method: "put", data });
}

export function userDestroy(data) {
  return request({ url: `/users/${data.id}/`, method: "delete", data });
}

export function userResetPassword(data) {
  return request({ url: `/users/${data.id}/reset_password/`, method: "post", data });
}
