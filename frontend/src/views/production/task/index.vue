<template>
  <div>
    <a-card title="生产任务">
      <a-row :gutter="[12, 8]">
        <a-col :span="24" style="width: 256px;">
          <a-range-picker @change="onChangePicker" />
        </a-col>
        <a-col :span="24" style="width: 200px;">
          <a-input v-model="searchForm.search" placeholder="生产单号" allowClear @pressEnter="search" />
        </a-col>
        <a-col :span="24" style="width: 84px;">
          <a-button type="primary" icon="search" @click="search">查询</a-button>
        </a-col>
      </a-row>

      <a-row style="margin-top: 12px">
        <a-table
          rowKey="id"
          :columns="columns"
          :data-source="items"
          :pagination="pagination"
          :loading="loading"
          :scroll="{ x: 1600 }"
        >
          <div slot="action" slot-scope="value, item, index">
            <a-button-group size="small">
              <a-button @click="detial(item)">详情</a-button>
              <a-button type="primary" @click="openCreateModal(item)">报工</a-button>
            </a-button-group>
          </div>
        </a-table>
      </a-row>
    </a-card>

    <form-modal v-model="visible" :form="targetItem" @create="create" />
  </div>
</template>

<script>
// import { productionOrderList } from "@/api/production";

export default {
  components: {
    FormModal: () => import("./FormModal.vue"),
  },
  data() {
    return {
      searchForm: { search: "", page: 1, ordering: undefined, status: "in_progress" },
      pagination: { current: 1, total: 0, pageSize: 16 },
      loading: false,
      items: [],
      columns: [
        {
          title: "序号",
          dataIndex: "index",
          width: 60,
          fixed: "left",
          customRender: (value, item, index) => {
            return index + 1;
          },
        },
        {
          title: "工单单号",
          dataIndex: "number",
          fixed: "left",
        },
        {
          title: "物料编号",
          dataIndex: "material_number",
        },
        {
          title: "物料名称",
          dataIndex: "material_name",
        },
        {
          title: "工序",
          dataIndex: "process_name",
        },
        {
          title: "计划数量",
          dataIndex: "total_quantity",
          width: 100,
        },
        {
          title: "完成数量",
          dataIndex: "quantity_produced",
          width: 100,
        },
        {
          title: "计划开始时间",
          dataIndex: "start_time",
          width: 180,
        },
        {
          title: "计划结束时间",
          dataIndex: "end_time",
          width: 180,
        },
        {
          title: "操作",
          dataIndex: "action",
          fixed: "right",
          width: 160,
          scopedSlots: { customRender: "action" },
        },
      ],
      visible: false,
      targetItem: {},
    };
  },
  methods: {
    initialize() {
      this.items = [
        {
          id: 1,
          number: "p2022061000001",
          status_display: "生产中",
          material_number: "G000000000001",
          material_name: "轴承",
          process_name: "退火",
          total_quantity: 100,
          quantity_produced: 10,
          start_time: '2022-06-12 00:00:00',
          end_time: '2022-06-12 00:00:00',
        },
        {
          id: 2,
          number: "p2022061000001",
          status_display: "生产中",
          material_number: "G000000000001",
          material_name: "轴承",
          process_name: "车加工",
          total_quantity: 100,
          quantity_produced: 10,
          start_time: '2022-06-12 00:00:00',
          end_time: '2022-06-12 00:00:00',
        },
        {
          id: 3,
          number: "p2022061000001",
          status_display: "生产中",
          material_number: "G000000000001",
          material_name: "轴承",
          process_name: "热处理",
          total_quantity: 100,
          quantity_produced: 10,
          start_time: '2022-06-12 00:00:00',
          end_time: '2022-06-12 00:00:00',
        },
        {
          id: 4,
          number: "p2022061000001",
          status_display: "生产中",
          material_number: "G000000000001",
          material_name: "轴承",
          process_name: "磨加工",
          total_quantity: 100,
          quantity_produced: 10,
          start_time: '2022-06-12 00:00:00',
          end_time: '2022-06-12 00:00:00',
        },
        {
          id: 5,
          number: "p2022061000001",
          status_display: "生产中",
          material_number: "G000000000001",
          material_name: "轴承",
          process_name: "抛光",
          total_quantity: 100,
          quantity_produced: 10,
          start_time: '2022-06-12 00:00:00',
          end_time: '2022-06-12 00:00:00',
        },
        {
          id: 6,
          number: "p2022061000001",
          status_display: "生产中",
          material_number: "G000000000001",
          material_name: "轴承",
          process_name: "防锈",
          total_quantity: 100,
          quantity_produced: 10,
          start_time: '2022-06-12 00:00:00',
          end_time: '2022-06-12 00:00:00',
        },
      ];
      // this.list();
    },
    list() {
      // this.loading = true;
      // productionOrderList(this.searchForm)
      //   .then((data) => {
      //     this.pagination.total = data.count;
      //     this.items = data.results;
      //   })
      //   .finally(() => {
      //     this.loading = false;
      //   });
    },
    create() {
      // this.list();
    },
    detial(item) {
      this.$router.push({ path: "/production/detial", query: { id: item.id } });
    },
    search() {
      // this.searchForm.page = 1;
      // this.pagination.current = 1;
      // this.list();
    },
    tableChange(pagination, filters, sorter) {
      // this.searchForm.page = pagination.current;
      // this.pagination.current = pagination.current;
      // this.searchForm.ordering = `${sorter.order == "descend" ? "-" : ""}${sorter.field}`;
      // this.list();
    },
    onChangePicker(date, dateString) {
      // let startDate = date[0];
      // let endDate = date[1];
      // this.searchForm.start_date = startDate ? startDate.format("YYYY-MM-DD") : undefined;
      // this.searchForm.end_date = endDate ? endDate.add(1, "days").format("YYYY-MM-DD") : undefined;
      // this.search();
    },
    openCreateModal(item) {
      this.targetItem = { ...item };
      this.visible = true;
    },
  },
  mounted() {
    this.initialize();
  },
};
</script>

<style scoped></style>
