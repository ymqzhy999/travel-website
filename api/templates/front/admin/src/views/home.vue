<template>
<div class="content">
	<div class="text" :style='{"margin":"50px auto","fontSize":"24px","color":"rgb(51, 51, 51)","textAlign":"center","fontWeight":"bold"}'>欢迎使用 {{this.$project.projectName}}</div>
    <div class="cardView">
        <div class="cards" :style='{"margin":"0 0 20px 0","alignItems":"center","flexDirection":"column","justifyContent":"center","display":"flex"}'>
			<div :style='{"boxShadow":"0 1px 6px rgba(0,0,0,.3)","margin":"3px 10px","borderRadius":"40px","display":"flex"}' v-if="isAuth('jingdianmenpiao','首页总数')">
				<div :style='{"width":"80px","background":"#ffc523","height":"80px"}'></div>
				<div :style='{"width":"160px","alignItems":"center","flexDirection":"column","justifyContent":"center","display":"flex"}'>
					<div :style='{"margin":"5px 0","lineHeight":"24px","fontSize":"20px","color":"#333","fontWeight":"bold","height":"24px"}'>{{jingdianmenpiaoCount}}</div>
					<div :style='{"margin":"5px 0","lineHeight":"24px","fontSize":"16px","color":"#666","height":"24px"}'>景点门票总数</div>
				</div>
			</div>
        </div>
        <div style="display: flex;align-items: center;width: 100%;margin-bottom: 10px;">
            <el-card style="width: 33.3%;margin: 0 10px;" v-if="isAuth('jingdianmenpiao','首页统计')">
                <div id="jingdianmenpiaoChart1" style="width:100%;height:400px;"></div>
            </el-card>
            <el-card style="width: 33.3%;margin: 0 10px;" v-if="isAuth('jingdianmenpiao','首页统计')">
                <div id="jingdianmenpiaoChart2" style="width:100%;height:400px;"></div>
            </el-card>
            <el-card style="width: 33.3%;margin: 0 10px;" v-if="isAuth('jingdianmenpiao','首页统计')">
                <div id="jingdianmenpiaoChart3" style="width:100%;height:400px;"></div>
            </el-card>
        </div>
    </div>
</div>
</template>
<script>
//3
import router from '@/router/router-static'
import * as echarts from 'echarts'
export default {
	data() {
		return {
            jingdianmenpiaoCount: 0,
		};
	},
  mounted(){
    this.init();
    this.getjingdianmenpiaoCount();
    this.jingdianmenpiaoChat1();
    this.jingdianmenpiaoChat2();
    this.jingdianmenpiaoChat3();
  },
  methods:{
    init(){
        if(this.$storage.get('Token')){
        this.$http({
            url: `${this.$storage.get('sessionTable')}/session`,
            method: "get"
        }).then(({ data }) => {
            if (data && data.code != 0) {
            router.push({ name: 'login' })
            }
        });
        }else{
            router.push({ name: 'login' })
        }
    },
    getjingdianmenpiaoCount() {
        this.$http({
            url: `jingdianmenpiao/count`,
            method: "get"
        }).then(({
            data
        }) => {
            if (data && data.code == 0) {
                this.jingdianmenpiaoCount = data.data
            }
        })
    },

    jingdianmenpiaoChat1() {
      this.$nextTick(()=>{

        var jingdianmenpiaoChart1 = echarts.init(document.getElementById("jingdianmenpiaoChart1"),'macarons');
        this.$http({
            url: "jingdianmenpiao/group/dianping",
            method: "get",
        }).then(({ data }) => {
            if (data && data.code === 0) {
                let res = data.data;
                let xAxis = [];
                let yAxis = [];
                let pArray = []
                for(let i=0;i<res.length;i++){
                    xAxis.push(res[i].dianping);
                    yAxis.push(parseFloat((res[i].total)));
                    pArray.push({
                        value: parseFloat((res[i].total)),
                        name: res[i].dianping
                    })
                }
                var option = {};
                option = {
                        title: {
                            text: '景点评分',
                            left: 'center'
                        },
                        tooltip: {
                          trigger: 'item',
                          formatter: '{b} : {c} ({d}%)'
                        },
                        series: [
                            {
                                type: 'pie',
                                radius: '55%',
                                center: ['50%', '60%'],
                                data: pArray,
                                emphasis: {
                                    itemStyle: {
                                        shadowBlur: 10,
                                        shadowOffsetX: 0,
                                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                                    }
                                }
                            }
                        ]
                };
                // 使用刚指定的配置项和数据显示图表。
                jingdianmenpiaoChart1.setOption(option);
                  //根据窗口的大小变动图表
                window.onresize = function() {
                    jingdianmenpiaoChart1.resize();
                };
            }
        });
      })
    },

    jingdianmenpiaoChat2() {
      this.$nextTick(()=>{
        // biaoti biaoti
        //  jiage

        var jingdianmenpiaoChart2 = echarts.init(document.getElementById("jingdianmenpiaoChart2"),'macarons');
        this.$http({
            url: `jingdianmenpiao/value/biaoti/jiage`,
            method: "get",
        }).then(({ data }) => {
            if (data && data.code === 0) {
                let res = data.data;
                let xAxis = [];
                let yAxis = [];
                let pArray = []
                for(let i=0;i<res.length;i++){
                    xAxis.push(res[i].biaoti);
                    yAxis.push(parseFloat((res[i].total)));
                    pArray.push({
                        value: parseFloat((res[i].total)),
                        name: res[i].biaoti
                    })
                }
                var option = {};
                option = {
                    title: {
                        text: '景点价格',
                        left: 'center'
                    },
                    tooltip: {
                      trigger: 'item',
                      formatter: '{b} : {c}'
                    },
                    xAxis: {
                        type: 'category',
                        boundaryGap: false,
                        data: xAxis
                    },
                    yAxis: {
                        type: 'value'
                    },
                    series: [{
                        data: yAxis,
                        type: 'line',
                    }]
                };
                // 使用刚指定的配置项和数据显示图表。
                jingdianmenpiaoChart2.setOption(option);
                  //根据窗口的大小变动图表
                window.onresize = function() {
                    jingdianmenpiaoChart2.resize();
                };
            }
        });
      })
    },

    jingdianmenpiaoChat3() {
      this.$nextTick(()=>{

        var jingdianmenpiaoChart3 = echarts.init(document.getElementById("jingdianmenpiaoChart3"),'macarons');
        this.$http({
            url: "jingdianmenpiao/group/pinglun",
            method: "get",
        }).then(({ data }) => {
            if (data && data.code === 0) {
                let res = data.data;
                let xAxis = [];
                let yAxis = [];
                let pArray = []
                for(let i=0;i<res.length;i++){
                    xAxis.push(res[i].pinglun);
                    yAxis.push(parseFloat((res[i].total)));
                    pArray.push({
                        value: parseFloat((res[i].total)),
                        name: res[i].pinglun
                    })
                }
                var option = {};
                option = {
                        title: {
                            text: '景点评论',
                            left: 'center'
                        },
                        tooltip: {
                          trigger: 'item',
                          formatter: '{b} : {c} ({d}%)'
                        },
                        series: [
                            {
                                type: 'pie',
                                radius: ['25%', '55%'],
                                center: ['50%', '60%'],
                                data: pArray,
                                emphasis: {
                                    itemStyle: {
                                        shadowBlur: 10,
                                        shadowOffsetX: 0,
                                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                                    }
                                }
                            }
                        ]
                };
                // 使用刚指定的配置项和数据显示图表。
                jingdianmenpiaoChart3.setOption(option);
                  //根据窗口的大小变动图表
                window.onresize = function() {
                    jingdianmenpiaoChart3.resize();
                };
            }
        });
      })
    },




  }
};
</script>
<style lang="scss" scoped>
    .cardView {
        display: flex;
        flex-wrap: wrap;
        width: 100%;

        .cards {
            display: flex;
            align-items: center;
            width: 100%;
            margin-bottom: 10px;
            justify-content: center;
            .card {
                width: calc(25% - 20px);
                margin: 0 10px;
                ::v-deep.el-card__body{
                    padding: 0;
                }
            }
        }
    }
</style>
