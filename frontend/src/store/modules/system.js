export default {
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
      state.userInfo = item;
    },
  },
};
