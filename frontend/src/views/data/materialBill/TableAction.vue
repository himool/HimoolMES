<template>
  <div>
    <a-button-group>
      <a-button icon="edit" size="small" @click="updateModalVisible = true">编辑</a-button>
      <a-popconfirm title="确定删除吗" @confirm="destroy">
        <a-button type="danger" icon="delete" size="small">删除</a-button>
      </a-popconfirm>
    </a-button-group>

    <update-form-modal
      v-model="updateModalVisible"
      :dataItem="dataItem"
      @update="update"
      @cancel="updateModalVisible = false"
    />
  </div>
</template>

<script>
import { materialDestroy } from "@/apis/material";

export default {
  components: {
    UpdateFormModal: () => import("./UpdateFormModal"),
  },
  props: ["dataItem"],
  data() {
    return {
      updateModalVisible: false,
    };
  },
  methods: {
    update(item) {
      this.$emit("update", item);
    },
    destroy() {
      materialDestroy({ id: this.dataItem.id }).then(() => {
        this.$message.success("删除成功");
        this.$emit("destroy", this.dataItem);
      });
    },
  },
};
</script>

<style scoped></style>
