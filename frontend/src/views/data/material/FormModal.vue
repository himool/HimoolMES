<template>
  <div>
    <a-modal
      v-model="visible"
      width="750px"
      :confirmLoading="loading"
      :maskClosable="false"
      @cancel="cancel"
      @ok="confirm"
    >
      <div slot="title">{{ form.id ? "编辑物料信息" : "新增物料信息" }}</div>
      <div>
        <a-form-model
          ref="form"
          :model="form"
          :rules="rules"
          :label-col="{ span: 4, md: 8 }"
          :wrapper-col="{ span: 20, md: 16 }"
        >
          <a-row gutter="12">
            <a-divider orientation="left" id="basic-information">
              基本信息
            </a-divider>
            <a-col :span="24" :md="12">
              <a-form-model-item prop="barcode" label="条形码">
                <a-input v-model="form.barcode" />
              </a-form-model-item>
            </a-col>
            <a-col :span="24" :md="12">
              <a-form-model-item prop="number" label="物料编号">
                <a-input v-model="form.number" />
              </a-form-model-item>
            </a-col>
            <a-col :span="24" :md="12">
              <a-form-model-item prop="name" label="物料名称">
                <a-input v-model="form.name" />
              </a-form-model-item>
            </a-col>
            <a-col :span="24" :md="12">
              <a-form-model-item prop="category" label="分类">
                <a-select v-model.number="form.category" style="width: 100%" :allowClear="true">
                  <a-select-option v-for="item of $parent.categoryItems" :key="item.id" :value="item.id"
                    >{{ item.name }}
                  </a-select-option>
                </a-select>
              </a-form-model-item>
            </a-col>
            <a-col :span="24" :md="12">
              <a-form-model-item prop="unit" label="单位">
                <a-select v-model.number="form.unit" :allowClear="true">
                  <a-select-option v-for="item of $parent.unitItems" :key="item.id" :value="item.id"
                    >{{ item.name }}
                  </a-select-option>
                </a-select>
              </a-form-model-item>
            </a-col>
            <a-col :span="24" :md="12">
              <a-form-model-item prop="spec" label="规格">
                <a-input v-model="form.spec" />
              </a-form-model-item>
            </a-col>
            <a-col :span="24" :md="12">
              <a-form-model-item prop="shelf_life_days" label="保质期天数">
                <a-input v-model="form.shelf_life_days" suffix="天" />
              </a-form-model-item>
            </a-col>
            <a-col :span="24" :md="12">
              <a-form-model-item prop="shelf_life_warning_days" label="保质期预警天数">
                <a-input v-model="form.shelf_life_warning_days" suffix="天" />
              </a-form-model-item>
            </a-col>
            <a-col :span="24" :md="12">
              <a-form-model-item prop="enable_batch_control" label="启用批次控制">
                <a-switch checked-children="启用" un-checked-children="禁用" v-model="form.enable_batch_control" />
              </a-form-model-item>
            </a-col>
            <a-col :span="24" :md="12">
              <a-form-model-item prop="is_active" label="状态">
                <a-select v-model="form.is_active" style="width: 100%;">
                  <a-select-option :value="true">激活</a-select-option>
                  <a-select-option :value="false">冻结</a-select-option>
                </a-select>
              </a-form-model-item>
            </a-col>
            <a-col :span="24" :md="12">
              <a-form-model-item prop="remark" label="备注">
                <a-input v-model="form.remark" allowClear />
              </a-form-model-item>
            </a-col>
          </a-row>
          <a-row gutter="12">
            <a-divider orientation="left" id="inventory-warning">
              库存预警
            </a-divider>
            <a-col :span="24" :md="12">
              <a-form-model-item prop="enable_inventory_warning" label="启用库存警告">
                <a-switch checked-children="启用" un-checked-children="禁用" v-model="form.enable_inventory_warning" />
              </a-form-model-item>
            </a-col>
            <a-col :span="24" :md="12">
              <a-form-model-item prop="inventory_upper" label="库存上限">
                <a-input-number v-model="form.inventory_upper" style="width: 100%" />
              </a-form-model-item>
            </a-col>
            <a-col :span="24" :md="12">
              <a-form-model-item prop="inventory_lower" label="库存下限">
                <a-input-number v-model="form.inventory_lower" style="width: 100%" />
              </a-form-model-item>
            </a-col>
          </a-row>
        </a-form-model>
      </div>
    </a-modal>
  </div>
</template>

<script>
// import Cookies from "js-cookie";
// import { goodsInformationCreate, goodsInformationUpdate } from "@/api/goods";
// function getBase64(file) {
//   return new Promise((resolve, reject) => {
//     const reader = new FileReader();
//     reader.readAsDataURL(file);
//     reader.onload = () => resolve(reader.result);
//     reader.onerror = (error) => reject(error);
//   });
// }

export default {
  props: ["visible", "form"],
  model: { prop: "visible", event: "cancel" },
  data() {
    return {
      loading: false,
      rules: {
        name: [{ required: true, message: "请输入物料名称", trigger: "change" }],
        number: [{ required: true, message: "请输入物料编号", trigger: "change" }],
      },
    };
  },
  methods: {
    confirm() {
      // let image_items = this.form.image_items.map((item) => {
      //   return item.response.id;
      // });
      // let inventory_items = this.warehouseItems.map((item) => {
      //   return {
      //     warehouse: item.id,
      //     initial_quantity: item.initial_quantity,
      //     batch_items: this.form.enable_batch_control ? item.batch_items : [],
      //   };
      // });
      // let formatData = {
      //   ...this.form,
      //   ...{
      //     goods_images: image_items,
      //     inventory_items,
      //   },
      // };
      // console.log(formatData);
      // this.$refs.form.validate((valid) => {
      //   if (valid) {
      //     this.loading = true;
      //     let func = this.form.id ? goodsInformationUpdate : goodsInformationCreate;
      //     func(formatData)
      //       .then((data) => {
      //         this.$message.success(this.form.id ? "修改成功" : "新增成功");
      //         this.$emit(this.form.id ? "update" : "create", data);
      //         this.cancel();
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
