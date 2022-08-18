<template>
  <div>
    <a-card title="员工账号">
      <a-row gutter="16">
        <a-col :span="24" :md="8" :xl="6" style="margin-bottom: 12px;">
          <a-input-search v-model="searchForm.search" placeholder="用户名, 名称" allowClear @search="search" />
        </a-col>

        <div style="margin-bottom: 12px; float: right;">
          <a-button type="primary" icon="plus" style="margin: 0 8px;" @click="openFormModal({})">新增账号</a-button>
        </div>
      </a-row>

      <a-row style="margin-top: 12px;">
        <a-table
          rowKey="id"
          size="small"
          :columns="columns"
          :dataSource="items"
          :loading="loading"
          :pagination="pagination"
          @change="tableChange"
        >
          <div slot="is_active" slot-scope="value">
            <a-tag :color="value ? 'green' : 'red'">{{ value ? "激活" : "冻结" }}</a-tag>
          </div>
          <div slot="action" slot-scope="value, item">
            <a-button-group>
              <a-button icon="edit" size="small" @click="openFormModal(item)">编辑</a-button>
              <a-popconfirm title="确定重置吗? 密码: 123456" @confirm="resetPassword(item.id)">
                <a-button size="small" type="primary" icon="sync">重置密码</a-button>
              </a-popconfirm>
              <a-popconfirm title="确定删除吗?" @confirm="destroy(item.id)">
                <a-button type="danger" icon="delete" size="small">删除</a-button>
              </a-popconfirm>
            </a-button-group>
          </div>
        </a-table>
      </a-row>
    </a-card>

    <form-modal v-model="visible" :form="targetItem" @create="create" @update="update" />
  </div>
</template>

<script>
import { userList, userDestroy, userResetPassword } from "@/apis/system";
import { roleOption } from "@/apis/option";

export default {
  components: {
    FormModal: () => import("./FormModal.vue"),
  },
  data() {
    return {
      columns: [
        {
          title: "序号",
          dataIndex: "index",
          customRender: (value, item, index) => index + 1,
        },
        {
          title: "用户名",
          dataIndex: "username",
          sorter: true,
        },
        {
          title: "员工姓名",
          dataIndex: "name",
          sorter: true,
        },
        {
          title: "手机号",
          dataIndex: "phone",
        },
        {
          title: "备注",
          dataIndex: "remark",
        },
        {
          title: "状态",
          dataIndex: "is_active",
          key: "is_active",
          scopedSlots: { customRender: "is_active" },
        },
        {
          title: "操作",
          dataIndex: "action",
          scopedSlots: { customRender: "action" },
          width: "256px",
        },
      ],
      searchForm: { search: "", page: 1, ordering: undefined, page_size: 15 },
      pagination: { current: 1, total: 0, pageSize: 15 },
      loading: false,
      items: [],

      roleItems: [],
      visible: false,
      targetItem: {},
    };
  },
  methods: {
    initialize() {
      this.list();
      roleOption().then((data) => {
        this.roleItems = data;
      });
    },
    list() {
      this.loading = true;
      userList(this.searchForm)
        .then((data) => {
          this.pagination.total = data.count;
          this.items = data.results;
        })
        .finally(() => {
          this.loading = false;
        });
    },
    create(item) {
      this.list();
    },
    update(item) {
      this.list();
    },
    destroy(id) {
      userDestroy({ id }).then(() => {
        this.$message.success("删除成功");
        this.list();
      });
    },
    resetPassword(id) {
      userResetPassword({ id }).then(() => {
        this.$message.success("重置成功");
      });
    },
    search() {
      this.searchForm.page = 1;
      this.pagination.current = 1;
      this.list();
    },
    tableChange(pagination, filters, sorter) {
      this.searchForm.page = pagination.current;
      this.pagination.current = pagination.current;
      this.searchForm.ordering = `${sorter.order == "descend" ? "-" : ""}${sorter.field}`;
      this.list();
    },
    openFormModal(item) {
      this.targetItem = { ...item };
      this.visible = true;
    },
  },
  mounted() {
    this.initialize();
  },
};
</script>

<style scoped></style>
