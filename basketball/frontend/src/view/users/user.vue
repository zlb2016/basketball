<template>
    <div>
        <Row :gutter="32">
            <Col span="12">
                <Card>
                    <p slot="title">人员信息</p>
                    <div>
                        <div class="demo-avatar" style="margin-left:100px">
                            <Avatar :src="avatarpath+avatar" style="width:150px;height:150px"/>
                        </div>
                        <div style="margin-left:60px;margin-top:30px">
                            姓名：
                            <Input prefix="ios-contact" v-model="username" placeholder="姓名" style="width: auto" ></Input>
                            <br> 
                            编号：
                            <Input prefix="ios-contact" v-model="serialnum" placeholder="编号" style="width: auto;margin-top:10px" ></Input>
                            <br>
                            角色：
                            <Input prefix="ios-contact" v-model="duty" placeholder="角色" style="width: auto;margin-top:10px" ></Input>
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
    import { getUserView } from '@/api/user'
    import qs from 'qs'
    export default {
        props: {
            ret:'loan',
            code:''
        },
        data () {
            return {
                username:'',
                serialnum:'',
                duty:'',
                fix_id:'',
                avatar:'',
                userinfoData:[],
                userlogs: {},
                avatarpath:'http://localhost:8000/storage/avatar_images/',
            }
        },
        methods: {
           
        },
        mounted() {
            var token=getToken();
            this.code=this.$route.query.user_code;
            getUserView(token,this.code).then(res => {   
                    console.log('userInfo',res.data);
                    this.userinfoData=res.data;
                    this.fix_id=this.userinfoData.userinfo.id;
                    this.username=this.userinfoData.userinfo.name;
                    this.serialnum=this.userinfoData.userinfo.serialnum;
                    this.duty=this.userinfoData.userinfo.duty;
                    this.avatar=this.userinfoData.userinfo.avatar;
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
