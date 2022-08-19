<template>
  <div>
    <a-modal
      v-model="visible"
      title="编辑BOM"
      :confirmLoading="confirmLoading"
      :destroyOnClose="true"
      :maskClosable="false"
      @cancel="handleCancel"
      @ok="handleConfirm"
    >
      <a-form :form="dataForm" :label-col="{ span: 6 }" :wrapper-col="{ span: 18 }">
        <a-form-item label="成品">
          <material-select
            v-decorator="[
              'finish_product',
              {
                initialValue: dataItem.finish_product,
                rules: [{ required: true, message: '请选择成品' }],
              },
            ]"
            :defaultItem="dataItem.finish_product_item"
            :allowClear="true"
          />
        </a-form-item>
        <a-form-item label="原料">
          <material-select
            v-decorator="[
              'raw_material',
              {
                initialValue: dataItem.raw_material,
                rules: [{ required: true, message: '请选择原料' }],
              },
            ]"
            :defaultItem="dataItem.raw_material_item"
            :allowClear="true"
          />
        </a-form-item>
        <a-form-item label="数量">
          <a-input-number
            v-decorator="[
              'quantity',
              {
                initialValue: dataItem.quantity,
                rules: [{ required: true, message: '请输入数量' }],
              },
            ]"
            style="width: 100%"
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
import { materialBillUpdate } from "@/apis/material";

export default {
  components: {
    MaterialSelect: () => import("@/components/MaterialSelect"),
  },
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
          materialBillUpdate({ id: this.dataItem.id, ...values })
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
