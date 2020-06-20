<template>
    <div>
        <Row>
        <chart-all style="height: 320px;" :value="my_data_classheight" text="测试echars"></chart-all>
        </Row>
        <Row >
          <Col span=""><Card>
             <Table  :columns="columns1" :data="data2"></Table>
          </Card></Col>
          
        </Row>
    </div>
</template>
<script>
import{ classheight, }from '@/mock/ranking'
import { ChartAll } from '@/components/charts'
export default {
    components:{
        ChartAll,
        },
     data(){
        return{
        my_data_classheight:{},
        columns1: [
                    {
                        title: '排名',
                        key: 'year',
                         "fixed": "left",
                        "width": 100
                    },
                    
                     {
                        "title": "姓名",
                        "key": "numbers",
                        "width": 100,
                        "sortable": true,
                        filters: [
                            {
                                label: 'Greater than 4000',
                                value: 1
                            },
                            {
                                label: 'Less than 4000',
                                value: 2
                            }
                        ],
                        filterMultiple: false,
                        filterMethod (value, row) {
                            if (value === 1) {
                                return row.numbers > 4000;
                            } else if (value === 2) {
                                return row.numbers < 4000;
                            }
                        }
                    },
                   
                    {
                        title: '胜',
                        key: 'mz',
                        "width": 100,
                        "sortable": true,
                    },
                    {
                        title: '负',
                        key: 'cs',
                        "width": 100,
                        "sortable": true,
                    },
                    {
                        title: '胜率',
                        key: 'sfmz',
                        "width": 100,
                        "sortable": true,
                    },
                    {
                        title: '胜场差',
                        key: 'sfcs',
                        "width": 100,
                        "sortable": true,
                    },
                    {
                        title: '联盟',
                        key: 'fqmz',
                        "width": 100,
                        "sortable": true,
                    },
                    {
                        title: '主场',
                        key: 'fqcs',
                        "width": 100,
                        "sortable": true,
                    },
                    {
                        title: '客场',
                        key: 'jg',
                        "width": 100,
                        "sortable": true,
                    },
                    {
                        title: '最近10场',
                        key: 'fs',
                        "width": 100,
                        "sortable": true,
                    },
                    {
                        title: '连续成绩',
                        key: 'lb',
                        "width": 100,
                        "sortable": true,
                    },
                    {
                        title: '得分/场',
                        key: 'zg',
                        "width": 100,
                        "sortable": true,
                    },
                    {
                        title: '均场失分',
                        key: 'qd',
                        "width": 100,
                        "sortable": true,
                    },
                    {
                        title: '差距',
                        key: 'gm',
                        "width": 100,
                        "sortable": true,
                    },
                    
                ],
                data2: [
                    {
                    year:'01',
                    numbers:'密尔沃基 雄鹿',
                    mz:'60',
                    cs:'22',
                    sfmz:'73.2',
                    sfcs:'0',
                    fqmz:'40-12',
                    fqcs:'33-8',
                    jg:'27-14',
                    fs:'7-3',
                    lb:'负1',
                    zg:'118.1',
                    qd:'109.3',
                   gm:'8.8'
                    },
                   {
                    year:'02',
                    numbers:'多伦多 猛龙',
                    mz:'58',
                    cs:'22',
                    sfmz:'73.2',
                    sfcs:'0',
                    fqmz:'40-12',
                    fqcs:'33-8',
                    jg:'27-14',
                    fs:'7-3',
                    lb:'负1',
                    zg:'118.1',
                    qd:'109.3',
                   gm:'8.8'
                    },
                    {
                    year:'03',
                    numbers:'费城 76人',
                    mz:'51',
                    cs:'22',
                    sfmz:'73.2',
                    sfcs:'0',
                    fqmz:'40-12',
                    fqcs:'33-8',
                    jg:'27-14',
                    fs:'7-3',
                    lb:'负1',
                    zg:'118.1',
                    qd:'109.3',
                   gm:'8.8'
                    },
                    {
                    year:'04',
                    numbers:'波士顿 凯尔特人',
                    mz:'51',
                    cs:'22',
                    sfmz:'73.2',
                    sfcs:'0',
                    fqmz:'40-12',
                    fqcs:'33-8',
                    jg:'27-14',
                    fs:'7-3',
                    lb:'负1',
                    zg:'118.1',
                    qd:'109.3',
                   gm:'8.8'
                    },
                ]
            
        }
    },
     mounted(){
        this.my_data_classheight = classheight
        } 
}
</script>

