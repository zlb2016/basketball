<template>
<div>
    <Row>
        <Col span="">
        <Card>
            <Row>
                <Col span="3">
                <p>请选择对比球队：</p>
                </Col>
                <Col span="4">
                <Select v-model="model1" style="width:100px">
                    <Option v-for="item in cityList" :value="item.value" :key="item.value">{{ item.label }}</Option>
                </Select>
                </Col>
                <Col span="2">
                <p>VS</p>
                </Col>
                <Col span="4">
                <Select v-model="model1" style="width:100px">
                    <Option v-for="item in cityList" :value="item.value" :key="item.value">{{ item.label }}</Option>
                </Select>
                </Col>
            </Row>
        </Card>
        </Col>

    </Row>
    <Row>
        <Col span="6">
        <Card class="b2">
            <Row>
                <Col span="">
                <p>亚特兰大 老鹰</p>
                </Col>
                <Col span="">
                <p>常规赛 29胜-53负|东部第12名</p>
                </Col>
                <Col span="12">
                <Card>
                    <Row>
                        <Col span="">
                        <p>均场得分</p>
                        </Col>
                        <Col span="">
                        <p>103.2</p>
                        </Col>
                        <Col span="">
                        <p>联盟第21</p>
                        </Col>

                    </Row>
                </Card>
                </Col>
                <Col span="12">
                <Card>
                    <Row>
                        <Col span="">
                        <p>均场失分</p>
                        </Col>
                        <Col span="">
                        <p>104</p>
                        </Col>
                        <Col span="">
                        <p>联盟第10</p>
                        </Col>

                    </Row>
                </Card>
                </Col>
                 <Col span="12">
                <Card>
                    <Row>
                        <Col span="">
                        <p>均场篮板</p>
                        </Col>
                        <Col span="">
                        <p>44.3</p>
                        </Col>
                        <Col span="">
                        <p>联盟第9</p>
                        </Col>

                    </Row>
                </Card>
                </Col>
                <Col span="12">
                <Card>
                    <Row>
                        <Col span="">
                        <p>均场抢断</p>
                        </Col>
                        <Col span="">
                        <p>8.2</p>
                        </Col>
                        <Col span="">
                        <p>联盟第7</p>
                        </Col>

                    </Row>
                </Card>
                </Col>
                 <Col span="12">
                <Card>
                    <Row>
                        <Col span="">
                        <p>均场助攻</p>
                        </Col>
                        <Col span="">
                        <p>23.6</p>
                        </Col>
                        <Col span="">
                        <p>联盟第10</p>
                        </Col>

                    </Row>
                </Card>
                </Col>
                <Col span="12">
                <Card>
                    <Row>
                        <Col span="">
                        <p>均场失误</p>
                        </Col>
                        <Col span="">
                        <p>15.78</p>
                        </Col>
                        <Col span="">
                        <p>联盟第3</p>
                        </Col>

                    </Row>
                </Card>
                </Col>
            </Row>
        </Card>
        </Col>
        <Col span="12">
        <Card >
            <Row>
                <Col span="">
               <Row>
                <chart-all style="height: 336px;" :value="my_data_classheight" text="球队对比"></chart-all>
                </Row>
                </Col>
                
            </Row>
        </Card>
        </Col>
        <Col span="6">
        <Card class="b1">
            <Row>
                <Col span="">
                <p>金州 勇士</p>
                </Col>
                <Col span="">
                <p>常规赛 57胜-25负|西部第1名</p>
                </Col>
                <Col span="12">
                <Card>
                    <Row>
                        <Col span="">
                        <p>均场得分</p>
                        </Col>
                        <Col span="">
                        <p>103.2</p>
                        </Col>
                        <Col span="">
                        <p>联盟第21</p>
                        </Col>

                    </Row>
                </Card>
                </Col>
                <Col span="12">
                <Card>
                    <Row>
                        <Col span="">
                        <p>均场失分</p>
                        </Col>
                        <Col span="">
                        <p>104</p>
                        </Col>
                        <Col span="">
                        <p>联盟第10</p>
                        </Col>

                    </Row>
                </Card>
                </Col>
                 <Col span="12">
                <Card>
                    <Row>
                        <Col span="">
                        <p>均场篮板</p>
                        </Col>
                        <Col span="">
                        <p>44.3</p>
                        </Col>
                        <Col span="">
                        <p>联盟第9</p>
                        </Col>

                    </Row>
                </Card>
                </Col>
                <Col span="12">
                <Card>
                    <Row>
                        <Col span="">
                        <p>均场抢断</p>
                        </Col>
                        <Col span="">
                        <p>8.2</p>
                        </Col>
                        <Col span="">
                        <p>联盟第7</p>
                        </Col>

                    </Row>
                </Card>
                </Col>
                 <Col span="12">
                <Card>
                    <Row>
                        <Col span="">
                        <p>均场助攻</p>
                        </Col>
                        <Col span="">
                        <p>23.6</p>
                        </Col>
                        <Col span="">
                        <p>联盟第10</p>
                        </Col>

                    </Row>
                </Card>
                </Col>
                <Col span="12">
                <Card>
                    <Row>
                        <Col span="">
                        <p>均场失误</p>
                        </Col>
                        <Col span="">
                        <p>15.78</p>
                        </Col>
                        <Col span="">
                        <p>联盟第3</p>
                        </Col>

                    </Row>
                </Card>
                </Col>
            </Row>
        </Card>
        </Col>

    </Row>
</div>
</template>

<script>
import{ classheight, }from '@/mock/player'
import { ChartAll } from '@/components/charts'
export default {
    components:{
ChartAll,
},
    data() {
        return {
            my_data_classheight:{},
            cityList: [{
                    value: 'ly',
                    label: '老鹰'
                },
                {
                    value: 'ys',
                    label: '勇士'
                },
                {
                    value: 'gn',
                    label: '公牛'
                },
                {
                    value: 'hj',
                    label: '火箭'
                },
                {
                    value: 'ketr',
                    label: '凯尔特人'
                },
                {
                    value: '76',
                    label: '76人'
                }
            ],
            model1: ''
        }
    },
    mounted(){
this.my_data_classheight = classheight
}
}
</script>

<style>
.b1{
    font-size:15px;
    color:cadetblue;
}
.b2{
    font-size:15px;
    color:rgb(202, 81, 218);
}
</style>