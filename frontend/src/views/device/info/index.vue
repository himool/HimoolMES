<template>
  <div>
    <a-card title="设备管理">
      <a-row gutter="16">
        <a-col :span="24" style="max-width: 200px; margin-bottom: 12px;">
          <a-input v-model="searchForm.search" placeholder="编号, 名称" allowClear @pressEnter="search" />
        </a-col>
        <a-col :span="24" style="width: 100px; margin-bottom: 12px;">
          <a-button type="primary" icon="search" @click="search">查询</a-button>
        </a-col>

        <div style="margin-bottom: 12px; float: right;">
          <a-button type="primary" icon="plus" style="margin: 0 8px;" @click="openFormModal({})">新增设备</a-button>
        </div>
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
              <a-button icon="edit" size="small" @click="openFormModal(item)">编辑</a-button>
              <a-popconfirm title="确定删除吗" @confirm="destroy(item.id)">
                <a-button type="danger" icon="delete" size="small">删除</a-button>
              </a-popconfirm>
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
          key: "index",
          customRender: (value, item, index) => {
            return index + 1;
          },
        },
        {
          title: "设备编号",
          dataIndex: "number",
        },
        {
          title: "设备名称",
          dataIndex: "name",
        },
        {
          title: "规格型号",
          dataIndex: "model",
        },
        {
          title: "设备类型",
          dataIndex: "category",
        },
        {
          title: "供应商",
          dataIndex: "supplier",
        },
        {
          title: "录入人",
          dataIndex: "creator_name",
        },
        {
          title: "录入时间",
          dataIndex: "create_time",
        },
        {
          title: "操作",
          dataIndex: "action",
          scopedSlots: { customRender: "action" },
          width: "156px",
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
          number: "D001",
          name: "焊机",
          model: "TL-1001",
          category: "焊接机",
          supplier: "京东",
          creator_name: "admin",
          create_time: "2022-06-20 09:00:00",
        },
        {
          id: 2,
          number: "D002",
          name: "焊机",
          model: "TL-1001",
          category: "焊接机",
          supplier: "京东",
          creator_name: "admin",
          create_time: "2022-06-20 09:00:00",
        },
        {
          id: 3,
          number: "D003",
          name: "测试仪",
          model: "TL-2001",
          category: "仪器",
          supplier: "京东",
          creator_name: "admin",
          create_time: "2022-06-20 09:00:00",
        },
        {
          id: 4,
          number: "D004",
          name: "涂覆机",
          model: "TL-3001",
          category: "其他",
          supplier: "京东",
          creator_name: "admin",
          create_time: "2022-06-20 09:00:00",
        },
        {
          id: 5,
          number: "D005",
          name: "涂覆机",
          model: "TL-4001",
          category: "其他",
          supplier: "京东",
          creator_name: "admin",
          create_time: "2022-06-20 09:00:00",
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
