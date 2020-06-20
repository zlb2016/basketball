import Mock from 'mockjs'
import {doCustomTimes}from '@/libs/util'
const Random = Mock.Random
 
export const classheight = {
    title: {
        text: '球队对比数据'
    },
    tooltip: {},
    legend: {
        data: ['老鹰', '勇士']
    },
    radar: {
        // shape: 'circle',
        name: {
            textStyle: {
                color: '#fff',
                backgroundColor: '#999',
                borderRadius: 3,
                padding: [3, 5]
           }
        },
        indicator: [
           { name: '三分', max: 6500},
           { name: '上篮', max: 16000},
           { name: '扣篮', max: 30000},
           { name: '内线', max: 38000},
           { name: '中投', max: 52000},
           { name: '组织', max: 25000},
           { name: '内防', max: 27000},
           { name: '外防', max: 33000},
           { name: '抢断', max: 34000},
           { name: '盖帽', max: 29000},
           { name: '篮板', max: 25000}
        ]
    },
    series: [{
        name: '老鹰 vs 勇士）',
        type: 'radar',
        // areaStyle: {normal: {}},
        data : [
            {
                value : [4300, 10000, 28000, 35000, 50000, 19000,16000,17000,18000,19000,23000],
                name : '老鹰'
            },
             {
                value : [5000, 14000, 28000, 31000, 42000, 21000,19000,18000,17000,14000,16000],
                name : '勇士'
            }
        ]
    }]
}