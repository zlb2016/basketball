<template>
    <div>
        <input autofocus id='one' type="text" data-index="0" >
        <br/>
        <br/>
        <input :autofocus='sc' id='test' type="text" data-index="0" @input="test()">
    </div>
</template>
<style scoped>
</style>
<script type="text/babel">
    export default {
        data() {
            return {
                focusCtrl:true,  // 自动聚焦控制,变动时,执行自动聚焦指令
                sc:false
            }
        },
        methods: {
           test(){
               //alert(123)
               var dd=document.getElementById("one");
               //this.focusCtrl=false;
               alert(dd.autofocus);
               dd.autofocus=false;
               alert(dd.autofocus);
               dd.removeAttribute("autofocus");
              // alert(this.focusCtrl);
               this.sc=true;
           }
        },
        mounted(){
    
        }
    }
</script>
