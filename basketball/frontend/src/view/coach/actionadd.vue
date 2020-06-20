<template>
    <div>
        <Row :gutter="24">
            <Col span="24">
                <Card>
                    <p slot="title">添加动作类别</p>
                    <div>
                    <Form ref="formValidate" :model="formValidate" :rules="ruleValidate" :label-width="80">
                        <FormItem label="动作名称" prop="name">
                            <Input v-model="formValidate.name" placeholder="动作名称"></Input>
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
    import { getActionadd } from '@/api/action'
    import { getToken } from '@/libs/util'
    import qs from 'qs'
    export default {
        data () {
            return {
                formValidate: {
                    name: ''
                },
                ruleValidate: {
                    name: [
                        { required: true,  message: '请输入动作名称', trigger: 'blur' }
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
                            "name":this.formValidate.name,//动作名称
                        }
                        getActionadd(token,qs.stringify(data)).then(res => {
                            console.log('data',res.data)
                            if(res.data.status=="success"){//接收返回值
                                this.$Message.success('操作成功!');
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
