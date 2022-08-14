<template>
  <div>
    <a-modal
      v-model="visible"
      :width="920"
      :confirmLoading="loading"
      :maskClosable="false"
      @cancel="cancel"
      @ok="confirm"
    >
      <div slot="title">{{ form.id ? "编辑巡检任务" : "新增质检" }}</div>
      <div>
        <a-form-model ref="form" :model="form" :rules="rules" :label-col="{ span: 8 }" :wrapper-col="{ span: 16 }">
          <a-row>
            <a-col :span="8">
              <a-form-model-item prop="1" label="质检总数量">
                <a-input v-model="form.a" allowClear />
              </a-form-model-item>
            </a-col>
            <a-col :span="8">
              <a-form-model-item prop="2" label="良品数量">
                <a-input v-model="form.b" allowClear />
              </a-form-model-item>
            </a-col>
            <a-col :span="8">
              <a-form-model-item prop="3" label="返工数量">
                <a-input v-model="form.c" allowClear />
              </a-form-model-item>
            </a-col>
            <a-col :span="8">
              <a-form-model-item prop="4" label="报废数量">
                <a-input v-model="form.d" allowClear />
              </a-form-model-item>
            </a-col>
            <a-col :span="8">
              <a-form-model-item prop="5" label="备注">
                <a-input v-model="form.e" allowClear />
              </a-form-model-item>
            </a-col>
          </a-row>

          <div style="margin-bottom: 12px;">
            <a-button type="primary">添加质检问题记录</a-button>
          </div>
          <a-table :columns="columns" :data-source="form.bom_items" :pagination="false">
            <template slot="quantity" slot-scope="value">
              <a-input :value="value"></a-input>
            </template>
            <template slot="action" slot-scope="value, item">
              <a-button type="danger" icon="delete" size="small">删除</a-button>
            </template>
          </a-table>
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
          title: "批号",
          dataIndex: "批号",
          fixed: "left",
        },
        {
          title: "所在位置",
          dataIndex: "所在位置",
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
          title: "操作",
          dataIndex: "action",
          fixed: "right",
          width: 256,
          scopedSlots: { customRender: "action" },
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
