export default [
  {
    title: '物料编号',
    dataIndex: 'number',
    sorter: true,
  },
  {
    title: '物料名称',
    dataIndex: 'name',
    sorter: true,
  },
  {
    title: '物料单位',
    dataIndex: 'unit_name',
  },
  {
    title: '操作',
    dataIndex: 'action',
    scopedSlots: { customRender: 'action' },
  },
]