<template>
<div>
    <Row >
      <Col span="18">
        <Card>
          <Row >
            <Col span="" class="dm"><p>亚特兰大老鹰队</p></Col>
            <Col span=""><p>常规赛  29胜-53负</p></Col>
           <Col span=""><p>东部第12名</p></Col>
          </Row>
        </Card>
      </Col>
      <Col span="6">
        <Card class="jl">
          <Row >
            <Col span=""><p>教练：罗伊德 皮尔斯</p></Col>
            <Col span=""><p>分区：东部|东南分区</p></Col>
              <Col span=""><p>球馆：菲利浦体育馆</p></Col>
            
          </Row>
        </Card>
      </Col>
       
      
    </Row>
    <Row>
        <Col span="14">
        <Card class="bor">
            <Carousel autoplay v-model="value2" loop>
                <CarouselItem>
                    <div class="demo-carousel"><img src="@/assets/images/1.png" width="550" height="480"> </div>
                    <div class="tp">
                        <p>官宣：休斯顿火箭正式续约豪斯与小里弗斯</p>
                    </div>
                </CarouselItem>
                <CarouselItem>
                    <div class="demo-carousel"><img src="@/assets/images/2.jpg" width="550" height="480"> </div>
                    <div class="tp">
                        <p>沃克谈加盟绿军理由：希望能在这里多赢球</p>
                    </div>
                </CarouselItem>
                <CarouselItem>
                    <div class="demo-carousel"><img src="@/assets/images/3.jpg" width="550" height="480"> </div>
                    <div class="tp">
                        <p>自由市场签约汇总 杜兰特欧文齐聚篮网</p>
                    </div>
                </CarouselItem>
                <CarouselItem>
                    <div class="demo-carousel"><img src="@/assets/images/4.jpg" width="550" height="480"> </div>
                    <div class="tp">
                        <p>官宣：坎特正式签约凯尔特人 将穿11号球衣</p>
                    </div>
                </CarouselItem>
            </Carousel>
        </Card>
        </Col>
        <Col span="10">
          <Card class="title">
            <Row  >
              <Col span="8">
                <p>球队赛程</p>
              </Col>
            </Row>
          </Card>
           <Card >
              <Row >
                  <Col span="4"><p>日期</p></Col>
                <Col span="4"><p>时间</p></Col>
                <Col span="4"><p>对手</p></Col>
                <Col span="4"><p>比分</p></Col>
                <Col span="4"><p>结果</p></Col>
                <Col span="4"><p>地点</p></Col>     
              </Row>
            </Card>
           <Card >
                <Row class="new">
               <Col span="4"><p>7-01</p></Col>
                <Col span="4"><p>10:00</p></Col>
                <Col span="4"><a href=""><router-link  :to="{ path: ''}">火箭</router-link></a></Col>
                <Col span="4" style="color:red"><p>0-0</p></Col>
                  <Col span="4" style="color:red"><p>未比赛</p></Col>
                
                <Col span="4"><p>甲骨文馆</p></Col>     
              </Row>
               <Row class="new">
               <Col span="4"><p>6-28</p></Col>
                <Col span="4"><p>15:00</p></Col>
                <Col span="4"><a href=""><router-link  :to="{ path: ''}">勇士</router-link></a></Col>
                <Col span="4" style="color:red"><p>114-110</p></Col>
                  <Col span="4" style="color:red"><p>胜</p></Col>
                <Col span="4"><p>甲骨文馆</p></Col>     
              </Row>
              <Row class="new">
               <Col span="4"><p>6-27</p></Col>
                <Col span="4"><p>11:00</p></Col>
                <Col span="4"><a href=""><router-link  :to="{ path: ''}">黄蜂</router-link></a></Col>
                <Col span="4" style="color:red"><p>55-68</p></Col>
                  <Col span="4" style="color:red"><p>败</p></Col>
                <Col span="4"><p>甲骨文馆</p></Col>     
              </Row>
               <Row class="new">
               <Col span="4"><p>6-28</p></Col>
                <Col span="4"><p>15:00</p></Col>
                <Col span="4"><a href=""><router-link  :to="{ path: ''}">勇士</router-link></a></Col>
                <Col span="4" style="color:red"><p>114-110</p></Col>
                  <Col span="4" style="color:red"><p>胜</p></Col>
                <Col span="4"><p>甲骨文馆</p></Col>     
              </Row>
              <Row class="new">
               <Col span="4"><p>6-27</p></Col>
                <Col span="4"><p>11:00</p></Col>
                <Col span="4"><a href=""><router-link  :to="{ path: ''}">黄蜂</router-link></a></Col>
                <Col span="4" style="color:red"><p>55-68</p></Col>
                  <Col span="4" style="color:red"><p>败</p></Col>
                <Col span="4"><p>甲骨文馆</p></Col>     
              </Row>
               <Row class="new">
               <Col span="4"><p>6-28</p></Col>
                <Col span="4"><p>15:00</p></Col>
                <Col span="4"><a href=""><router-link  :to="{ path: ''}">勇士</router-link></a></Col>
                <Col span="4" style="color:red"><p>114-110</p></Col>
                  <Col span="4" style="color:red"><p>胜</p></Col>
                <Col span="4"><p>甲骨文馆</p></Col>     
              </Row>
              <Row class="new">
               <Col span="4"><p>6-27</p></Col>
                <Col span="4"><p>11:00</p></Col>
                <Col span="4"><a href=""><router-link  :to="{ path: ''}">黄蜂</router-link></a></Col>
                <Col span="4" style="color:red"><p>55-68</p></Col>
                  <Col span="4" style="color:red"><p>败</p></Col>
                <Col span="4"><p>甲骨文馆</p></Col>     
              </Row>
               <Row class="new">
               <Col span="4"><p>6-28</p></Col>
                <Col span="4"><p>15:00</p></Col>
                <Col span="4"><a href=""><router-link  :to="{ path: ''}">勇士</router-link></a></Col>
                <Col span="4" style="color:red"><p>114-110</p></Col>
                  <Col span="4" style="color:red"><p>胜</p></Col>
                <Col span="4"><p>甲骨文馆</p></Col>     
              </Row>
              <Row class="new">
               <Col span="4"><p>6-27</p></Col>
                <Col span="4"><p>11:00</p></Col>
                <Col span="4"><a href=""><router-link  :to="{ path: ''}">黄蜂</router-link></a></Col>
                <Col span="4" style="color:red"><p>55-68</p></Col>
                  <Col span="4" style="color:red"><p>败</p></Col>
                <Col span="4"><p>甲骨文馆</p></Col>     
              </Row>
                <Row class="new">
               <Col span="4"><p>6-28</p></Col>
                <Col span="4"><p>15:00</p></Col>
                <Col span="4"><a href=""><router-link  :to="{ path: ''}">勇士</router-link></a></Col>
                <Col span="4" style="color:red"><p>114-110</p></Col>
                  <Col span="4" style="color:red"><p>胜</p></Col>
                <Col span="4"><p>甲骨文馆</p></Col>     
              </Row>
              <Row class="new">
               <Col span="4"><p>6-27</p></Col>
                <Col span="4"><p>11:00</p></Col>
                <Col span="4"><a href=""><router-link  :to="{ path: ''}">黄蜂</router-link></a></Col>
                <Col span="4" style="color:red"><p>55-68</p></Col>
                  <Col span="4" style="color:red"><p>败</p></Col>
                <Col span="4"><p>甲骨文馆</p></Col>     
              </Row>
                <Row class="new">
               <Col span="4"><p>6-28</p></Col>
                <Col span="4"><p>15:00</p></Col>
                <Col span="4"><a href=""><router-link  :to="{ path: ''}">勇士</router-link></a></Col>
                <Col span="4" style="color:red"><p>114-110</p></Col>
                  <Col span="4" style="color:red"><p>胜</p></Col>
                <Col span="4"><p>甲骨文馆</p></Col>     
              </Row>
            
            </Card>
        </Col>
    </Row>
</div>
</template>
<style>
.title{
    font-size: 16px;
    background-color:  rgb(3, 123, 153);
    color:white;
}
.new{
    margin-top:10px;
}
.tp {
  position: relative;
  top: -40px;
  color: white;
  font-size: 18px;
  background-color: black;
}
.dm{
    font-size:24px;
}
.jl{
    font-size: 18px;
}
</style>
