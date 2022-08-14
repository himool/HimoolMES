<template>
  <div>
    <a-modal v-model="visible" :confirmLoading="loading" :maskClosable="false" @cancel="cancel" @ok="confirm">
      <div slot="title">{{ form.id ? "编辑质量巡检" : "新增质量巡检" }}</div>
      <div>
        <a-form-model ref="form" :model="form" :rules="rules" :label-col="{ span: 6 }" :wrapper-col="{ span: 16 }">
          <!-- <a-form-model-item prop="name" label="质量检验单号">
            <a-input />
          </a-form-model-item>
          <a-form-model-item prop="position" label="责任部门">
            <a-input />
          </a-form-model-item>
          <a-form-model-item prop="remark" label="图片">
            <a-upload
              action="https://www.mocky.io/v2/5cc8019d300000980a055e76"
              list-type="picture-card"
              :file-list="fileList"
              @preview="handlePreview"
              @change="handleChange"
            >
              <div v-if="fileList.length < 8">
                <a-icon type="plus" />
                <div class="ant-upload-text">
                  上传
                </div>
              </div>
            </a-upload>
          </a-form-model-item>
          <a-form-model-item prop="standard" label="发生地">
            <a-input />
          </a-form-model-item> -->
          <a-form-model-item prop="status" label="意见">
            <a-input />
          </a-form-model-item>
          <a-form-model-item prop="remark" label="备注">
            <a-input />
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
      fileList: [],
    };
  },
  methods: {
    handleChange({ fileList }) {
      this.fileList = fileList;
    },
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
