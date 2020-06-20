<template>
    <div>
        <Row :gutter="24">
            <Col span="24">
                <Card>
                    <p slot="title">添加人员</p>
                    <div>
                    <Form ref="formValidate" :model="formValidate" :rules="ruleValidate" :label-width="80">
                        <FormItem label="姓名" prop="name">
                            <Input v-model="formValidate.name" placeholder="姓名"></Input>
                        </FormItem>
                        <FormItem label="编号" prop="serialnum">
                            <Input v-model="formValidate.serialnum" placeholder="编号"></Input>
                        </FormItem>
                        <FormItem label="角色" prop="duty">
                            <Input v-model="formValidate.duty" placeholder="角色">
                            </Input>
                        </FormItem>
                        <FormItem label="照片" prop="avatar">
                            <Input v-model="formValidate.avatar" placeholder="照片">
                            </Input>
                        </FormItem>
                        <FormItem label="邮箱" prop="email" style="display:none">
                            <Input v-model="formValidate.email" placeholder="邮箱">
                            123456@163.com
                            </Input>
                        </FormItem>
                        <FormItem label="密码" prop="password" style="display:none">
                            <Input v-model="formValidate.password" placeholder="密码">
                            secret
                            </Input>
                        </FormItem>
                        <FormItem>
                            <Button type="primary" @click="handleSubmit('formValidate')">提交</Button>
                            <Button @click="handleReset('formValidate')" style="margin-left: 8px">重置</Button>
                        </FormItem>
                    </Form>
                    </div>                    
                </Card>
            </Col>
        </Row>
    </div>

</template>
<script>
    import { getUseradd } from '@/api/user'
    import { getToken } from '@/libs/util'
    import qs from 'qs'
    import {isIntegerNotMust} from './js/validate'
    export default {
        data () {
            return {
                formValidate: {
                    serialnum: '',
                    duty: '',
                    avatar: '',
                    email: '123456@163.com',
                    name: '',
                    password: 'secret'
                },
                ruleValidate: {
                    serialnum: [
                        {required: true,validator: isIntegerNotMust,trigger:'blur'}
                    ],
                    duty: [
                        { required: true,  message: '请输入角色', trigger: 'blur' }
                    ],
                    avatar: [
                        { required: true,  message: '请上传照片', trigger: 'change' }
                    ],
                    name: [
                        { required: true,  message: '请输入姓名', trigger: 'blur' }
                    ]
                }
            }
        },
        methods: {
            handleSubmit (name) {
                this.$refs[name].validate((valid) => {
                    if (valid) {
                        var token=getToken();
                var data={
                            "serialnum":this.formValidate.serialnum,//编号
                            "duty":this.formValidate.duty,//角色
                            "avatar":this.formValidate.avatar,//照片
                            "email":this.formValidate.email,//邮箱
                            "name":this.formValidate.name,//姓名
                            "password":this.formValidate.password//密码
                        }
                        getUseradd(token,qs.stringify(data)).then(res => {
                            if(res.data.status=="success"){//接收返回值
                                this.$Message.success('操作成功!');
                                //location.reload();//刷新本页面
                            }else{
                                this.$Message.error('操作失败!');
                            }                         
                        })
                    } else {
                        this.$Message.error('操作失败!');
                    }
                })
            },
            handleReset (name) {
                this.$refs[name].resetFields();
            }
        }
    }
</script>
