<template>
    <div>
        <Card>
            <Row>
                <Col span="6">
                    <Button style="margin-left:20px;margin-top:6px" type="info">动作类别</Button>
                    <Select v-model="model1" @on-change="getactionValue" style="width:200px;margin-left:10px;margin-top:6px">
                        <Option v-for="item in actiionlist" :value="item.id" :key="item.id">{{ item.name }}</Option>
                    </Select>
                </Col>
                <Col span="6">
                    <Button style="margin-left:20px;margin-top:6px" type="success">视频类型</Button>
                    <Select v-model="model2" @on-change="getvideoValue" style="width:200px;margin-left:10px;margin-top:6px">
                        <Option v-for="item in videolist" :value="item.value" :key="item.value">{{ item.name }}</Option>
                    </Select>
                </Col>
                <Col span="6">
                    <Button style="margin-left:20px;margin-top:6px" @click="handleSubmit()" type="warning">分析视频</Button>
                </Col>
            </Row>
            <br>
            <Row :gutter="16">
                <Col span="12">
                    <div>
                        <Row>
                            <Card style="height:320px">
                                <p slot="title">
                                    <Icon type="ios-film-outline"></Icon>
                                    视频
                                </p>
                                <ul>
                                    <uploadfile :getaction="actiontype" :getvideo="videotype" :is_standard='1' @filelist="filelist"></uploadfile>
                                </ul>
                            </Card>
                            
                        </Row>
                    </div>
                </Col>
                <Col span="12">
                        <Col span="12">
                            <Card>
                                <p slot="title">
                                    <Icon type="ios-body" />
                                    动作序列
                                </p>
                                <ul>
                                    <Row>
                                        <br>
                                        <div v-for="item in filesList">
                                            <img :src="filepath+'standard_action/standard_pose/'+actype+'/'+item" width="250px" height="150px"/>
                                            <Button style="margin-left:100px;" type="success">{{item}}</Button>
                                        </div>
                                    </Row>
                                </ul> 
                            </Card>
                        </Col>
                </Col>
            </Row>
            <br>
            
            </Row>
        </Card>
    </div>
</template>
<script>
    import uploadfile from './uploadfile.vue'
    import { getToken } from '@/libs/util'
    import { getActionList } from '@/api/action'
    import { getVideocut } from '@/api/videoaction'
    import { getVideoresult } from '@/api/videoaction'
    import qs from 'qs'
    export default {
        name: 'standard',
        components: {
            uploadfile,
        },
        data(){
            return{
                actiionlist:[],
                model1:'',
                model2:'',
                videolist:[//视频类型
                    {
                        value: '1',
                        name: '彩色视频'
                    },
                    {
                        value: '2',
                        name: '深度视频'
                    },
                ],
                actiontype:'',
                videotype:'',
                is_standard:'',
                filelists:[],//上传文件的数组
                filesList:[],
                filepath:'http://localhost:8000/storage/',
                actype:''//动作文件夹名称
            }
        },
        methods: {
           getactionValue(val){//获取动作类别id
                console.log('12321--',val);
                this.actiontype=val;
           },
           getvideoValue(val){//获取动视频类型value
                console.log('33--',val)
                this.videotype=val;
                if(val=='1'){
                    console.log('33--','彩色视频')
                }else{
                    console.log('33--','深度视频')
                }
           },
           filelist(data){//接收子组件的上传文件名
                this.filelists.push(data);
            },
            handleSubmit(){//切分视频
                var token=getToken();
                getVideocut(token,this.filelists).then(res => {//获得上传文件的路径
                    if(res.data.status=="success"){//接收返回值
                        
                        console.log('123====',res.data);
                        var d=res.data.allda;//获取文件名和动作类型、视频类型、是否标准动作
                        if(res.data.mark==1){//对应深度视频和彩色视频已上传并切分成功
                            var action_type=d[1];//获取动作类型，根据动作类型分析姿态
                            this.actype=res.data.actiontype;
                            var path='standard_action/standard_pose/'+this.actype;
                            this.$Message.success('深度视频和彩色视频切分成功，正在进行姿态分析!');
                            getVideoresult(token,path).then(res => {//接收视频分析结果:将切分的图片帧和动作id存储到action_frames表中;将人体骨架坐标存储到skeletons表中
                                this.filesList=res.data.data;
                            })
                        }else{
                            if(d[2]==1){//判断视频类型
                                this.$Message.error('彩色视频切分成功，请上传对应深度视频!');
                            }else{
                                this.$Message.error('深度视频切分成功，请上传对应彩色视频!');
                            }
                            location.reload();//刷新本页面
                        }                      
                    }else{
                        this.$Message.error('操作失败!');
                    }                         
                })
            }
        },
        mounted() {
            var token=getToken();
            getActionList(token).then(res => {//获得动作类别列表
                this.actiionlist = res.data.actions;
                console.log('actiionlist',res.data);
            })
        },
    }
</script>
