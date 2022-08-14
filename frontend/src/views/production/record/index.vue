<template>
  <div>
    <a-card title="报工记录">
      <a-row :gutter="[12, 8]">
        <a-col :span="24" style="width: 256px;">
          <a-range-picker @change="onChangePicker" />
        </a-col>
        <a-col :span="24" style="width: 200px;">
          <a-input v-model="searchForm.search" placeholder="生产单号, 销售单号" allowClear @pressEnter="search" />
        </a-col>
        <a-col :span="24" style="width: 84px;">
          <a-button type="primary" icon="search" @click="search">查询</a-button>
        </a-col>
      </a-row>

      <a-row style="margin-top: 12px">
        <a-table rowKey="id" :columns="columns" :data-source="items" :pagination="pagination" :loading="loading">
          <div slot="action" slot-scope="value, item">
            <a-button-group>
              <a-button size="small" @click="openFormModal(item)">质检</a-button>
            </a-button-group>
          </div>
        </a-table>
      </a-row>
    </a-card>

    <a-modal v-model="checkVisible" title="质检">
      <a-form-model :label-col="{ span: 6 }" :wrapper-col="{ span: 16 }">
        <a-form-model-item label="不合格数量">
          <a-input-number style="width: 100%;" />
        </a-form-model-item>
      </a-form-model>
    </a-modal>
  </div>
</template>

<script>
// import { productionRecordList } from "@/api/production";

export default {
  data() {
    return {
      searchForm: { search: "", page: 1, ordering: undefined },
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
          title: "生产计划单号",
          dataIndex: "production_order_number",
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
          title: "生产数量",
          dataIndex: "production_quantity",
          width: 100,
        },
        {
          title: "创建时间",
          dataIndex: "create_time",
          width: 180,
        },
        {
          title: "创建人",
          dataIndex: "creator_name",
          width: 180,
        },
        // {
        //   title: "操作",
        //   dataIndex: "action",
        //   fixed: "right",
        //   width: 100,
        //   scopedSlots: { customRender: "action" },
        // },
      ],
      checkItem: {},
      checkVisible: false,
    };
  },
  methods: {
    initialize() {
      this.items = [
        {
          id: 1,
          production_order_number: "p2022061000001",
          material_number: "P001",
          material_name: "手机",
          production_quantity: 10,
          create_time: "2022-06-12 00:00:00",
          creator_name: "admin",
        },
        {
          id: 2,
          production_order_number: "p2022061000002",
          material_number: "P002",
          material_name: "电脑",
          production_quantity: 10,
          create_time: "2022-06-12 00:00:00",
          creator_name: "admin",
        },
      ];
      // this.list();
    },
    list() {
      // this.loading = true;
      // productionRecordList(this.searchForm)
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
    openFormModal(item) {
      this.checkItem = { ...item };
      this.checkVisible = true;
    },
  },
  mounted() {
    this.initialize();
  },
};
</script>

<style scoped></style>
