<template>
  <div>
    <Card>
      <Button style="margin: 20px 0;" type="primary" @click="add">新增动作类别</Button>
      <tables ref="tables" editable searchable search-place="top" v-model="actiionlist.tableData.actions" :columns="actiionlist.columns" />
      <Button style="margin: 10px 0;" type="primary" @click="exportExcel">导出动作类别信息</Button>
    </Card>
  </div>
</template>

<script>
import Tables from '_c/tables'
import { getActionList } from '@/api/action'
import { getToken } from '@/libs/util'
import axios from 'axios'
import qs from 'qs'

export default {
  name: 'test_page',
  components: {
    Tables
  },
  data () {
    var token=getToken();
    return {
        actiionlist: {
            columns: [
            {title: '动作名称', key: 'name', sortable: true},
            {title: '添加时间', key: 'created_at'},
            {
                    title: '操作',
                    key: 'handle',
                    options: [],
                    button: [
                         (h, params, vm) => {
                            return h('Poptip', {
                              props: {
                                confirm: true,
                                title: '你确定吗?'
                              },
                              on: {
                                'on-ok': () => {
                                     location.href='../coach/action_info_page?action_code='+params.row.id;
                                }
                              }
                            }, [
                              h('Button',{
                                    props: {
                                        type: 'success',
                                        size: 'small',
                                        disabled: false
                                    },
                                    style: {
                                        marginRight: '5px'
                                    }
                                }, '详情')
                            ])
                          },
                    ]
                }
            ],
        tableData: []
        }
    };
  },
  methods: {
    handleDelete (params) {
      console.log(params)
    },
    exportExcel () {
      this.$refs.tables.exportCsv({
        filename: `table-${(new Date()).valueOf()}.csv`
      })
    },
    add () {
        location.href='../coach/action_add_page';
    }
  },
  mounted () {
    var token=getToken();
    getActionList(token).then(res => {
      this.actiionlist.tableData = res.data;
      console.log('actiionlist',res.data);
    })
  }
}
</script>

<style>

</style>