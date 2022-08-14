<template>
  <div>
    <a-card title="领料单">
      <a-button slot="extra" icon="printer" type="primary" style="margin-right: 8px;" ghost v-print="'#printContent'">
        打印
      </a-button>
      <a-button slot="extra" icon="left" type="primary" ghost @click="() => this.$router.go(-1)">
        返回
      </a-button>

      <a-table :columns="columns" :data-source="bomItems" :pagination="false">

      </a-table>
    </a-card>
  </div>
</template>

<script>
// import { productionOrderDetail } from "@/api/production";
import JsBarcode from "jsbarcode";

export default {
  data() {
    return {
      loading: false,
      item: {},
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
          title: "物料编号",
          dataIndex: "number",
        },
        {
          title: "物料名称",
          dataIndex: "name",
        },
        {
          title: "数量",
          dataIndex: "quantity",
        },
      ],
      bomItems: [
        { id: 2, number: "G000000000002", name: "原料A", quantity: 10 },
        { id: 3, number: "G000000000003", name: "原料B", quantity: 5 },
      ],
    };
  },
  methods: {
    getJsBarcode(number) {
      JsBarcode("#barcode", number, {
        lineColor: "#000",
        width: 2,
        height: 40,
        displayValue: true,
      });
    },
    initData() {},
  },
  mounted() {
    this.initData();
  },
};
</script>
<style></style>
