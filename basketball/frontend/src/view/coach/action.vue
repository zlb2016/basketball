<template>
    <div>
        <Row :gutter="32">
            <Col span="12">
                <Card>
                    <p slot="title">动作类别信息</p>
                    <div>
                        <div style="margin-left:60px;margin-top:30px">
                            动作名称：
                            <Input prefix="ios-basketball" v-model="actionname" placeholder="动作名称" style="width: auto" ></Input>
                            <br> 
                            创建时间：
                            <Input prefix="ios-basketball-outline" v-model="created_at" placeholder="创建时间" style="width: auto;margin-top:10px" ></Input>
                        </div>
                    </div>
                </Card>
            </Col>
        </Row>
        <br/>
        <br/>
        
    </div>
</template>
<script>
    import { getToken } from '@/libs/util'
    import { getActionView } from '@/api/action'
    import qs from 'qs'
    export default {
        data () {
            return {
                actionname:'',
                created_at:'',
            }
        },
        methods: {
           
        },
        mounted() {
            var token=getToken();
            this.code=this.$route.query.action_code;
            console.log('code',this.code)
            getActionView(token,this.code).then(res => {
                    console.log('actionInfo',res.data);
                    this.actioninfoData=res.data;
                    this.actionname=this.actioninfoData.actioninfo.name;
                    this.created_at=this.actioninfoData.actioninfo.created_at;
            });
        }
    }
</script>
<style>
    .page-container {
    left: 0;
    right: 0;
    margin: auto;
    margin-top: 20px;
    padding-left: 280px;
    display: inline-flex !important;
    }

    @media only screen and (max-width : 992px) {
    .page-container {
        padding-left: 0;
        display: flex !important;
    }
    }

    #navbar {
    position: absolute;
    top: 20px;
    left: 20px;
    }

    .center-content {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    }

    .side-by-side {
    display: flex;
    justify-content: center;
    align-items: center;
    }
    .side-by-side >* {
    margin: 0 5px;
    }

    .bold {
    font-weight: bold;
    }

    .margin-sm {
    margin: 5px;
    }

    .margin {
    margin: 20px;
    }

    .button-sm {
    padding: 0 10px !important;
    }

    .pad-sides-sm {
    padding: 0 8px !important;
    }

    #github-link {
    display: flex !important;
    justify-content: center;
    align-items: center;
    border-bottom: 1px solid;
    margin-bottom: 10px;
    }

    #overlay, .overlay {
    position: absolute;
    top: 0;
    left: 0;
    }

    #facesContainer canvas {
    margin: 10px;
    }
</style>
