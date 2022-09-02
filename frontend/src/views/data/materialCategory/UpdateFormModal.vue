<template>
  <div>
    <a-modal
      :visible="visible"
      title="编辑物料分类"
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
                initialValue: dataItem.name,
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
                initialValue: dataItem.remark,
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
import { materialCategoryUpdate } from "@/apis/material";

export default {
  props: ["visible", "dataItem"],
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
          materialCategoryUpdate({ id: this.dataItem.id, ...values })
            .then((data) => {
              this.$emit("update", data);
              this.$message.success("更新成功");
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
