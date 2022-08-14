<template>
  <div>
    <a-card title="生产计划详情">
      <a-button slot="extra" type="primary" style="margin-right: 8px;" ghost v-print="'#printContent'">
        <a-icon type="printer" />打印</a-button
      >
      <a-button slot="extra" type="primary" ghost @click="$router.go(-1)"> <a-icon type="left" />返回</a-button>
      <section id="printContent">
        <div style="font-size: 36px; font-weight: 400; text-align: center">生产工单</div>
        <a-row>
          <a-col :span="24">
            <img class="jsbarcode" id="jsbarcode" ref="jsbarcode" />
          </a-col>
          <a-col :span="8">物料编号: {{ item.material_number }}</a-col>
          <a-col :span="8">物料名称: {{ item.material_name }}</a-col>
          <a-col :span="8">计划数量: {{ item.total_quantity }}</a-col>
          <a-col :span="8">完成数量: {{ item.quantity_produced }}</a-col>
          <a-col :span="8">计划开始时间: {{ item.start_time }}</a-col>
          <a-col :span="8">计划结束时间: {{ item.end_time }}</a-col>
          <a-col :span="8">创建时间: {{ item.create_time }}</a-col>
          <a-col :span="8">创建人: {{ item.creator_name }}</a-col>
        </a-row>
          
        <div style="margin-top: 16px">
          <table border="1" style="width: 100%">
            <tr>
              <th>序号</th>
              <th>工序名称</th>
              <th>计划数量</th>
              <th>完成数量</th>
              <th>计划开始时间</th>
              <th>计划结束时间</th>
            </tr>
            <tr v-for="(item, index) in materialItems" :key="item.id">
              <td>{{ index + 1 }}</td>
              <td>{{ item.process_name }}</td>
              <td>{{ item.total_quantity }}</td>
              <td>{{ item.quantity_produced }}</td>
              <td>{{ item.start_time }}</td>
              <td>{{ item.end_time }}</td>
            </tr>
          </table>
        </div>
      </section>

      <!-- <section id="printContent">
        
        <a-spin :spinning="loading">
          <img id="barcode" style="float: right" />
          <a-descriptions bordered>
            <a-descriptions-item label="生产计划单号">
              {{ item.number }}
            </a-descriptions-item>
            <a-descriptions-item label="状态">
              {{ item.status_display }}
            </a-descriptions-item>
            <a-descriptions-item label="物料编号">
              {{ item.material_number }}
            </a-descriptions-item>
            <a-descriptions-item label="物料名称">
              {{ item.material_name }}
            </a-descriptions-item>
            <a-descriptions-item label="计划数量">
              {{ item.total_quantity }}
            </a-descriptions-item>
            <a-descriptions-item label="完成数量">
              {{ item.quantity_produced }}
            </a-descriptions-item>
            <a-descriptions-item label="计划开始时间">
              {{ item.start_time }}
            </a-descriptions-item>
            <a-descriptions-item label="计划结束时间">
              {{ item.end_time }}
            </a-descriptions-item>
            <a-descriptions-item label="创建时间">
              {{ item.create_time }}
            </a-descriptions-item>
            <a-descriptions-item label="创建人">
              {{ item.creator_name }}
            </a-descriptions-item>
          </a-descriptions>
        </a-spin>
      </section> -->
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
      materialItems: [
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
    initData() {
      new JsBarcode(this.$refs.jsbarcode, 'p2022061000001', {
            format: "CODE128",
            width: 2,
            height: 35,
            displayValue: true,
            background: "#ffffff",
            lineColor: "#000000",
          });

      this.item = {
        number: "p2022061000001",
        status_display: "生产中",
        material_number: "P001",
        material_name: "手机",
        total_quantity: 100,
        quantity_produced: 10,
        start_time: "2022-06-12 00:00:00",
        end_time: "2022-06-12 00:00:00",
        create_time: "2022-06-10 00:00:00",
        creator_name: "admin",
      };
      // this.loading = true;
      // productionOrderDetail({ id: this.$route.query.id })
      //   .then((data) => {
      //     this.item = data;
      //     this.getJsBarcode(data.number);
      //   })
      //   .finally(() => {
      //     this.loading = false;
      //   });
    },
  },
  mounted() {
    this.initData();
  },
};
</script>
<style>
  .jsbarcode {
    display: inline-block;
    float: right;
  }
  </style>
  