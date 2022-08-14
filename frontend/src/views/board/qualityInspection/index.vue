<template>
  <div>
    <a-row :gutter="[8, 8]"> 
      <a-col :span="8">
        <a-card :bordered="false" size="small" :body-style="{ padding: '8px 0px' }" style="overflow: hidden">
          <div slot="title">
            <img :src="image3" width="16" height="16" style="margin-top: -2px" />
            <span style="margin-left: 8px">当日合格率</span>
          </div>

          <div style="height: 140px; text-align: center">
            <a-card-grid class="smallCard" :hoverable="false">
              <div style="margin-top: 24px">
                <span class="number">
                  <span style="color: #bae637">34</span>/100
                </span>
                <span class="intro">合格数量</span>
              </div>
            </a-card-grid>
            <a-card-grid class="smallCard" :hoverable="false">
              <a-progress type="circle" :percent="34" strokeColor="#bae637" :width="90" />
            </a-card-grid>
          </div>
        </a-card>
      </a-col>
      <a-col :span="8">
        <a-card :bordered="false" size="small" :body-style="{ padding: '8px 0px' }" style="overflow: hidden">
          <div slot="title">
            <img :src="image1" width="16" height="16" style="margin-top: -2px" />
            <span style="margin-left: 8px">当日不良品数量</span>
          </div>

          <div style="height: 140px; text-align: center">
            <a-card-grid class="smallCard" :hoverable="false">
              <div style="margin-top: 24px">
                <span class="number">
                  <span style="color: #fa8c16">23</span>/100
                </span>
                <span class="intro">不良品数量</span>
              </div>
            </a-card-grid>
            <a-card-grid class="smallCard" :hoverable="false">
              <a-progress type="circle" :percent="23" strokeColor="#fa8c16" :width="90" />
            </a-card-grid>
          </div>
        </a-card>
      </a-col>
      <a-col :span="8">
        <a-card :bordered="false" size="small" :body-style="{ padding: '8px 0px' }" style="overflow: hidden">
          <div slot="title">
            <img :src="image2" width="16" height="16" style="margin-top: -2px" />
            <span style="margin-left: 8px">当日报废数量</span>
          </div>

          <div style="height: 140px; text-align: center">
            <a-card-grid class="smallCard" :hoverable="false">
              <div style="margin-top: 24px">
                <span class="number">
                  <span style="color: #f5222d">13</span>/100
                </span>
                <span class="intro">报废数量</span>
              </div>
            </a-card-grid>
            <a-card-grid class="smallCard" :hoverable="false">
              <a-progress type="circle" :percent="13" strokeColor="#f5222d" :width="90" />
            </a-card-grid>
          </div>
        </a-card>
      </a-col>
    </a-row>

    <a-row :gutter="[8, 8]">
      <a-col :span="12">
        <a-card :bordered="false" size="small" style="height: 260px">
          <template slot="title">质量问题分布</template>
          <div id="container1" />
        </a-card>
      </a-col>
      <a-col :span="12">
        <a-card :bordered="false" size="small" style="height: 260px">
          <template slot="title">生产质检合格数量</template>
          <template slot="extra">
            <a-select size="small" placeholder="设备" style="width: 200px; margin: -2px 0" />
          </template>
          <div id="container2" />
        </a-card>
      </a-col>
    </a-row>

    <a-row :gutter="[8, 8]">
      <a-col :span="24">
        <a-card :bordered="false" size="small" style="height: 260px">
          <template slot="title">工序质检合格率</template>

          <div>
            <a-table
              size="small"
              :columns="columns"
              :dataSource="dataSource"
              :pagination="false"
              :scroll="{ y: 150 }"
            >
              <template slot="chart" slot-scope="value, item">
                <a-progress :percent="item.completed_quantity" />
              </template>
            </a-table>
          </div>
        </a-card>
      </a-col>
    </a-row>
  </div>
</template>

<script>
import { Pie, Line } from "@antv/g2plot";

export default {
  data() {
    return {
      image1: require("./image1.png"),
      image2: require("./image2.png"),
      image3: require("./image3.png"),

      container1: null,
      container2: null,
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
          title: "生产数量",
          dataIndex: "total_quantity",
        },
        {
          title: "合格数量",
          dataIndex: "completed_quantity",
        },
        {
          title: "合格率",
          dataIndex: "completed_progress",
        },
        {
          title: "图表",
          dataIndex: "chart",
          width: 200,
          scopedSlots: { customRender: "chart" },
        },
      ],
      dataSource: [
        {
          process_name: "退货",
          total_quantity: 100,
          completed_quantity: 73,
          completed_progress: "73%",
        },
        {
          process_name: "车加工",
          total_quantity: 100,
          completed_quantity: 80,
          completed_progress: "80%",
        },
        {
          process_name: "热处理",
          total_quantity: 100,
          completed_quantity: 66,
          completed_progress: "66%",
        },
        {
          process_name: "磨加工",
          total_quantity: 100,
          completed_quantity: 58,
          completed_progress: "58%",
        },
        {
          process_name: "抛光",
          total_quantity: 100,
          completed_quantity: 79,
          completed_progress: "79%",
        },
        {
          process_name: "防锈",
          total_quantity: 100,
          completed_quantity: 93,
          completed_progress: "93%",
        },
      ],
    };
  },
  methods: {
    initData() {
      this.container1 = new Pie("container1", {
        data: [
          { name: "容量测试", quantity: 15 },
          { name: "扭力测试", quantity: 20 },
          { name: "拉力压力测试", quantity: 10 },
          { name: "附着性测试", quantity: 20 },
          { name: "组装配对", quantity: 35 },
        ],
        appendPadding: 10,
        angleField: "quantity",
        colorField: "name",
        height: 180,
      });

      this.container2 = new Line("container2", {
        data: [
          { type: "退火", name: "容量测试", quantity: 20 },
          { type: "退火", name: "扭力测试", quantity: 38 },
          { type: "退火", name: "拉力压力测试", quantity: 90 },
          { type: "退火", name: "附着性测试", quantity: 85 },
          { type: "退火", name: "组装配对", quantity: 13 },
          { type: "车加工", name: "容量测试", quantity: 54 },
          { type: "车加工", name: "扭力测试", quantity: 80 },
          { type: "车加工", name: "拉力压力测试", quantity: 65 },
          { type: "车加工", name: "附着性测试", quantity: 28 },
          { type: "车加工", name: "组装配对", quantity: 60 },
          { type: "热处理", name: "容量测试", quantity: 44 },
          { type: "热处理", name: "扭力测试", quantity: 23 },
          { type: "热处理", name: "拉力压力测试", quantity: 76 },
          { type: "热处理", name: "附着性测试", quantity: 37 },
          { type: "热处理", name: "组装配对", quantity: 57 },
          { type: "磨加工", name: "容量测试", quantity: 84 },
          { type: "磨加工", name: "扭力测试", quantity: 33 },
          { type: "磨加工", name: "拉力压力测试", quantity: 96 },
          { type: "磨加工", name: "附着性测试", quantity: 52 },
          { type: "磨加工", name: "组装配对", quantity: 27 },
          { type: "抛光", name: "容量测试", quantity: 12 },
          { type: "抛光", name: "扭力测试", quantity: 69 },
          { type: "抛光", name: "拉力压力测试", quantity: 85 },
          { type: "抛光", name: "附着性测试", quantity: 18 },
          { type: "抛光", name: "组装配对", quantity: 36 },
          { type: "防锈", name: "容量测试", quantity: 14 },
          { type: "防锈", name: "扭力测试", quantity: 62 },
          { type: "防锈", name: "拉力压力测试", quantity: 35 },
          { type: "防锈", name: "附着性测试", quantity: 58 },
          { type: "防锈", name: "组装配对", quantity: 26 },
        ],
        xField: "name",
        yField: "quantity",
        seriesField: "type",
        label: {},
        height: 180,
      });

      this.container1.render();
      this.container2.render();
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
  