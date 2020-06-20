<template>
    <div>
        <Upload
            ref="upload"
            :before-upload="upload"
            :show-upload-list="false"
            :on-success="handleSuccess"
            :format="['mp4','avi']"
            :max-size="2048"
            :on-format-error="handleFormatError"
            :on-exceeded-size="handleMaxSize"
            multiple
            type="drag"
            :action="baseurl"
            style="display: inline-block;width:195px;float:left;">
            <div style="width: 58px;height:58px;line-height: 58px;">
                <Icon type="ios-camera" size="20"></Icon>
            </div>
            <div style="width: 195px;height:130px;line-height: 130px;text-align:center;border:1px solid #dddee1;cursor:pointer;">
                <Icon type="plus" size="40" color="#dddee1"></Icon>
            </div>
        </Upload>
        <div v-for="item in uploadList">
            <template v-if="item.status === 'finished'">
                <iframe :src="fileData" frameborder="0"></iframe>
            </template>
            <template>
                <Progress v-if="item.showProgress" :percent="item.percentage" hide-info></Progress>
            </template>
        </div>
    </div>
</template>
<script>
    import {getVideoadd} from '@/api/videoaction'
    import qs from 'qs'
    import { getToken } from '@/libs/util'
    export default {
        data() {
            return {
                token:'',
                fileData:'',
                uploadList: [],
                baseurl:''
            }
        },
        methods: {
            upload(file){
                let exceededNum=file.name.lastIndexOf(".");
　　            let exceededStr=file.name.substring(exceededNum+1,file.name.length).trim();
                console.log('self',exceededNum)
                console.log('uploads',exceededStr);
                this.fileData=file;
　　             return true;
            },
            handleSuccess (res, file) {
                var filepath=res["data"];
                this.fileData='http://localhost:8000/storage/'+filepath;
                console.log('res',res);
                console.log('file',file);
            },
            handleFormatError (file) {
                this.$Notice.warning({
                    title: '文件格式不正确',
                    desc: '文件格式 ' + file.name + ' 不正确, 请选择mp4或avi文件'
                });
            },
            handleMaxSize (file) {
                this.$Notice.warning({
                    title: '超出文件大小限制',
                    desc: '文件  ' + file.name + ' 太大，不能超过2M.'
                });
            },
        },
        mounted() {
            var token=getToken();
            this.token=token;
            this.uploadList = this.$refs.upload.fileList;
            this.baseurl='http://localhost:8000/api/v1/videos/add?token='+this.token;
        },
    }
</script>
