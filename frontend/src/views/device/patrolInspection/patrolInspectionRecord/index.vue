<template>
  <div>
      <a-row gutter="16">
        <a-col :span="24" style="max-width: 200px; margin-bottom: 12px;">
          <a-input v-model="searchForm.search" placeholder="编号, 名称" allowClear @pressEnter="search" />
        </a-col>
        <a-col :span="24" style="width: 100px; margin-bottom: 12px;">
          <a-button type="primary" icon="search" @click="search">查询</a-button>
        </a-col>

        <!-- <div style="margin-bottom: 12px; float: right;">
          <a-button type="primary" icon="plus" style="margin: 0 8px;" @click="openFormModal({})">新增巡检记录</a-button>
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
              <a-button icon="edit" size="small" @click="openFormModal(item)">编辑</a-button>
              <a-popconfirm title="确定删除吗" @confirm="destroy(item.id)">
                <a-button type="danger" icon="delete" size="small">删除</a-button>
              </a-popconfirm>
            </a-button-group>
          </div>
        </a-table>
      </a-row>

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
          title: "检查部位",
          dataIndex: "position",
        },
        {
          title: "标准及评定基准",
          dataIndex: "standard",
        },
        {
          title: "状态",
          dataIndex: "status",
        },
        {
          title: "巡检时间",
          dataIndex: "create_time",
        },
        {
          title: "备注",
          dataIndex: "remark",
        },
        // {
        //   title: "操作",
        //   dataIndex: "action",
        //   scopedSlots: { customRender: "action" },
        //   width: "156px",
        // },
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
          position: "控制",
          standard: "开关/按钮/显示器/指示灯齐全有效无破损",
          status: "正常运行",
          create_time: "2022-06-20 09:00:00",
          remark: "",
        },
        {
          id: 2,
          position: "机械机构",
          standard: "正常开机, 通过系统自检程序, 正常运行",
          status: "正常运行",
          create_time: "2022-06-20 09:00:00",
          remark: "",
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
