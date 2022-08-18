<template>
  <a-select
    :value="value"
    show-search
    allowClear
    :placeholder="placeholder"
    :filter-option="filterOption"
    :disabled="disabled"
    style="width: 100%"
    @change="handleChange"
  >
    <a-select-option v-for="item in dataItems" :key="item.id" :value="item.id" :item="item">
      {{ item.name }}
    </a-select-option>
  </a-select>
</template>

<script>
import { materialCategoryOption } from "@/apis/option";

export default {
  props: ["value", "placeholder", "disabled"],
  model: { prop: "value", event: "change" },
  data() {
    return {
      dataItems: [],
    };
  },
  methods: {
    filterOption(input, option) {
      const item = option.data.attrs.item;
      return item.name.indexOf(input) !== -1;
    },
    handleChange(value) {
      this.$emit("change", value);
    },
  },
  mounted() {
    materialCategoryOption().then((data) => (this.dataItems = data));
  },
};
</script>

<style scoped></style>
