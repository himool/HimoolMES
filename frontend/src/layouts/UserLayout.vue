<template>
  <div class="background" ref="card">
    <a-card class="card">
      <div>
        <div style="text-align: center; padding-top: 32px;">
          <img :src="logo" width="112" style="margin-top: 12px; margin-left: 8px; cursor: pointer;"
            @click="backIndex" />
        </div>
        <div class="title" style="margin-bottom: 24px; margin-top: 8px;">
          <span style="cursor: pointer; font-size: 24px;" @click="backIndex">Himool MES</span>
        </div>
        <!-- <div style="text-align: center; font-size: 16px; color: #666; margin-bottom: 24px;">MES - 让企业管理更简单高效</div> -->
      </div>
      <router-view />
    </a-card>
  </div>
</template>

<script>
  export default {
    name: 'UserLayout',
    data() {
      return {
        logo: require('@/assets/logo.png'),
      }
    },
    methods: {
      backIndex() {
        // window.open('http://www.haioucloud.com', '_self');
      },
    },
  }
</script>

<style scoped>
  .card {
    width: 480px;
    border-radius: 8px;
    padding-bottom: 64px;
    margin: auto;
  }

  .background {
    min-height: 100%;
    padding: 10vh 0;
    background: #f0f2f5 url('~@/assets/background.svg') no-repeat 50%;
  }

  .title {
    text-align: center;
    /* font-size: 32px; */
    color: #1890ff;
    margin-top: 8px;
    font-weight: bold;
  }
</style>