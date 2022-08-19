<template>
  <div>
    <a-card title="BOM管理">
      <a-row :gutter="[12, 12]">
        <a-col :span="24" style="width: 256px">
          <a-input v-model="searchForm.search" placeholder="成品编号, 名称" allowClear @pressEnter="search" />
        </a-col>
        <a-col :span="24" style="width: 200px">
          <material-select v-model="searchForm.finish_product" placeholder="物料" @change="search" />
        </a-col>
        <a-col :span="24" style="width: 100px">
          <a-button type="primary" icon="search" @click="search" style="width: 100%">
            查询
          </a-button>
        </a-col>
        <a-col :span="24" style="width: 130px; float: right">
          <a-button type="primary" icon="plus" style="width: 100%" @click="createModalVisible = true">
            新增BOM
          </a-button>
        </a-col>

        <a-col :span="24">
          <a-table
            rowKey="id"
            :columns="columns"
            :dataSource="dataItems"
            :loading="dataLoading"
            :pagination="pagination"
            @change="changeTable"
          >
            <template slot="action" slot-scope="value, item">
              <table-action :dataItem="item" @update="update" @destroy="destroy" />
            </template>
          </a-table>
        </a-col>
      </a-row>
    </a-card>

    <create-form-modal v-model="createModalVisible" @create="create" @cancel="createModalVisible = false" />
  </div>
</template>

<script>
import { insertItem, replaceItem, removeItem } from "@/utils/functions";
import { materialBillList } from "@/apis/material";

export default {
  components: {
    MaterialSelect: () => import("@/components/MaterialSelect"),
    CreateFormModal: () => import("./CreateFormModal"),
    TableAction: () => import("./TableAction"),
  },
  data() {
    return {
      searchForm: { search: "", page: 1, ordering: undefined },
      pagination: { current: 1, total: 0, pageSize: 16 },
      dataLoading: false,

      // Table
      columns: [
        {
          title: "序号",
          dataIndex: "index",
          customRender: (_value, _item, index) => index + 1,
        },
        {
          title: "成品编号",
          dataIndex: "number",
          customRender: (_value, item) => item.finish_product_item.number,
        },
        {
          title: "成品名称",
          dataIndex: "name",
          customRender: (_value, item) => item.finish_product_item.name,
        },
        {
          title: "原料编号",
          dataIndex: "number",
          customRender: (_value, item) => item.raw_material_item.number,
        },
        {
          title: "原料名称",
          dataIndex: "name",
          customRender: (_value, item) => item.raw_material_item.name,
        },
        {
          title: "数量",
          dataIndex: "quantity",
        },
        {
          title: "备注",
          dataIndex: "remark",
        },
        {
          title: "操作",
          dataIndex: "action",
          scopedSlots: { customRender: "action" },
        },
      ],
      dataItems: [],

      createModalVisible: false,
    };
  },
  methods: {
    search() {
      this.searchForm.page = 1;
      this.pagination.current = 1;
      this.list();
    },
    list() {
      this.dataLoading = true;
      materialBillList(this.searchForm)
        .then((data) => {
          this.pagination.total = data.count;
          this.dataItems = data.results;
        })
        .finally(() => {
          this.dataLoading = false;
        });
    },
    create(item) {
      this.dataItems = insertItem(this.dataItems, item);
    },
    update(item) {
      this.dataItems = replaceItem(this.dataItems, item);
    },
    destroy(item) {
      this.dataItems = removeItem(this.dataItems, item);
    },
    changeTable(pagination, _filters, sorter) {
      this.searchForm.page = pagination.current;
      this.pagination.current = pagination.current;
      this.searchForm.ordering = `${sorter.order == "descend" ? "-" : ""}${sorter.field}`;
      this.list();
    },
  },
  mounted() {
    this.list();
  },
};
</script>

<style scoped></style>
