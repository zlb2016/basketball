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
                 <Col span="2"><p>选择球队：</p></Col>
                <Col span="5"><Cascader :data="data4" :load-data="loadData" class="selection" style="width:120px"></Cascader></Col>
               </Row>
            </Card>
          </Col>
        </Row>
        <Row >
          <Col span="24">
            <Card class="bg">
              <Row >
                <Col span="6"><p>时间</p></Col>
                <Col span="6"><p>对阵</p></Col>
                <Col span="6"><p>比分</p></Col>
                <Col span="6"><p>地点</p></Col>
        
                    
              </Row>
            </Card>
          </Col>
          <Col span=""></Col>
        </Row>
         <Row >
          <Col span="24">
            <Card class="bg1">
                <Row class="new">
                <Col span="6"><p>7月01日 星期一 10:00</p></Col>
                <Col span="6"><a href=""><router-link  :to="{ path: '/schedule/scheduleInfo'}">老鹰</router-link></a>@<a href=""><router-link  :to="{ path: '/new/new'}">火箭</router-link></a></Col>
                <Col span="6" style="color:red"><p>未进行比赛</p></Col>
                <Col span="6"><p>甲骨文球馆</p></Col>     
              </Row>
              <Row class="new">
                <Col span="6"><p>6月19日 星期五 11:00</p></Col>
                <Col span="6"><a href=""><router-link  :to="{ path: '/new/new'}">猛龙</router-link></a>@<a href=""><router-link  :to="{ path: '/new/new'}">勇士</router-link></a></Col>
                <Col span="6"><p>114-110</p></Col>
                <Col span="6"><p>甲骨文球馆</p></Col>     
              </Row>
              <Row class="new">
                <Col span="6"><p>6月16日 星期日 10:00</p></Col>
                <Col span="6"><a href=""><router-link  :to="{ path: '/new/new'}">黄蜂</router-link></a>@<a href=""><router-link  :to="{ path: '/new/new'}">公牛</router-link></a></Col>
                <Col span="6"><p>55-68</p></Col>
                <Col span="6"><p>甲骨文球馆</p></Col>     
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
                data4: [
                    {
                        value: 'dongbu',
                        label: '东部球队',
                        children: [],
                        loading: false
                    },
                    {
                        value: 'xibu',
                        label: '西部球队',
                        children: [],
                        loading:false
                    }
                ]
          
            }
        },
        methods: {
            loadData (item, callback) {
                item.loading = true;
                setTimeout(() => {
                    if (item.value === 'dongbu') {
                        item.children = [
                            {
                                value: 'Bull',
                                label: '公牛'
                            },
                            {
                                value: 'Horbets',
                                label: '黄蜂'
                            },
                            {
                                value: '76',
                                label: '76人'
                            }
                        ];
                    } else if (item.value === 'xibu') {
                        item.children = [
                           {
                                value: 'SPURS',
                                label: '马刺'
                            },
                            {
                                value: 'Thunder',
                                label: '雷霆'
                            },
                            {
                                value: 'War',
                                label: '勇士'
                            }
                        ];
                    }
                    item.loading = false;
                    callback();
                }, 1000);
            }
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