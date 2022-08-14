<template>
  <div>
    <a-row :gutter="[8, 8]">
      <a-col :span="8">
        <a-card :bordered="false" size="small" :body-style="{ padding: '8px 0px' }" style="overflow: hidden">
          <div slot="title">
            <img :src="stockInImage" width="16" height="16" style="margin-top: -2px" />
            <span style="margin-left: 8px">今日工单执行进度</span>
          </div>

          <div style="height: 140px">
            <a-card-grid class="smallCard" :hoverable="false">
              <span class="number">99</span>
              <span class="intro">今日已完成</span>
            </a-card-grid>
            <a-card-grid class="smallCard" :hoverable="false">
              <span class="number" style="color: #1890ff">88</span>
              <span class="intro">待生产</span>
            </a-card-grid>
            <div style="margin-bottom: 24px">
              <a-progress :percent="70" style="width: 100%; padding: 0px 36px" />
            </div>
          </div>
        </a-card>
      </a-col>
      <a-col :span="8">
        <a-card :bordered="false" size="small" :body-style="{ padding: '8px 0px' }" style="overflow: hidden">
          <div slot="title">
            <img :src="stockOutImage" width="16" height="16" style="margin-top: -2px" />
            <span style="margin-left: 8px">今日工单延误率</span>
          </div>

          <div style="height: 140px">
            <a-card-grid class="smallCard" :hoverable="false">
              <span class="number">100</span>
              <span class="intro">延期工单</span>
            </a-card-grid>
            <a-card-grid class="smallCard" :hoverable="false">
              <span class="number" style="color: #ffa940">200</span>
              <span class="intro">总工单</span>
            </a-card-grid>
            <div style="margin-bottom: 24px">
              <a-progress :percent="50" strokeColor="#ffa940" style="width: 100%; padding: 0px 36px" />
            </div>
          </div>
        </a-card>
      </a-col>
      <a-col :span="8">
        <a-card :bordered="false" size="small" :body-style="{ padding: '8px 0px' }" style="overflow: hidden">
          <div slot="title">
            <img :src="materialImage" width="16" height="16" style="margin-top: -2px" />
            <span style="margin-left: 8px">产品完成进度</span>
          </div>
          <div style="height: 140px; text-align: center">
            <a-card-grid class="smallCard" :hoverable="false">
              <div style="margin-top: 24px">
                <span class="number"> <span style="color: #bae637">546</span>/2341 </span>
                <span class="intro">占用</span>
              </div>
            </a-card-grid>
            <a-card-grid class="smallCard" :hoverable="false">
              <a-progress type="circle" :percent="25" strokeColor="#bae637" :width="90" />
            </a-card-grid>
          </div>
        </a-card>
      </a-col>
    </a-row>

    <a-row :gutter="[8, 8]">
      <a-col :span="12">
        <a-card :bordered="false" size="small" style="height: 260px">
          <template slot="title">工序生产进度</template>
          <template slot="extra">
            <a-select size="small" placeholder="工单号" style="width: 200px; margin: -2px 0" />
          </template>

          <div>
            <a-table size="small" :columns="columns" :dataSource="dataSource" :pagination="false" :scroll="{ y: 150 }">
              <template slot="chart" slot-scope="value, item">
                <a-progress :percent="item.completed_quantity" />
              </template>
            </a-table>
          </div>
        </a-card>
      </a-col>
      <a-col :span="12">
        <a-card :bordered="false" size="small" style="height: 260px">
          <template slot="title">工序生产进度</template>
          <template slot="extra">
            <a-select size="small" placeholder="工单号" style="width: 200px; margin: -2px 0" />
          </template>
          <div id="container1" />
        </a-card>
      </a-col>
    </a-row>

    <a-row :gutter="[8, 8]">
      <a-col :span="24">
        <a-card :bordered="false" size="small" style="height: 260px">
          <template slot="title">工单生产进度</template>

          <div>
            <a-table size="small" :columns="columns1" :dataSource="dataSource1" :pagination="false" :scroll="{ y: 150 }">
              <template slot="chart" slot-scope="value, item">
                <a-progress :percent="item.completed_quantity / item.total_quantity * 100" />
              </template>
            </a-table>
          </div>
        </a-card>
      </a-col>
    </a-row>
  </div>
</template>

<script>
import { Column } from "@antv/g2plot";

export default {
  data() {
    return {
      stockInImage: require("./StockIn.png"),
      stockOutImage: require("./StockOut.png"),
      materialImage: require("./Material.png"),

      container1: null,
      columns: [
        {
          title: "序号",
          dataIndex: "index",
          customRender: (value, item, index) => index + 1,
          width: 60,
        },
        {
          title: "工序",
          dataIndex: "process_name",
        },
        {
          title: "需求数量",
          dataIndex: "total_quantity",
        },
        {
          title: "完成数量",
          dataIndex: "completed_quantity",
        },
        {
          title: "完成进度",
          dataIndex: "completed_progress",
        },
        {
          title: "图表",
          dataIndex: "chart",
          width: 200,
          scopedSlots: { customRender: "chart" },
        },
      ],
      columns1: [
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
        },
        {
          title: "完成进度",
          dataIndex: "completed_progress",
        },
        {
          title: "图表",
          dataIndex: "chart",
          width: 200,
          scopedSlots: { customRender: "chart" },
        },
      ],
      dataSource1: [
        {
          id: 2,
          number: "p2022061000002",
          status: "in_progress",
          status_display: "生产中",
          material_number: "P002",
          material_name: "轴承",
          total_quantity: 1000,
          completed_quantity: 800,
          completed_progress: "80%",
          start_time: "2022-06-12 00:00:00",
          end_time: "2022-06-12 00:00:00",
        },
        {
          id: 3,
          number: "p2022061000003",
          status: "in_progress",
          status_display: "生产中",
          material_number: "P002",
          material_name: "轴承",
          total_quantity: 400,
          completed_quantity: 80,
          completed_progress: "20%",
          start_time: "2022-06-12 00:00:00",
          end_time: "2022-06-12 00:00:00",
        },
        {
          id: 4,
          number: "p2022061000004",
          status: "in_progress",
          status_display: "生产中",
          material_number: "P002",
          material_name: "轴承",
          total_quantity: 200,
          completed_quantity: 100,
          completed_progress: "50%",
          start_time: "2022-06-12 00:00:00",
          end_time: "2022-06-12 00:00:00",
        },
        {
          id: 4,
          number: "p2022061000005",
          status: "in_progress",
          status_display: "生产中",
          material_number: "P002",
          material_name: "轴承",
          total_quantity: 100,
          completed_quantity: 80,
          completed_progress: "80%",
          start_time: "2022-06-12 00:00:00",
          end_time: "2022-06-12 00:00:00",
        },
      ],
      dataSource: [
        {
          process_name: "退货",
          total_quantity: 100,
          completed_quantity: 90,
          completed_progress: "90%",
        },
        {
          process_name: "车加工",
          total_quantity: 100,
          completed_quantity: 85,
          completed_progress: "85%",
        },
        {
          process_name: "热处理",
          total_quantity: 100,
          completed_quantity: 80,
          completed_progress: "80%",
        },
        {
          process_name: "磨加工",
          total_quantity: 100,
          completed_quantity: 75,
          completed_progress: "75%",
        },
        {
          process_name: "抛光",
          total_quantity: 100,
          completed_quantity: 70,
          completed_progress: "70%",
        },
        {
          process_name: "防锈",
          total_quantity: 100,
          completed_quantity: 50,
          completed_progress: "50%",
        },
      ],
    };
  },
  methods: {
    initData() {
      this.container1 = new Column("container1", {
        data: [
          { name: "退火", quantity: 90 },
          { name: "车加工", quantity: 85 },
          { name: "热处理", quantity: 80 },
          { name: "磨加工", quantity: 75 },
          { name: "抛光", quantity: 70 },
          { name: "防锈", quantity: 50 },
        ],
        xField: "name",
        yField: "quantity",
        label: {},
        height: 200,
      });

      this.container1.render();
    },
  },
  mounted() {
    this.initData();
  },
};
</script>

<style scoped>
.title {
  font-size: 24px;
  font-weight: bold;
  color: #1890ff;
}
</style>

<style lang="less" scoped>
.smallCard {
  width: 50%;
  text-align: center;
  box-shadow: 0 0 0 #888888;
}
.chartTitle {
  font-size: 14px;
  font-weight: bold;
}
.number {
  font-size: 24px;
  height: 50%;
  font-weight: bold;
  display: flex;
  align-items: center;
  justify-content: center;
}
.intro {
  height: 50%;
  font-size: 14px;
  color: #666;
  display: flex;
  align-items: center;
  justify-content: center;
}
.percent {
  height: 45px;
  font-size: 20px;
  text-align: left;
  color: #1890ff;
  &::before {
    content: "占用率:";
    font-size: 12px;
  }
  &::after {
    content: "%";
    font-size: 12px;
  }
}
</style>
