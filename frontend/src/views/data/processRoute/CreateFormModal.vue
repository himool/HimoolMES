<template>
  <div>
    <a-modal
      v-model="visible"
      title="新增工艺路线"
      :width="780"
      :confirmLoading="confirmLoading"
      :destroyOnClose="true"
      :maskClosable="false"
      @cancel="handleCancel"
      @ok="handleConfirm"
    >
      <a-form :form="dataForm" :label-col="{ span: 6 }" :wrapper-col="{ span: 18 }">
        <a-row>
          <a-col :span="12">
            <a-form-item label="物料">
              <material-select
                v-decorator="[
                  'material',
                  {
                    rules: [{ required: true, message: '请选择物料' }],
                  },
                ]"
                :allowClear="true"
              />
            </a-form-item>
          </a-col>
          <a-col :span="12">
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
          </a-col>
          <a-col :span="24">
            <a-form-item label="工序" :label-col="{ span: 3 }" :wrapper-col="{ span: 21 }">
              <process-table
                v-decorator="[
                  'process_items',
                  {
                    rules: [{ required: true, message: '请添加工序' }],
                  },
                ]"
              />
            </a-form-item>
          </a-col>
        </a-row>
      </a-form>
    </a-modal>
  </div>
</template>

<script>
import { processRouteCreate } from "@/apis/production";

export default {
  components: {
    MaterialSelect: () => import("@/components/MaterialSelect"),
    ProcessTable: () => import("@/components/ProcessTable"),
  },
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
          processRouteCreate(values)
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
