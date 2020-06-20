<template>
    <div>
        <Row >
          <Col span="24">
            <Card>
              <Row>
                <Col span="" style="font-size:24px;font-weight:700;"><P>亚特兰大 老鹰</P></Col>
                <Col span="8"><p>东部联盟中排名#12</p></Col>
                  <Col span="8"><p>教练：罗伊德 皮尔斯</p></Col>
                <Col span="8"><p>29胜-53负</p></Col>
                  
              </Row>
            </Card>
          </Col>
       
        </Row>
        <Row >
          <Col span="24">
            <Card>
              <Row >
                <Col span="20"><p>常规赛数据</p></Col>
                <Col span="4"><a href=""><router-link  :to="{ path: '/team/ranking_page'}">球队排名</router-link></a></Col>
              </Row>
            </Card>
          </Col>
            
          
        </Row>
        <Row >
          <Col span="">
            <Card>
              <Table height="400" :columns="columns1" :data="data2"></Table>
            </Card>
          </Col>
        </Row>
    </div>
</template>
<script>
    export default {
        data () {
            return {
                columns1: [
                    {
                        title: '年度',
                        key: 'year',
                         "fixed": "left",
                        "width": 100
                    },
                    
                     {
                        "title": "场数",
                        "key": "numbers",
                        "width": 100,
                        "sortable": true,
                        filters: [
                            {
                                label: 'Greater than 4000',
                                value: 1
                            },
                            {
                                label: 'Less than 4000',
                                value: 2
                            }
                        ],
                        filterMultiple: false,
                        filterMethod (value, row) {
                            if (value === 1) {
                                return row.numbers > 4000;
                            } else if (value === 2) {
                                return row.numbers < 4000;
                            }
                        }
                    },
                   
                    {
                        title: '命中',
                        key: 'mz',
                        "width": 100,
                        "sortable": true,
                    },
                    {
                        title: '出手',
                        key: 'cs',
                        "width": 100,
                        "sortable": true,
                    },
                    {
                        title: '三分命中',
                        key: 'sfmz',
                        "width": 100,
                        "sortable": true,
                    },
                    {
                        title: '三分出手',
                        key: 'sfcs',
                        "width": 100,
                        "sortable": true,
                    },
                    {
                        title: '罚球命中',
                        key: 'fqmz',
                        "width": 100,
                        "sortable": true,
                    },
                    {
                        title: '罚球出手',
                        key: 'fqcs',
                        "width": 100,
                        "sortable": true,
                    },
                    {
                        title: '进攻',
                        key: 'jg',
                        "width": 100,
                        "sortable": true,
                    },
                    {
                        title: '防守',
                        key: 'fs',
                        "width": 100,
                        "sortable": true,
                    },
                    {
                        title: '篮板',
                        key: 'lb',
                        "width": 100,
                        "sortable": true,
                    },
                    {
                        title: '助攻',
                        key: 'zg',
                        "width": 100,
                        "sortable": true,
                    },
                    {
                        title: '抢断',
                        key: 'qd',
                        "width": 100,
                        "sortable": true,
                    },
                    {
                        title: '盖帽',
                        key: 'gm',
                        "width": 100,
                        "sortable": true,
                    },
                    {
                        title: '失误',
                        key: 'sw',
                        "width": 100,
                        "sortable": true,
                    },
                    {
                        title: '犯规',
                        key: 'fg',
                        "width": 100,
                        "sortable": true,
                    },
                    {
                        title: '得分',
                        key: 'score',
                        "width": 100,
                        "sortable": true,
                    }
                ],
                data2: [
                    {
                    year:'2018赛季',
                    numbers:'82',
                    mz:'3392',
                    cs:'7524',
                    sfmz:'1067',
                    sfcs:'3034',
                    fqmz:'1443',
                    fqcs:'1918',
                    jg:'955',
                    fs:'2825',
                    lb:'3780',
                    zg:'2118',
                    qd:'675',
                    gm:'419',
                    sw:'1397',
                    fg:'1932',
                    score:'9294'
                    },
                     {
                    year:'2017赛季',
                    numbers:'82',
                    mz:'3392',
                    cs:'7524',
                    sfmz:'1067',
                    sfcs:'3034',
                    fqmz:'1443',
                    fqcs:'1918',
                    jg:'955',
                    fs:'2825',
                    lb:'3780',
                    zg:'2118',
                    qd:'675',
                    gm:'419',
                    sw:'1397',
                    fg:'1932',
                    score:'9294'
                    },
                     {
                    year:'2016赛季',
                    numbers:'82',
                    mz:'3392',
                    cs:'7524',
                    sfmz:'1067',
                    sfcs:'3034',
                    fqmz:'1443',
                    fqcs:'1918',
                    jg:'955',
                    fs:'2825',
                    lb:'3780',
                    zg:'2118',
                    qd:'675',
                    gm:'419',
                    sw:'1397',
                    fg:'1932',
                    score:'9294'
                    }
                 
                ]
            }
        }
    }
</script>
 
 
 
 
