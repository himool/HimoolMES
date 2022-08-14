<template>
  <div>
    <a-row :gutter="[8, 8]">
      <a-col :span="6">
        <a-card :bordered="false">
          <div style="text-align: center">
            <div class="title">7</div>
            <div class="value">维护中设备</div>
          </div>
        </a-card>
      </a-col>
      <a-col :span="6">
        <a-card :bordered="false">
          <div style="text-align: center">
            <div class="title">2</div>
            <div class="value">待响应维护请求</div>
          </div>
        </a-card>
      </a-col>
      <a-col :span="6">
        <a-card :bordered="false">
          <div style="text-align: center">
            <div class="title">5</div>
            <div class="value">本周定期保养设备</div>
          </div>
        </a-card>
      </a-col>
      <a-col :span="6">
        <a-card :bordered="false">
          <div style="text-align: center">
            <div class="title">3</div>
            <div class="value">已完成故障维修</div>
          </div>
        </a-card>
      </a-col>
    </a-row>

    <a-row :gutter="[8, 8]">
      <a-col :span="12">
        <a-card :bordered="false" size="small" style="height: 300px">
          <template slot="title">运行时间分析</template>
          <div id="container1" />
        </a-card>
      </a-col>
      <a-col :span="12">
        <a-card :bordered="false" size="small" style="height: 300px">
          <template slot="title">设备故障次数</template>
          <template slot="extra">
            <a-select size="small" placeholder="设备组" style="width: 200px; margin: -2px 0" />
          </template>
          <div id="container2" />
        </a-card>
      </a-col>
    </a-row>

    <a-row :gutter="[8, 8]">
      <a-col :span="24">
        <a-card :bordered="false" size="small" style="height: 310px">
          <template slot="title">设备状态</template>

          <div>
            <a-table
              size="small"
              :columns="columns"
              :dataSource="dataSource"
              :pagination="false"
              :scroll="{ y: 200 }"
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
import { Column } from "@antv/g2plot";

export default {
  data() {
    return {
      container1: null,
      container2: null,

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
          dataIndex: "device_number",
        },
        {
          title: "设备名称",
          dataIndex: "device_name",
        },
        {
          title: "设备状态",
          dataIndex: "device_status",
        },
        {
          title: "开始时间",
          dataIndex: "start_time",
        },
        {
          title: "结束时间",
          dataIndex: "end_time",
        },
        {
          title: "备注",
          dataIndex: "remark",
        },
      ],
      dataSource: [
        {
          id: 1,
          device_number: "D001",
          device_name: "设备1",
          device_status: "启用",
          start_time: "2022-05-20 09:00:00",
          end_time: "2022-06-10 21:00:00",
          remark: "",
        },
        {
          id: 2,
          device_number: "D002",
          device_name: "设备2",
          device_status: "启用",
          start_time: "2022-05-20 09:00:00",
          end_time: "2022-06-05 21:00:00",
          remark: "",
        },
        {
          id: 3,
          device_number: "D003",
          device_name: "设备3",
          device_status: "关闭",
          start_time: "2022-06-10 09:00:00",
          end_time: "2022-06-20 21:00:00",
          remark: "",
        },
        {
          id: 4,
          device_number: "D004",
          device_name: "设备4",
          device_status: "启用",
          start_time: "2022-04-20 09:00:00",
          end_time: "2022-06-20 21:00:00",
          remark: "",
        },
        {
          id: 5,
          device_number: "D005",
          device_name: "设备5",
          device_status: "关闭",
          start_time: "2022-03-20 09:00:00",
          end_time: "2022-06-20 21:00:00",
          remark: "",
        },
      ],
    };
  },
  methods: {
    initData() {
      this.container1 = new Column("container1", {
        data: [
          { type: "运行", date: "设备1", quantity: 33 },
          { type: "运行", date: "设备2", quantity: 23 },
          { type: "运行", date: "设备3", quantity: 12 },
          { type: "运行", date: "设备4", quantity: 40 },
          { type: "运行", date: "设备5", quantity: 10 },
          { type: "故障", date: "设备1", quantity: 11 },
          { type: "故障", date: "设备2", quantity: 0 },
          { type: "故障", date: "设备3", quantity: 10 },
          { type: "故障", date: "设备4", quantity: 0 },
          { type: "故障", date: "设备5", quantity: 12 },
          { type: "待机", date: "设备1", quantity: 56 },
          { type: "待机", date: "设备2", quantity: 77 },
          { type: "待机", date: "设备3", quantity: 78 },
          { type: "待机", date: "设备4", quantity: 60 },
          { type: "待机", date: "设备5", quantity: 78 },
        ],
        xField: "date",
        yField: "quantity",
        seriesField: "type",
        label: {},
        meta: { date: { alias: "日期" }, quantity: { alias: "入库数量" } },
        height: 220,
        isStack: true,
      });

      this.container2 = new Column("container2", {
        data: [
          { date: "设备1", quantity: 10 },
          { date: "设备2", quantity: 2 },
          { date: "设备3", quantity: 7 },
          { date: "设备4", quantity: 8 },
          { date: "设备5", quantity: 1 },
        ],
        xField: "date",
        yField: "quantity",
        label: {},
        meta: { date: { alias: "日期" }, quantity: { alias: "入库数量" } },
        height: 220,
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
