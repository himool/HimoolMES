<template>
  <div>
    <a-card title="物料管理">
      <a-row :gutter="[12, 12]">
        <a-col :span="24" style="width: 256px">
          <a-input v-model="searchForm.search" placeholder="编号, 名称, 备注" allowClear @pressEnter="search" />
        </a-col>
        <a-col :span="24" style="width: 200px">
          <material-category-select v-model="searchForm.category" placeholder="分类" @change="search" />
        </a-col>
        <a-col :span="24" style="width: 200px">
          <a-select v-model="searchForm.type" placeholder="类型" allowClear style="width: 100%" @change="search">
            <a-select-option key="raw_material" value="raw_material">原材料</a-select-option>
            <a-select-option key="finish_product" value="finish_product">成品</a-select-option>
          </a-select>
        </a-col>
        <a-col :span="24" style="width: 100px">
          <a-button type="primary" icon="search" @click="search" style="width: 100%">
            查询
          </a-button>
        </a-col>
        <a-col :span="24" style="width: 130px; float: right">
          <a-button type="primary" icon="plus" style="width: 100%" @click="createModalVisible = true">
            新增物料
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
import { materialList } from "@/apis/material";

export default {
  components: {
    MaterialCategorySelect: () => import("@/components/MaterialCategorySelect"),
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
          title: "编号",
          dataIndex: "number",
        },
        {
          title: "名称",
          dataIndex: "name",
        },
        {
          title: "类型",
          dataIndex: "type_display",
        },
        {
          title: "分类",
          dataIndex: "category_name",
          customRender: (_value, item) => item.category_item?.name,
        },
        {
          title: "规格",
          dataIndex: "spec",
        },
        {
          title: "单位",
          dataIndex: "unit",
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
      materialList(this.searchForm)
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
