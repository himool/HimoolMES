<template>
  <div>
    <a-modal v-model="visible" :confirmLoading="loading" :maskClosable="false" @cancel="cancel" @ok="confirm">
      <div slot="title">{{ form.id ? "编辑巡检任务" : "新增巡检任务" }}</div>
      <div>
        <a-form-model ref="form" :model="form" :rules="rules" :label-col="{ span: 6 }" :wrapper-col="{ span: 16 }">
          <a-form-model-item prop="device" label="设备">
            <a-select style="width: 100%"></a-select>
          </a-form-model-item>
          <a-form-model-item prop="position" label="检查部位">
            <a-input v-model="form.position" allowClear />
          </a-form-model-item>
          <a-form-model-item prop="standard" label="标准及评定基准">
            <a-input v-model="form.standard" allowClear />
          </a-form-model-item>
          <a-form-model-item prop="execution_cycle" label="执行周期">
            <a-input v-model="form.execution_cycle" allowClear />
          </a-form-model-item>
          <a-form-model-item prop="execution_sequence" label="执行顺序">
            <a-input v-model="form.execution_sequence" allowClear />
          </a-form-model-item>
          <a-form-model-item prop="remark" label="备注">
            <a-input v-model="form.remark" allowClear />
          </a-form-model-item>
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
