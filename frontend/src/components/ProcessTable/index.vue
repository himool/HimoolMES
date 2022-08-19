<template>
  <div>
    <a-table :columns="columns" :data-source="dataItems" size="small" :pagination="false">
      <template slot="name" slot-scope="value, item">
        <a-input v-model="item.name" size="small" @change="change" />
      </template>
      <template slot="remark" slot-scope="value, item">
        <a-input v-model="item.remark" size="small" @change="change" />
      </template>
      <template slot="action" slot-scope="value, item, index">
        <a-button-group size="small">
          <a-button icon="up" :disabled="index === 0" @click="upItem(index)" />
          <a-button icon="down" :disabled="index + 1 === dataItems.length" @click="downItem(index)" />
          <a-button type="danger" icon="delete" size="small" @click="removeItem(index)"></a-button>
        </a-button-group>
      </template>
      <template slot="footer">
        <a-button type="dashed" icon="plus" style="width: 100%" @click="addItem">新增工序</a-button>
      </template>
    </a-table>
  </div>
</template>

<script>
export default {
  props: ["value"],
  model: { prop: "value", event: "change" },
  data() {
    return {
      columns: [
        {
          title: "序号",
          dataIndex: "index",
          customRender: (_value, _item, index) => index + 1,
        },
        {
          title: "名称",
          dataIndex: "name",
          scopedSlots: { customRender: "name" },
        },
        {
          title: "备注",
          dataIndex: "remark",
          scopedSlots: { customRender: "remark" },
        },
        {
          title: "操作",
          dataIndex: "action",
          scopedSlots: { customRender: "action" },
        },
      ],
      dataItems: [],
    };
  },
  methods: {
    addItem() {
      this.dataItems.push({ name: "", remark: "" });
    },
    upItem(index) {
      if (index !== 0) {
        const dataItems = [...this.dataItems];
        const targetItem = dataItems[index];
        dataItems.splice(index, 1);
        dataItems.splice(index - 1, 0, targetItem);
        this.dataItems = dataItems;
        this.change();
      }
    },
    downItem(index) {
      if (index + 1 < this.dataItems.length) {
        const dataItems = [...this.dataItems];
        const targetItem = dataItems[index];
        dataItems.splice(index, 1);
        dataItems.splice(index + 1, 0, targetItem);
        this.dataItems = dataItems;
        this.change();
      }
    },
    removeItem(index) {
      this.dataItems.splice(index, 1);
      this.change();
    },
    change() {
      const dataItems = [];
      for (let index in this.dataItems) {
        let item = this.dataItems[index];
        if (item.name && item.name.length > 0) {
          item["index"] = index;
          dataItems.push(item);
        }
      }
      console.log("change", dataItems);
      this.$emit("change", dataItems);
    },
  },
  mounted() {
    console.log(this.value);
    this.dataItems = this.value || [{ name: "", remark: "" }];
  },
};
</script>

<style scoped></style>
