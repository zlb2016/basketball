<template>
    <div>
        <Row >
          <Col span="24">
            <Card class="sel">
               <Row >
                   <Col span="2"><p>开始时间：</p></Col>
                <Col span="5">
                    <DatePicker type="date" placeholder="请选择时间..." style="width:110px"></DatePicker>
                </Col>
                  <Col span="2"><p>结束时间：</p></Col>
                <Col span="5">
                    <DatePicker type="date" placeholder="请选择时间..." style="width:110px" ></DatePicker>
                </Col>
               </Row>
            </Card>
          </Col>
        </Row>
        <Row >
          <Col span="24">
            <Card class="bg">
              <Row >
                <Col span="5"><p>时间</p></Col>
                <Col span="5"><p>对阵</p></Col>
                <Col span="5"><p>比分</p></Col>
                <Col span="5"><p>地点</p></Col>
                <Col span="4"><p>操作</p></Col>
                    
              </Row>
            </Card>
          </Col>
          <Col span=""></Col>
        </Row>
         <Row >
          <Col span="24">
            <Card class="bg1">
                <Row class="new">
                <Col span="5"><p>7月01日 星期一 10:00</p></Col>
                <Col span="5"><a href=""><router-link  :to="{ path: '/schedule/scheduleInfo'}">老鹰</router-link></a>@<a href=""><router-link  :to="{ path: '/new/new'}">火箭</router-link></a></Col>
                <Col span="5" style="color:red"><p>未进行比赛</p></Col>
                <Col span="5"><p>甲骨文球馆</p></Col>     
                <Col span="4" ><a href=""><router-link  :to="{ path: '/tactical/defenseInfo_page'}" >查看详情</router-link></a></Col>
                
              </Row>
              <Row class="new">
                <Col span="5"><p>6月19日 星期五 11:00</p></Col>
                <Col span="5"><a href=""><router-link  :to="{ path: '/new/new'}">猛龙</router-link></a>@<a href=""><router-link  :to="{ path: '/new/new'}">勇士</router-link></a></Col>
                <Col span="5"><p>114-110</p></Col>
                <Col span="5"><p>甲骨文球馆</p></Col>
                <Col span="4" ><a href=""><router-link  :to="{ path: ''}" >查看详情</router-link></a></Col>
                     
              </Row>
              <Row class="new">
                <Col span="5"><p>6月16日 星期日 10:00</p></Col>
                <Col span="5"><a href=""><router-link  :to="{ path: '/new/new'}">黄蜂</router-link></a>@<a href=""><router-link  :to="{ path: '/new/new'}">公牛</router-link></a></Col>
                <Col span="5"><p>55-68</p></Col>
                <Col span="5"><p>甲骨文球馆</p></Col>     
                <Col span="4" ><a href=""><router-link  :to="{ path: ''}" >查看详情</router-link></a></Col>
                
              </Row>
            </Card>
          </Col>
        </Row>
    </div>
</template>
 <script>
    export default {
        data () {
            return {
               
          
            }
        },
        methods: {
          
        }
    }
</script>

<style>
.sel{
    font-size:15px;
    background-color: rgb(31, 171, 206);

}
.bg{
    background-color:  rgb(3, 123, 153);
    color:white;
    font-size:16px;
    text-align: center;
}
.bg1{

    font-size:16px;
    text-align: center; 

}
.new{
    margin-top:10px;
}
</style>