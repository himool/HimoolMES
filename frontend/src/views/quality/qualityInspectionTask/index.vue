<template>
  <div>
    <a-card title="巡检任务">
      <a-row gutter="16">
        <a-col :span="24" style="max-width: 200px; margin-bottom: 12px;">
          <a-input v-model="searchForm.search" placeholder="编号, 名称" allowClear @pressEnter="search" />
        </a-col>
        <a-col :span="24" style="width: 100px; margin-bottom: 12px;">
          <a-button type="primary" icon="search" @click="search">查询</a-button>
        </a-col>

        <!-- <div style="margin-bottom: 12px; float: right;">
          <a-button type="primary" icon="plus" style="margin: 0 8px;" @click="openFormModal({})">新增巡检任务</a-button>
        </div> -->
      </a-row>

      <a-row style="margin-top: 12px;">
        <a-table
          rowKey="id"
          size="small"
          :columns="columns"
          :dataSource="items"
          :loading="loading"
          :pagination="pagination"
          @change="tableChange"
        >
          <div slot="action" slot-scope="value, item">
            <a-button-group>
              <a-button icon="edit" size="small" @click="openFormModal(item)">质检</a-button>
              <!-- <a-popconfirm title="确定删除吗" @confirm="destroy(item.id)">
                <a-button type="danger" icon="delete" size="small">删除</a-button>
              </a-popconfirm> -->
            </a-button-group>
          </div>
        </a-table>
      </a-row>
    </a-card>

    <form-modal v-model="visible" :form="targetItem" @create="create" @update="update" />
  </div>
</template>

<script>
// import { deviceList, deviceDestroy } from "@/api/manage";

export default {
  components: {
    FormModal: () => import("./FormModal.vue"),
  },
  data() {
    return {
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
          title: "状态",
          dataIndex: "status_display",
          width: 100,
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
          title: "计划数量",
          dataIndex: "total_quantity",
          width: 100,
        },
        {
          title: "完成数量",
          dataIndex: "completed_quantity",
          width: 100,
        },
        {
          title: "操作",
          dataIndex: "action",
          fixed: "right",
          width: 256,
          scopedSlots: { customRender: "action" },
        },
      ],
      searchForm: { search: "", page: 1, page_size: 15 },
      pagination: { current: 1, total: 0, pageSize: 15 },
      loading: false,
      items: [],

      visible: false,
      targetItem: {},
    };
  },
  methods: {
    initialize() {
      this.items = [
        {
          id: 1,
          number: "p2022061000002",
          status: "in_progress",
          status_display: "生产中",
          material_number: "P002",
          material_name: "轴承",
          total_quantity: 100,
          quantity_produced: 10,
          completed_quantity: 20,
          start_time: "2022-06-12 00:00:00",
          end_time: "2022-06-12 00:00:00",
        },
        {
          id: 2,
          number: "p2022061000003",
          status: "in_progress",
          status_display: "生产中",
          material_number: "P002",
          material_name: "轴承",
          total_quantity: 200,
          quantity_produced: 20,
          completed_quantity: 140,
          start_time: "2022-06-20 00:00:00",
          end_time: "2022-06-12 00:00:00",
        },
      ];
      // this.list();
    },
    list() {
      // this.loading = true;
      // deviceList(this.searchForm)
      //   .then((response) => {
      //     console.log(response);
      //     this.pagination.total = response.data.count;
      //     this.items = response.data.results;
      //   })
      //   .finally(() => {
      //     this.loading = false;
      //   });
    },
    create(item) {
      // this.list();
    },
    update(item) {
      // this.list();
    },
    search() {
      // this.searchForm.page = 1;
      // this.pagination.current = 1;
      // this.list();
    },
    openFormModal(item) {
      this.targetItem = { ...item };
      this.visible = true;
    },
    destroy(id) {
      // deviceDestroy({ id }).then(() => {
      //   this.$message.success("删除成功");
      //   this.list();
      // });
    },
    tableChange(pagination, filters, sorter) {
      // this.searchForm.page = pagination.current;
      // this.pagination.current = pagination.current;
      // this.searchForm.ordering = `${sorter.order == "descend" ? "-" : ""}${sorter.field}`;
      // this.list();
    },
  },
  mounted() {
    this.initialize();
  },
};
</script>
