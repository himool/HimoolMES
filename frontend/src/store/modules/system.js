export default {
  namespaced: true,
  state: () => ({
    userInfo: {
      id: undefined,
      username: "",
      name: "",
      is_manager: false,
      permissions: [],
    },
  }),
  mutations: {
    serUserInfo(state, item) {
      console.log(item)
      state.userInfo = item;
    },
  },
};
