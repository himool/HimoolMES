<template>
  <div>
    <a-modal
      :visible="visible"
      title="编辑物料"
      :confirmLoading="confirmLoading"
      :destroyOnClose="true"
      :maskClosable="false"
      @cancel="handleCancel"
      @ok="handleConfirm"
    >
      <a-form :form="dataForm" :label-col="{ span: 6 }" :wrapper-col="{ span: 18 }">
        <a-form-item label="编号">
          <a-input
            v-decorator="[
              'number',
              {
                initialValue: dataItem.number,
                rules: [
                  { required: true, message: '请输入物料编号' },
                  { max: 32, message: '超出最大长度(32)' },
                ],
              },
            ]"
            :allowClear="true"
          />
        </a-form-item>
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
        <a-form-item label="类型">
          <a-radio-group
            v-decorator="[
              'type',
              {
                initialValue: dataItem.type,
                rules: [{ required: true, message: '请选择物料类型' }],
              },
            ]"
            button-style="solid"
            style="width: 100%; text-align: center;"
          >
            <a-radio-button value="raw_material" style="width: 50%">
              原料
            </a-radio-button>
            <a-radio-button value="finish_product" style="width: 50%">
              成品
            </a-radio-button>
          </a-radio-group>
        </a-form-item>
        <a-form-item label="分类">
          <material-category-select v-decorator="['category', { initialValue: dataItem.category }]" />
        </a-form-item>
        <a-form-item label="规格">
          <a-input
            v-decorator="[
              'spec',
              {
                initialValue: dataItem.spec,
                rules: [{ max: 64, message: '超出最大长度(64)' }],
              },
            ]"
            :allowClear="true"
          />
        </a-form-item>
        <a-form-item label="单位">
          <a-input
            v-decorator="[
              'unit',
              {
                initialValue: dataItem.unit,
                rules: [{ max: 64, message: '超出最大长度(64)' }],
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
import { materialUpdate } from "@/apis/material";

export default {
  components: {
    MaterialCategorySelect: () => import("@/components/MaterialCategorySelect"),
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
          materialUpdate({ id: this.dataItem.id, ...values })
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
