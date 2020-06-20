<template>
  <div>
    <Card>
      <Button style="margin: 20px 0;" type="primary" @click="add">新增人员</Button>
      <tables ref="tables" editable searchable search-place="top" v-model="userlist.tableData.users" :columns="userlist.columns" />
      <Button style="margin: 10px 0;" type="primary" @click="exportExcel">导出人员信息</Button>
    </Card>
  </div>
</template>

<script>
import Tables from '_c/tables'
import { getUserList } from '@/api/user'
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
        userlist: {
            columns: [
            {title: '姓名', key: 'name', sortable: true},
            {title: '编号', key: 'serialnum'},
            {title: '角色', key: 'duty'},
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
                                     location.href='../system/user_info_page?user_code='+params.row.serialnum;
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
        location.href='../system/user_add_page';
    }
  },
  mounted () {
    var token=getToken();
    getUserList(token).then(res => {
      this.userlist.tableData = res.data;
      console.log('ok',res.data);
    })
  }
}
</script>

<style>

</style>