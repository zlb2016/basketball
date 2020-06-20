import Mock from 'mockjs'
import {doCustomTimes}from '@/libs/util'
const Random = Mock.Random
 
export const classheight = {
    xAxis: {
        type: 'category',
        data: ['雄鹿', '猛龙', '76人', '凯尔特人', '步行者', '篮网', '魔术','活塞','黄蜂','热火','奇才','老鹰','公牛','骑士','尼克斯'],
        axisLabel:{
            interval:0,
            rotate:45,
            },

     
    },
    yAxis: {
        type: 'value'
    },
    series: [{
        data: [60, 58, 51, 49, 48, 42, 42,41,39,39,32,29,22,19,17],
        type: 'line'
    }]
}