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
        <Col span="12">
        <Card>
            <Row>
                <Col span="">
                <chart-all style="height: 336px;" :value="my_data_classheight" text="球队对比"></chart-all>
                </Col>
            </Row>
        </Card>
        </Col>
        <!--球员对比数据-->
        <Col span="12">
        <Card>
            <Row>
                <Col span="">
                <chart-all style="height: 336px;" :value="my_data_classheight" text="球队对比"></chart-all>
                </Col>
            </Row>
        </Card>
        </Col>
    </Row>
    <Row>
        <Col span="">
        <Card>
            <Row>
                <Col span="">
                <p style="font-size:18px">推荐阵容</p>
                </Col>
                <Col span="">
                <Table :columns="columns1" :data="data2"></Table>
                </Col>
            </Row>
        </Card>
        </Col>

    </Row>
</div>
</template>

<script>
import {
    classheight,
} from '@/mock/player'
import {
    ChartAll
} from '@/components/charts'
export default {
    components: {
        ChartAll,
    },
    data() {
        return {
            my_data_classheight: {},
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
            model1: '',
            columns1: [{
                    title: '姓名',
                    key: 'name'
                },
                {
                    title: '位置',
                    key: 'local'
                },
                {
                    title: '身高',
                    key: 'tall'
                },
                {
                    title: '体重',
                    key: 'weight'
                },
                {
                    title: '球号',
                    key: 'number'
                },
                {
                    title: '能力',
                    key: 'birth'
                },
                {
                    title: '经验',
                    key: 'experience'
                },

            ],
            data2: [{
                    name: '布鲁诺',
                    local: '前锋',
                    tall: '2.08米',
                    weight: '105.7公斤',
                    number: '13',
                    birth: '70+',
                    experience: '3',

                },
                {
                    name: '艾萨克',
                    local: '前锋-中锋',
                    tall: '2.13米',
                    weight: '117.9公斤',
                    number: '8',
                    birth: '60+',
                    experience: '1',

                },
                {
                    name: '亨特',
                    local: '前锋',
                    tall: '2.01米',
                    weight: '102.1公斤',
                    number: '12',
                    birth: '55',
                    experience: '1',

                },
                {
                    name: '布鲁诺',
                    local: '前锋',
                    tall: '2.08米',
                    weight: '105.7公斤',
                    number: '11',
                    birth: '50+',
                    experience: '2',

                },
            ]
        }
    },
    mounted() {
        this.my_data_classheight = classheight
    }
}
</script>