<template>
  <div>
    <a-select
      :value="value"
      :placeholder="placeholder"
      show-search
      allowClear
      :disabled="disabled"
      :filter-option="false"
      style="width: 100%;"
      @search="search"
      @change="change"
      @focus="focus"
      @popupScroll="scroll"
    >
      <div v-if="dataLoading" slot="notFoundContent" style="text-align: center;">
        <a-spin size="small" />
      </div>
      <a-select-option v-for="item in dataItems" :key="item.id" :value="item.id" :item="item">
        {{ item.name }}
      </a-select-option>
    </a-select>
  </div>
</template>

<script>
import { materialOption } from "@/apis/option";

export default {
  props: ["value", "defaultItem", "disabled", "placeholder"],
  model: { prop: "value", event: "change" },
  data() {
    return {
      searchForm: { search: "", page: 1 },

      dataItems: [],
      dataLoading: false,
      dataCount: 0,

      timeout: null,
    };
  },
  methods: {
    list() {
      if (this.searchForm.page == 1) this.dataItems = [];

      this.dataLoading = true;
      materialOption(this.searchForm)
        .then((data) => {
          this.dataCount = data.count;
          this.dataItems.push(...data.results);
        })
        .finally(() => {
          this.dataLoading = false;
        });
    },
    change(value) {
      this.$emit("change", value);
    },
    focus() {
      this.searchForm.page = 1;
      this.list();
    },
    scroll({ target }) {
      if (this.dataLoading) return;
      if (target.scrollTop + target.offsetHeight >= target.scrollHeight) return;
      if (this.dataItems.length >= this.dataCount) return;

      this.searchForm.page += 1;
      this.list();
    },
    search(value) {
      this.searchForm.search = value;
      if (this.timeout) {
        clearTimeout(this.timeout);
        this.timeout = null;
      }
      this.timeout = setTimeout(this.list, 300);
    },
  },
  mounted() {
    if (this.defaultItem) {
      this.dataItems = [this.defaultItem];
    }
  },
};
</script>

<style scoped></style>
