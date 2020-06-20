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
                    <Button style="margin-left:20px;margin-top:6px" @click="handleSubmit()" type="success">分析</Button>
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
                                    <uploadfile :getaction="actiontype" :getvideo="videotype" :is_standard='0' @filelist="filelist"></uploadfile>
                                </ul>
                            </Card>
                            
                        </Row>
                    </div>
                </Col>
                <Col span="12">
                    <Row>
                        <Card>
                            <p slot="title">
                                <Icon type="ios-contrast" />
                                对比
                            </p>
                            <ul>
                                <Row>
                                    <Col span="12">
                                        <Row>
                                            <div style="margin-left:70px">
                                                <Tag color="orange">视频段1</Tag>
                                            </div>  
                                        </Row>
                                        <img :src='filepath+actionframe' width="200px" height="200px"/>
                                    </Col>
                                    <Col span="12">
                                        <Row>
                                             <div style="margin-left:70px">
                                                <Tag color="green">标准动作1</Tag>
                                             </div>
                                        </Row>
                                        <img :src='filepath+standard_action' width="200px" height="200px"/>
                                    </Col>
                                </Row>
                            </ul>
                        </Card>
                    </Row>
                </Col>
            </Row>
            <br>
            <Row>
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
                                <img :src="filepath+'test_action/athlete-'+userid+'/'+actype+'/pose/'+item" width="250px" height="150px" align="middle"/>
                                <Button style="margin-left:80px;margin-top:20px" @click="handlePose(item)" type="success">姿态分析</Button>
                            </div>
                        </Row>
                        </ul> 
                    </Card>
                </Col>
                <Col span="12">
                    <Card>
                        <p slot="title">
                            <Icon type="ios-text-outline" />
                            分析结果
                        </p>
                        <ul>
                            <Row>
                                <br>
                                <Input v-model="value" type="textarea"  :rows="8" placeholder="Enter something..." />
                            </Row>
                        </ul>
                    </Card>
                </Col>
            </Row>
        </Card>
    </div>
</template>
<script>
    import uploadfile from './uploadfile.vue'
    import { getActionList } from '@/api/action'
    import { getVideocut } from '@/api/videoaction'
    import { getVideoresult } from '@/api/videoaction'
    import {getVideoposeresult} from '@/api/videoaction'
    import {getVideoaddresult} from '@/api/videoaction'
    import { getToken } from '@/libs/util'
    import qs from 'qs'
    export default {
        name: 'basic',
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
                value:'测试动作，标准动作，相似度',
                filesList:[],
                filepath:'http://localhost:8000/storage/',
                actionframe:'test/frame1.png',//默认显示的图片地址
                standard_path:'http://localhost:8000/storage/',
                standard_action:'standard_action/standard_pose/shoot/1.png',//默认显示的图片地址,
                filelists:[],//上传文件的数组
                actype:'',
                userid:''//运动员id

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
            filelist(data){//接收子组件的上传文件名-视频类型、动作类型、是否标准动作
                this.filelists.push(data);
                console.log('filelists',this.filelists);
                console.log('data====',data);
            },
            handleSubmit() {//需要上传视频的文件名
                var token=getToken();
                getVideocut(token,this.filelists).then(res => {//获得上传文件的路径
                    console.log('res.data---',res.data);
                    if(res.data.status=="success"){//接收返回值
                        var d=res.data.allda;//获取文件名和动作类型、视频类型、是否标准动作
                        if(res.data.mark==1){//对应深度视频和彩色视频已上传并切分成功
                            var action_type=d[1];//获取动作类型，根据动作类型分析姿态
                            this.actype=res.data.actiontype;
                            this.userid=res.data.userid;
                            console.log('res.dataid---',res.data.userid);
                            var path='test_action/athlete-'+this.userid+'/'+this.actype+'/pose';
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
            },
            handlePose(item){//动作序列下分析姿态
                var token=getToken();
                this.actionframe='color_pic/'+item;
                getVideoposeresult(token,'2','1').then(res => {//获取存储的分析结果,参数为动作id和视频帧id（根据标准动作和测试动作的骨架坐标进行计算，得出结果存储到action_results表）
                    if(res.data.status=="success"){//接收返回值
                        console.log('res.data.',res.data)
                        if(res.data.data!=null){
                            this.$Message.success('动作分析结果已获取!');
                            this.value=res.data.data['result'];
                        }else{//进行计算，存储计算结果
                            this.$Message.success('视频正在进行分析，请等待!');
                            //分析结果可以使用python进行分析，然后新增到数据库中
                            var info={
                                action_id:'2',
                                frame:'1',
                                result:'测试新增分析结果'
                            }
                            getVideoaddresult(token,qs.stringify(info)).then(res => {//接收视频分析结果
                                if(res.data.status=="success"){
                                    this.$Message.success('动作分析结果已获取!');
                                    this.value=res.data.data;
                                }else{
                                    this.$Message.error('获取结果操作失败!');
                                }   
                            })
                        }
                    }else{
                        this.$Message.error('操作失败!');
                    }                         
                })
                this.standard_action='standard_action/standard_pose/shoot/standard.jpg'//动作类别+视频帧
                //this.value='该动作为运球，姿态分析结果：相似性为90%，需要继续提高手肘的高度';//姿态分析结果
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