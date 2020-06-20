<template>
    <div>
        <Card>
            <Row>
                <Col span="12">
                    <Dropdown style="margin-left: 20px">
                        <Button type="primary">
                            动作类别
                        <Icon type="ios-arrow-down"></Icon>
                        </Button>
                        <DropdownMenu slot="list">
                            <DropdownItem>投篮</DropdownItem>
                            <DropdownItem>运球</DropdownItem>
                            <DropdownItem>传球</DropdownItem>
                        </DropdownMenu>
                    </Dropdown>
                </Col>
            </Row>
            <br>
            <Row :gutter="16">
                    <div>
                        <Row>
                            <Card >
                                <p slot="title">
                                    <Icon type="ios-film-outline"></Icon>
                                    数据统计
                                </p>
                                <ul>
                                    <Row>

                                    </Row>
                                    <Row>
                                        <img src="./训练统计.png" width="700" height="500" >
                                    </Row>
                                </ul>
                            </Card>
                        </Row>
                    </div>
            </Row>
            <br>
            
            </Row>
        </Card>
    </div>
</template>
<script>
    import { getToken } from '@/libs/util'
    import qs from 'qs'
    export default {
        name: 'basic',
        data(){
            return{
           
            }
        },
        methods: {
           
        },
        mounted() {
            
        },
    }
</script>