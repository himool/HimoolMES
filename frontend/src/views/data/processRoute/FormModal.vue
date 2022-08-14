<template>
  <div>
    <a-modal
      v-model="visible"
      :width="720"
      :confirmLoading="loading"
      :maskClosable="false"
      @cancel="cancel"
      @ok="confirm"
    >
      <div slot="title">{{ form.id ? "编辑工艺路线" : "新增工艺路线" }}</div>
      <div>
        <a-form-model ref="form" :model="form" :rules="rules" :label-col="{ span: 6 }" :wrapper-col="{ span: 16 }">
          <a-row>
            <a-col :span="12">
              <a-form-model-item prop="number" label="父级物料">
                <a-select style="width: 100%"></a-select>
              </a-form-model-item>
            </a-col>
            <a-col :span="12">
              <a-form-model-item prop="remark" label="备注">
                <a-input></a-input>
              </a-form-model-item>
            </a-col>
          </a-row>

          <div style="margin-bottom: 12px;">
            <a-button type="primary">添加工艺</a-button>
          </div>
          <a-list :data-source="form.process_items" :bordered="true">
            <a-list-item slot="renderItem" slot-scope="item">
              <a-list-item-meta :title="item.name" />
              <div>
                <a-button-group>
                  <a-button size="small" icon="arrow-up" />
                  <a-button size="small" icon="arrow-down" />
                </a-button-group>
              </div>
            </a-list-item>
          </a-list>
        </a-form-model>
      </div>
    </a-modal>
  </div>
</template>

<script>
// import { deviceCreate, deviceUpdate } from "@/api/manage";

export default {
  props: ["visible", "form"],
  model: { prop: "visible", event: "cancel" },
  data() {
    return {
      rules: {
        number: [{ required: true, message: "请输入编号", trigger: "change" }],
        name: [{ required: true, message: "请输入名称", trigger: "change" }],
      },
      loading: false,
      bomColumns: [
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
          scopedSlots: { customRender: "quantity" },
        },
        {
          title: "操作",
          dataIndex: "action",
          scopedSlots: { customRender: "action" },
          width: "156px",
        },
      ],
    };
  },
  methods: {
    confirm() {
      // this.$refs.form.validate((valid) => {
      //   if (valid) {
      //     this.loading = true;
      //     let func = this.form.id ? deviceUpdate : deviceCreate;
      //     func(this.form)
      //       .then((data) => {
      //         this.$message.success(this.form.id ? "修改成功" : "新增成功");
      //         this.$emit(this.form.id ? "update" : "create", data);
      //         this.cancel();
      //       })
      //       .catch((error) => {
      //         this.$message.error(error.response.data.detial);
      //       })
      //       .finally(() => {
      //         this.loading = false;
      //       });
      //   }
      // });
    },
    cancel() {
      this.$emit("cancel", false);
      this.$refs.form.resetFields();
    },
  },
};
</script>

<style scoped></style>
