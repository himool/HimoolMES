import VueRouter from "vue-router";
import board from "./board";
import data from "./data";
import device from "./device";
import production from "./production";
import quality from "./quality";
import system from "./system";
import user from "./user";

const index = {
  path: "/",
  component: () => import("@/layouts/BaseLayout"),
  redirect: "/board/production",
};

const routes = [index, board, data, device, production, quality, system, user];

export default new VueRouter({ mode: "history", routes });
