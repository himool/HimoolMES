<template>
  <div>
    <a-card title="BOM管理">
      <a-row gutter="16">
        <a-col :span="24" style="max-width: 200px; margin-bottom: 12px;">
          <a-input v-model="searchForm.search" placeholder="编号, 名称" allowClear @pressEnter="search" />
        </a-col>
        <a-col :span="24" style="width: 100px; margin-bottom: 12px;">
          <a-button type="primary" icon="search" @click="search">查询</a-button>
        </a-col>

        <a-col :span="24" style="width: 300px; margin-bottom: 12px;">
          <a-button-group>
            <a-button icon="file-excel" @click="downloadTemplate">模板下载</a-button>
            <a-upload name="file" :showUploadList="false" :customRequest="importExcel">
              <a-button icon="upload">导入</a-button>
            </a-upload>
            <a-button icon="download" @click="exportExcel">导出</a-button>
          </a-button-group>
        </a-col>

        <div style="margin-bottom: 12px; float: right;">
          <a-button type="primary" icon="plus" style="margin: 0 8px;" @click="openFormModal({})">新增BOM</a-button>
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
          <div slot="is_active" slot-scope="value">
            <a-tag :color="value ? 'green' : 'red'">{{ value ? "激活" : "冻结" }}</a-tag>
          </div>
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
          title: "编号",
          dataIndex: "number",
        },
        {
          title: "名称",
          dataIndex: "name",
        },
        {
          title: "分类",
          dataIndex: "category_name",
        },
        {
          title: "状态",
          dataIndex: "is_active",
          scopedSlots: { customRender: "is_active" },
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
          number: "G000000000001",
          name: "轴承",
          category_name: "成品",
          is_active: true,
          bom_items: [
            { id: 2, number: "G000000000002", name: "原料A", quantity: 10 },
            { id: 3, number: "G000000000003", name: "原料B", quantity: 5 },
          ],
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
    exportExcel() {
      // goodsInformationExport(this.searchForm)
      //   .then((resp) => {
      //     exportExcel(resp.data, "物料信息列表");
      //   })
      //   .catch((err) => {
      //     this.$message.error(err.response.data.error);
      //   });
    },
    downloadTemplate() {
      // goodsInformationTemplate()
      //   .then((resp) => {
      //     exportExcel(resp.data, "物料信息导入模板");
      //   })
      //   .catch((err) => {
      //     this.$message.error(err.response.data.error);
      //   });
    },
    importExcel(item) {
      // let data = new FormData();
      // data.append("file", item.file);
      // this.importLoading = true;
      // setTimeout(() => {
      //   goodsInformationImport(data)
      //     .then(() => {
      //       this.$message.success("导入成功");
      //       this.list();
      //     })
      //     .catch((err) => {
      //       this.$message.error(err.response.data.detail);
      //     })
      //     .finally(() => {
      //       this.importLoading = false;
      //     });
      // }, 1000);
    },
  },
  mounted() {
    this.initialize();
  },
};
</script>
