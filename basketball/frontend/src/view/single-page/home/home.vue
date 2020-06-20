<template>
<div>
  <Row>
    <Col span="4">
    <Card class="btn">
      <Row>
        <Col span="">
        <DatePicker :value="value1" style="width: 120px" type="date" placeholder="请选择日期"></DatePicker>
        </Col>
        <Col span="">
        <p>星期三</p>
        </Col>
        <Col span="">
        <p>10场比赛</p>
        </Col>
        <!-- <Col span=""><Button type="primary">全部赛程</Button></Col> -->
      </Row>

    </Card>
    </Col>
    <Col span="20">
    <Card class="btn">
      <Row>
        <Col span="7">
        <Card class="margin">
          <Row>
            <Col span="8">
            <p>雄鹿</p>
            </Col>
            <Col span="8" class="txt">64-77</Col>
            <Col span="8">
            <p>森林狼</p>
            </Col>
          </Row>
          <Row>
            <Col span="8">
            <p>1-1</p>
            </Col>
            <Col span="8">
            <Icon type="ios-basketball" />
            </Col>
            <Col span="8">
            <p>2-0</p>
            </Col>
          </Row>
        </Card>
        </Col>
        <Col span="7">
        <Card class="margin">
          <Row>
            <Col span="8">
            <p>公牛</p>
            </Col>
            <Col span="8" class="txt">55-63</Col>
            <Col span="8">
            <p>火箭</p>
            </Col>
          </Row>
          <Row>
            <Col span="8">
            <p>1-1</p>
            </Col>
            <Col span="8">
            <Icon type="ios-basketball" />
            </Col>
            <Col span="8">
            <p>2-0</p>
            </Col>
          </Row>
        </Card>
        </Col>
        <Col span="7">
        <Card class="margin">
          <Row>
            <Col span="8">
            <p>CHN</p>
            </Col>
            <Col span="8" class="time">11:00</Col>
            <Col span="8">
            <p>黄蜂</p>
            </Col>
          </Row>
          <Row>
            <Col span="8">
            <p>0-1</p>
            </Col>
            <Col span="8">
            <Icon type="ios-basketball" />
            </Col>
            <Col span="8">
            <p>2-0</p>
            </Col>
          </Row>
        </Card>
        </Col>
        <Col span="3"><Button type="text" size="large" to="schedule/schedule_page" >更多赛程>></Button></Col>
      </Row>
    </Card>
    </Col>
  </Row>
  <Row>
    <Col span="15">
    <Card class="bor">
      <Carousel autoplay v-model="value2" loop>
        <CarouselItem>
          <div class="demo-carousel"><img src="@/assets/images/1.png" width="550" height="480" > </div>
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
    <Col span="9">
    <Card>
      <Row>
        <Col span="6"><p>最新资讯</p></Col>
        <Col span="">
        <Button type="text" class="more">换一批</Button>
        </Col>
      </Row>
      <Row>

        <Col span="9">
        <img src="@/assets/images/1.png" width="80" height="80">
        </Col>
        <Col span="15" class="txt1">
        <a href=""><router-link  :to="{ path: '/new/new'}">21世纪各队最佳扣篮，麦迪惊世骑扣</router-link></a>
        </Col>
      </Row>
      <Row>
        <Col span="9">
        <img src="@/assets/images/2.jpg" width="80" height="80">
        </Col>
        <Col span="15">
        <a href="">伯克斯：科尔说服我加盟勇士 在这里能赢球</a>
        </Col>
      </Row>
      <Row>
        <Col span="9">
        <img src="@/assets/images/3.jpg" width="80" height="80">
        </Col>
        <Col span="15" class="txt1">
       <a href="">霍华德：感谢科比骂我软蛋 后来才明白意思</a>
        </Col>
      </Row>
      <Row>
        <Col span="9">
        <img src="@/assets/images/4.jpg" width="80" height="80">
        </Col>
        <Col span="15" class="txt1">
         <a href="">21世纪各队最佳扣篮，麦迪惊世骑扣</a>
        </Col>
      </Row>
      <Row>
        <Col span="9">
        <img src="@/assets/images/1.png" width="80" height="80">
        </Col>
        <Col span="15" class="txt1">
        <a href="">伯克斯：科尔说服我加盟勇士 在这里能赢球</a>
        </Col>
      </Row>

    </Card>

    </Col>
    <!-- <Col span="6">
    <Card>
      <Row>
        <Col span="">
        <Button type="text" class="more">换一换</Button>
        </Col>
      </Row>
      <Row>
        <Col span=""><a href="">曝前4号秀德拉甘-本德尔将前往俄罗斯打球</a> </Col>
        <Col span=""><a href="">伯克斯：科尔说服我加盟勇士 在这里能赢球</a> </Col>
        <Col span=""><a href="">霍华德：感谢科比骂我软蛋 后来才明白意思</a> </Col>
        <Col span=""><a href="">曝前4号秀德拉甘-本德尔将前往俄罗斯打球</a> </Col>
        <Col span=""><a href="">伯克斯：科尔说服我加盟勇士 在这里能赢球</a> </Col>
        <Col span=""><a href="">霍华德：感谢科比骂我软蛋 后来才明白意思</a> </Col>
        <Col span=""><a href="">曝前4号秀德拉甘-本德尔将前往俄罗斯打球</a> </Col>
        <Col span=""><a href="">伯克斯：科尔说服我加盟勇士 在这里能赢球</a> </Col>
        <Col span=""><a href="">霍华德：感谢科比骂我软蛋 后来才明白意思</a> </Col>
        <Col span=""><a href="">伯克斯：科尔说服我加盟勇士 在这里能赢球</a> </Col>
     


      </Row>
    </Card>
    </Col> -->

  </Row>
</div>
</template>


<script>
export default {
  data() {
    return {
      value1: '2019-07-18',
      value2: 0
    }
  }
}
</script>
<style>
.margin{
  position: relative;
  margin-left:10px;
}
.btn {
  text-align: center;
  background-color: rgb(118, 225, 252);
}

.txt {
  color: red;
  font-weight: 700;
}

.time {
  color: green;
  font-weight: 700;
}

.tp {
  position: relative;
  top: -40px;
  color: white;
  font-size: 18px;
  background-color: black;
}

.more {
  position: relative;

  left: 170px;
  color: rgb(6, 184, 184);
  font-size: 14px;
}
</style>

<!--<template>
<div>
  <img src="@/assets/images/tool-logo.png" alt=" ">
</div>
</template>

<script>
import InforCard from '_c/info-card'
import CountTo from '_c/count-to'
import {
  ChartAny
} from "_c/charts"
import {
  ChartPie,
  ChartBar
} from '_c/charts'
import Example from './example.vue'
export default {
  name: 'home',
  components: {
    InforCard,
    CountTo,
    ChartPie,
    ChartBar,
    Example,
    ChartAny,
  },
  data() {
    return {

    }
  },
  methods: {

  },
  mounted() {

  }
}
</script>

<style lang="less">
.count-style {
  font-size: 50px;
}

;
.rgba {
  background-color: FFFFFF;
}

;
.circle {
  text-align: center
}

;
</style>-->




