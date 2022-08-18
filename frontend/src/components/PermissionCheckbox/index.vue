<template>
  <a-spin :spinning="dataLoading">
    <a-descriptions layout="vertical" size="small" bordered>
      <a-descriptions-item v-for="item in dataItems" :key="item.id" :span="3">
        <template slot="label">
          <a-checkbox
            :checked="
              checkboxStatus[item.id] &&
                checkboxStatus[item.id].anyChecked &&
                checkboxStatus[item.id] &&
                checkboxStatus[item.id].allChecked
            "
            :indeterminate="
              checkboxStatus[item.id] &&
                checkboxStatus[item.id].anyChecked &&
                checkboxStatus[item.id] &&
                !checkboxStatus[item.id].allChecked
            "
            @change="checkAll(item)"
          >
            {{ item.name }}
          </a-checkbox>
        </template>
        <a-checkbox-group
          :value="checkedValues"
          @change="(values) => changePermission(item, values)"
          style="width: 100%"
        >
          <a-row>
            <a-col v-for="permissionItem in item.permission_items" :key="permissionItem.id" :span="12">
              <a-checkbox :value="permissionItem.id">{{ permissionItem.name }}</a-checkbox>
            </a-col>
          </a-row>
        </a-checkbox-group>
      </a-descriptions-item>
    </a-descriptions>
  </a-spin>
</template>

<script>
import { permissionGroupList } from "@/apis/system";

export default {
  props: ["value"],
  model: { prop: "value", event: "change" },
  data() {
    return {
      checkedValues: [],
      dataItems: [],
      dataLoading: false,
      checkboxStatus: {},
    };
  },
  methods: {
    checkAll(permissionGroupItem) {
      if (this.checkboxStatus[permissionGroupItem.id]?.anyChecked) {
        if (this.checkboxStatus[permissionGroupItem.id]?.allChecked) {
          this.changePermission(permissionGroupItem, []);
        } else {
          this.changePermission(
            permissionGroupItem,
            permissionGroupItem.permission_items.map((item) => item.id)
          );
        }
      } else {
        this.changePermission(
          permissionGroupItem,
          permissionGroupItem.permission_items.map((item) => item.id)
        );
      }
    },
    changePermission(permissionGroupItem, checkedPermissions) {
      const permissionSet = new Set(this.checkedValues);

      for (const permissionItem of permissionGroupItem.permission_items) {
        permissionSet.delete(permissionItem.id);
      }

      for (const permissionId of checkedPermissions) {
        permissionSet.add(permissionId);
      }

      const status = {};
      for (const groupItem of this.dataItems) {
        status[groupItem.id] = { anyChecked: false, allChecked: true };
        for (const permissionItem of groupItem.permission_items) {
          if (permissionSet.has(permissionItem.id)) {
            status[groupItem.id].anyChecked = true;
          } else {
            status[groupItem.id].allChecked = false;
          }
        }
      }

      this.checkboxStatus = status;
      this.checkedValues = Array.from(permissionSet);
      this.$emit("change", this.checkedValues);
    },
  },
  mounted() {
    this.dataLoading = true;
    permissionGroupList()
      .then((data) => {
        this.dataItems = data;
        if (this.value !== undefined) {
          const permissionSet = new Set(this.value);

          const status = {};
          for (const groupItem of this.dataItems) {
            status[groupItem.id] = { anyChecked: false, allChecked: true };
            for (const permissionItem of groupItem.permission_items) {
              if (permissionSet.has(permissionItem.id)) {
                status[groupItem.id].anyChecked = true;
              } else {
                status[groupItem.id].allChecked = false;
              }
            }
          }

          this.checkboxStatus = status;
          this.checkedValues = Array.from(permissionSet);
        }
      })
      .finally(() => (this.dataLoading = false));
  },
};
</script>

<style scoped></style>
