<template>
    <div>
        <el-row :gutter="20">
            <el-col :span="8">
                <el-card shadow="hover" class="mgb20" style="height: 252px">
                    <div class="user-info">
                        <img src="../../assets/img/img.jpg" class="user-avator" alt />
                        <div class="user-info-cont">
                            <div class="user-info-name">{{ name }}</div>
                            <div>{{ role }}</div>
                        </div>
                    </div>
                    <div class="user-info-list">
                        上次登录地点：
                        <span>北京</span>
                    </div>
                </el-card>
            </el-col>
            <el-col :span="16">
                <el-row :gutter="20" class="mgb20" style="margin-top: ">
                    <el-col :span="8">
                        <el-card shadow="hover" :body-style="{ padding: '0px' }">
                            <div class="grid-content grid-con-1">
                                <i class="el-icon-user grid-con-icon"></i>
                                <div class="grid-cont-right">
                                    <div class="grid-num">4396</div>
                                    <div>用户访问量</div>
                                </div>
                            </div>
                        </el-card>
                    </el-col>
                    <el-col :span="8">
                        <el-card shadow="hover" :body-style="{ padding: '0px' }">
                            <div class="grid-content grid-con-2">
                                <i class="el-icon-upload grid-con-icon"></i>
                                <div class="grid-cont-right">
                                    <div class="grid-num">23</div>
                                    <div>上传次数</div>
                                </div>
                            </div>
                        </el-card>
                    </el-col>
                    <el-col :span="8">
                        <el-card shadow="hover" :body-style="{ padding: '0px' }">
                            <div class="grid-content grid-con-3">
                                <i class="el-icon-download grid-con-icon"></i>
                                <div class="grid-cont-right">
                                    <div class="grid-num">88</div>
                                    <div>下载次数</div>
                                </div>
                            </div>
                        </el-card>
                    </el-col>
                </el-row>
                <el-row :gutter="20" class="mgb20">
                    <el-col :span="8">
                        <el-card shadow="hover" :body-style="{ padding: '0px' }">
                            <div class="grid-content grid-con-1">
                                <i class="el-icon-lx-people grid-con-icon"></i>
                                <div class="grid-cont-right">
                                    <div class="grid-num">12</div>
                                    <div>用户数</div>
                                </div>
                            </div>
                        </el-card>
                    </el-col>
                    <el-col :span="8">
                        <el-card shadow="hover" :body-style="{ padding: '0px' }">
                            <div class="grid-content grid-con-2">
                                <i class="el-icon-ship grid-con-icon"></i>
                                <div class="grid-cont-right">
                                    <div class="grid-num">15</div>
                                    <div>船舶数量</div>
                                </div>
                            </div>
                        </el-card>
                    </el-col>
                    <el-col :span="8">
                        <el-card shadow="hover" :body-style="{ padding: '0px' }">
                            <div class="grid-content grid-con-3">
                                <i class="el-icon-trophy grid-con-icon"></i>
                                <div class="grid-cont-right">
                                    <div class="grid-num">5000KM</div>
                                    <div>总里程</div>
                                </div>
                            </div>
                        </el-card>
                    </el-col>
                </el-row>
            </el-col>
        </el-row>
        <el-row :gutter="20">
            <el-col :span="12">
                <el-card shadow="hover">
                    <v-chart class="chart" :option="in_option" />
                </el-card>
            </el-col>
            <el-col :span="12">
                <el-card shadow="hover">
                    <v-chart class="chart" :option="out_option" />
                </el-card>
            </el-col>
        </el-row>
        <el-row>
            <h4>堆存信息可视化</h4>
        </el-row>
        <div class="container">
            <div class="drag-box">
                <div class="drag-box-item" v-for="item in info" :key="item.id">
                    <div class="item-title">{{ item.bw }}</div>
                    <draggable :options="dragOptions">
                        <transition-group tag="div" id="" class="item-ul">
                            <div v-for="cargo in item.cargo" :key="cargo.id">
                                <div v-if="cargo.danger_count == 1" class="drag-list_red" key="1">危险箱</div>
                                <div v-if="cargo.normal_count == 1" class="drag-list_yellow" key="2">普通箱</div>
                                <div v-if="cargo.cold_count == 1" class="drag-list_blue" key="3">冷藏箱</div>
                                <div v-if="cargo.over_count == 1" class="drag-list_brown" key="4">超限箱</div>
                                <div v-if="cargo.null_count == 1" class="drag-list" key="4">空箱</div>
                            </div>
                        </transition-group>
                    </draggable>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import draggable from 'vuedraggable';
// import Schart from 'vue-schart';
import bus from '../common/bus';
import { use } from 'echarts/core';
import { CanvasRenderer } from 'echarts/renderers';
import { PieChart } from 'echarts/charts';
import { TitleComponent, TooltipComponent, LegendComponent } from 'echarts/components';
import VChart, { THEME_KEY } from 'vue-echarts';

use([CanvasRenderer, PieChart, TitleComponent, TooltipComponent, LegendComponent]);
export default {
    name: 'dashboard',
    components: {
        VChart,
        draggable
    },
    provide: {
        [THEME_KEY]: 'dark'
    },
    data() {
        return {
            dragOptions: {
                animation: 120,
                scroll: true,
                group: 'sortlist',
                ghostClass: 'ghost-style'
            },
            name: localStorage.getItem('ms_username'),
            info: [],

            in_option: {
                title: {
                    text: '船舶进口占比',
                    left: 'center'
                },
                tooltip: {
                    trigger: 'item',
                    formatter: '{a} <br/>{b} : {c} ({d}%)'
                },
                legend: {
                    orient: 'vertical',
                    left: 'left',
                    data: ['美途马士基207EI-214W', '马斯特里赫特马士基209EI-218W', '马士基哈利法克斯211EI-217W']
                },
                series: [
                    {
                        name: '船舶进口占比',
                        type: 'pie',
                        radius: '55%',
                        center: ['50%', '60%'],
                        data: [
                            { value: 1790, name: '美途马士基207EI-214W' },
                            { value: 1591, name: '马斯特里赫特马士基209EI-218W' },
                            { value: 2948, name: '马士基哈利法克斯211EI-217W' }
                        ],
                        emphasis: {
                            itemStyle: {
                                shadowBlur: 10,
                                shadowOffsetX: 0,
                                shadowColor: 'rgba(0, 0, 0, 0.5)'
                            }
                        }
                    }
                ]
            },
            out_option: {
                title: {
                    text: '船舶出口占比',
                    left: 'center'
                },
                tooltip: {
                    trigger: 'item',
                    formatter: '{a} <br/>{b} : {c} ({d}%)'
                },
                legend: {
                    orient: 'vertical',
                    left: 'left',
                    data: ['美途马士基207EI-214W', '马斯特里赫特马士基209EI-218W', '马士基哈利法克斯211EI-217W']
                },
                series: [
                    {
                        name: '船舶出口占比',
                        type: 'pie',
                        radius: '55%',
                        center: ['50%', '60%'],
                        data: [
                            { value: 1244, name: '美途马士基207EI-214W' },
                            { value: 2362, name: '马斯特里赫特马士基209EI-218W' },
                            { value: 1801, name: '马士基哈利法克斯211EI-217W' }
                        ],
                        emphasis: {
                            itemStyle: {
                                shadowBlur: 10,
                                shadowOffsetX: 0,
                                shadowColor: 'rgba(0, 0, 0, 0.5)'
                            }
                        }
                    }
                ]
            },
            
        };
    },
    computed: {
        role() {
            return this.name === 'admin' ? '超级管理员' : '普通用户';
        }
    },
    created() {
        this.init_data();
        // this.handleListener();
        // this.changeDate();
    },
    // activated() {
    //     this.handleListener();
    // },
    // deactivated() {
    //     window.removeEventListener('resize', this.renderChart);
    //     bus.$off('collapse', this.handleBus);
    // },
    methods: {
        init_data() {
            for (var i = 0; i <= 12; i++) {
                let temp_cargo = [];
                for (var j = 0; j <= 18; j++) {
                    let a = Math.random(1, 10) * 15;
                    // console.log(a);
                    let t_danger_count = 0;
                    let t_normal_count = 0;
                    let t_cold_count = 0;
                    let t_over_count = 0;
                    let t_null_count = 0;
                    if (a < 3) {
                        t_danger_count = 1;
                    } else if (a < 6) {
                        t_normal_count = 1;
                    } else if (a < 9) {
                        t_cold_count = 1;
                    } else if (a < 12) {
                        t_over_count = 1;
                    } else {
                        t_null_count = 1;
                    }
                    temp_cargo.push({
                        id: j,
                        danger_count: t_danger_count,
                        normal_count: t_normal_count,
                        cold_count: t_cold_count,
                        over_count: t_over_count,
                        null_count: t_null_count
                    });
                }
                this.info.push({
                    id: i,
                    bw: i + 1,
                    cargo: temp_cargo
                });
            }
            // console.log(this.info);
        },
        changeDate() {
            const now = new Date().getTime();
            this.data.forEach((item, index) => {
                const date = new Date(now - (6 - index) * 86400000);
                item.name = `${date.getFullYear()}/${date.getMonth() + 1}/${date.getDate()}`;
            });
        }
        // handleListener() {
        //     bus.$on('collapse', this.handleBus);
        //     // 调用renderChart方法对图表进行重新渲染
        //     window.addEventListener('resize', this.renderChart);
        // },
        // handleBus(msg) {
        //     setTimeout(() => {
        //         this.renderChart();
        //     }, 200);
        // },
        // renderChart() {
        //     this.$refs.bar.renderChart();
        //     this.$refs.line.renderChart();
        // }
    }
};
</script>


<style scoped>
.drag-box {
    display: flex;
    user-select: none;
    text-align: center;
}
.drag-box-item {
    flex: 1;
    /* max-width: 330px; */
    /* min-width: 300px; */
    background-color: #eff1f5;
    margin-right: 16px;
    border-radius: 6px;
    border: 1px #e1e4e8 solid;
}
.chart {
    height: 400px;
}
.el-row {
    margin-bottom: 20px;
}

.grid-content {
    display: flex;
    align-items: center;
    height: 100px;
}

.grid-cont-right {
    flex: 1;
    text-align: center;
    font-size: 14px;
    color: #999;
}

.grid-num {
    font-size: 30px;
    font-weight: bold;
}

.grid-con-icon {
    font-size: 50px;
    width: 100px;
    height: 100px;
    text-align: center;
    line-height: 100px;
    color: #fff;
}

.grid-con-1 .grid-con-icon {
    background: rgb(45, 140, 240);
}

.grid-con-1 .grid-num {
    color: rgb(45, 140, 240);
}

.grid-con-2 .grid-con-icon {
    background: rgb(100, 213, 114);
}

.grid-con-2 .grid-num {
    color: rgb(45, 140, 240);
}

.grid-con-3 .grid-con-icon {
    background: rgb(242, 94, 67);
}

.grid-con-3 .grid-num {
    color: rgb(242, 94, 67);
}

.user-info {
    display: flex;
    align-items: center;
    padding-bottom: 20px;
    border-bottom: 2px solid #ccc;
    margin-bottom: 20px;
}

.user-avator {
    width: 120px;
    height: 120px;
    border-radius: 50%;
}

.user-info-cont {
    padding-left: 50px;
    flex: 1;
    font-size: 14px;
    color: #999;
}

.user-info-cont div:first-child {
    font-size: 30px;
    color: #222;
}

.user-info-list {
    font-size: 14px;
    color: #999;
    line-height: 25px;
}

.user-info-list span {
    margin-left: 70px;
}

.mgb20 {
    margin-bottom: 20px;
}

.todo-item {
    font-size: 14px;
}

.todo-item-del {
    text-decoration: line-through;
    color: #999;
}

.schart {
    width: 100%;
    height: 300px;
}
.drag-list {
    border: 1px #e1e4e8 solid;
    padding: 10px;
    margin: 5px 0 10px;
    list-style: none;
    background-color: #fff;
    border-radius: 6px;
    cursor: pointer;
    -webkit-transition: border 0.3s ease-in;
    transition: border 0.3s ease-in;
}
.drag-list:hover {
    border: 1px solid #20a0ff;
}

.drag-list_red {
    border: 1px #e1e4e8 solid;
    padding: 10px;
    margin: 5px 0 10px;
    list-style: none;
    background-color: orangered;
    border-radius: 6px;
    cursor: pointer;
    -webkit-transition: border 0.3s ease-in;
    transition: border 0.3s ease-in;
}
.drag-list_red:hover {
    border: 1px solid #20a0ff;
}
.drag-list_blue {
    border: 1px #e1e4e8 solid;
    padding: 10px;
    margin: 5px 0 10px;
    list-style: none;
    background-color: rgb(166, 206, 207);
    border-radius: 6px;
    cursor: pointer;
    -webkit-transition: border 0.3s ease-in;
    transition: border 0.3s ease-in;
}
.drag-list_blue:hover {
    border: 1px solid #20a0ff;
}
.drag-list_yellow {
    border: 1px #e1e4e8 solid;
    padding: 10px;
    margin: 5px 0 10px;
    list-style: none;
    background-color: rgba(230, 238, 120, 0.438);
    border-radius: 6px;
    cursor: pointer;
    -webkit-transition: border 0.3s ease-in;
    transition: border 0.3s ease-in;
}
.drag-list_yellow:hover {
    border: 1px solid #20a0ff;
}
.drag-list_brown {
    border: 1px #e1e4e8 solid;
    padding: 10px;
    margin: 5px 0 10px;
    list-style: none;
    background-color: rgb(240, 147, 40);
    border-radius: 6px;
    cursor: pointer;
    -webkit-transition: border 0.3s ease-in;
    transition: border 0.3s ease-in;
}
.drag-list_brown:hover {
    border: 1px solid #20a0ff;
}

.drag-title {
    font-weight: 400;
    line-height: 25px;
    margin: 10px 0;
    font-size: 22px;
    color: #1f2f3d;
}
.item-title {
    padding: 8px 8px 8px 12px;
    font-size: 14px;
    line-height: 1.5;
    color: #24292e;
    font-weight: 600;
}
.item-ul {
    padding: 0 8px 8px;
    height: 500px;
    overflow-y: scroll;
}
.item-ul::-webkit-scrollbar {
    width: 0;
}
.drag-list {
    border: 1px #e1e4e8 solid;
    padding: 10px;
    margin: 5px 0 10px;
    list-style: none;
    background-color: #fff;
    border-radius: 6px;
    cursor: pointer;
    -webkit-transition: border 0.3s ease-in;
    transition: border 0.3s ease-in;
}
.drag-list:hover {
    border: 1px solid #20a0ff;
}
.drag-title {
    font-weight: 400;
    line-height: 25px;
    margin: 10px 0;
    font-size: 22px;
    color: #1f2f3d;
}
.ghost-style {
    display: block;
    color: transparent;
    border-style: dashed;
}
</style>
