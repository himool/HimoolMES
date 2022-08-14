<template>
  <div>
    <a-card :tab-list="tabList" :active-tab-key="currentTab" @tabChange="tabChange">
      <div v-if="currentTab == 'shelveTask'">
        <shelve-task-panel></shelve-task-panel>
      </div>
      <div v-else-if="currentTab == 'shelveRecord'">
        <shelve-record-panel></shelve-record-panel>
      </div>
    </a-card>
  </div>
</template>

<script>
  export default {
    components: {
      ShelveTaskPanel: () => import('./maintenanceTask/index'),
      ShelveRecordPanel: () => import('./maintenanceRecord/index'),
    },
    data() {
      return {
        tabList: [
          {
            key: 'shelveTask',
            tab: '维保任务',
          },
          {
            key: 'shelveRecord',
            tab: '维保记录',
          },
        ],
        currentTab: undefined,
      }
    },
    methods: {
      initData() {
        let currentTab = this.$route.query.currentTab;
        if (currentTab) {
          this.currentTab = currentTab;
        } else {
          this.currentTab = this.tabList[0].key;
          this.$router.push({ query: { currentTab: this.currentTab } });
        }
      },
      tabChange(key) {
        this.currentTab = key;
        this.$router.push({ query: { currentTab: this.currentTab } });
      },
    },
    mounted() {
      this.initData();
    },
  }
</script>