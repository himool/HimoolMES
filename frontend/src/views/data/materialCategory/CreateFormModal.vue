<template>
  <div>
    <a-modal
      :visible="visible"
      title="新增物料分类"
      :confirmLoading="confirmLoading"
      :destroyOnClose="true"
      :maskClosable="false"
      @cancel="handleCancel"
      @ok="handleConfirm"
    >
      <a-form :form="dataForm" :label-col="{ span: 6 }" :wrapper-col="{ span: 18 }">
        <a-form-item label="名称">
          <a-input
            v-decorator="[
              'name',
              {
                rules: [
                  { required: true, message: '请输入物料名称' },
                  { max: 64, message: '超出最大长度(64)' },
                ],
              },
            ]"
            :allowClear="true"
          />
        </a-form-item>
        <a-form-item label="备注">
          <a-input
            v-decorator="[
              'remark',
              {
                rules: [{ max: 256, message: '超出最大长度(256)' }],
              },
            ]"
            :allowClear="true"
          />
        </a-form-item>
      </a-form>
    </a-modal>
  </div>
</template>

<script>
import { materialCategoryCreate } from "@/apis/material";

export default {
  props: ["visible"],
  model: { prop: "visible", event: "cancel" },
  data() {
    return {
      confirmLoading: false,
      dataForm: null,
    };
  },
  methods: {
    handleConfirm() {
      this.dataForm.validateFields((error, values) => {
        if (error === null) {
          this.confirmLoading = true;
          materialCategoryCreate(values)
            .then((data) => {
              this.$emit("create", data);
              this.$message.success("创建成功");
              this.handleCancel();
            })
            .finally(() => {
              this.confirmLoading = false;
            });
        }
      });
    },
    handleCancel() {
      this.$emit("cancel", false);
    },
  },
  mounted() {
    this.dataForm = this.$form.createForm(this);
  },
};
</script>

<style scoped></style>
