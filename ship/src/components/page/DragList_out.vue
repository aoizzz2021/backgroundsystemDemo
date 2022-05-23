<template>
    <section class="main">
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-rank"></i> 货物堆存信息可视化</el-breadcrumb-item>
                <el-breadcrumb-item>出口可视化</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="container">
            <div class="plugins-tips">
                <el-select
                    v-model="selectedId"
                    filterable
                    placeholder="船舶名 必填项！！！"
                    class="handle-select mr10"
                    @change="selectchange"
                >
                    <el-option v-for="item in shipdata" :key="item.id" :label="item.ship_name" :value="item.id"></el-option>
                </el-select>
            </div>
            <div class="drag-box">
                <div class="drag-box-item" v-for="item in info" :key="item.id">
                    <div class="item-title">{{ item.bw }}</div>
                    <draggable v-model="todo" @remove="removeHandle" :options="dragOptions">
                        <transition-group tag="div" id="" class="item-ul">
                            <div v-if="item.danger_count ==1" class="drag-list_red" key="1">危险箱</div>
                            <div v-if="item.normal_count ==1" class="drag-list_yellow" key="2">普通箱</div>
                            <div v-if="item.cold_count ==1" class="drag-list_blue" key="3">冷藏箱</div>
                            <div v-if="item.over_count ==1" class="drag-list_brown" key="4">超限箱</div>
                        </transition-group>
                    </draggable>
                </div>
            </div>
            <!-- <div class="drag-box">
                <div class="drag-box-item">
                    <div class="item-title">07</div>
                    <draggable v-model="todo" @remove="removeHandle" :options="dragOptions">
                        <transition-group tag="div" id="todo" class="item-ul">
                            <div v-for="item in seven" :class="item.class" :key="item.id">
                                {{item.content}}
                            </div>
                        </transition-group>
                    </draggable>
                </div>
                <div class="drag-box-item">
                    <div class="item-title">06</div>
                    <draggable v-model="doing" @remove="removeHandle" :options="dragOptions">
                        <transition-group tag="div" id="doing" class="item-ul">
                            <div v-for="item in six" :class="item.class" :key="item.id">
                                {{item.content}}
                            </div>
                        </transition-group>
                    </draggable>
                </div>
                <div class="drag-box-item">
                    <div class="item-title">05</div>
                    <draggable v-model="done" @remove="removeHandle" :options="dragOptions">
                        <transition-group tag="div" id="done" class="item-ul">
                            <div v-for="item in five" :class="item.class" :key="item.id">
                                {{item.content}}
                            </div>
                        </transition-group>
                    </draggable>
                </div>
                <div class="drag-box-item">
                    <div class="item-title">04</div>
                    <draggable v-model="done" @remove="removeHandle" :options="dragOptions">
                        <transition-group tag="div" id="done" class="item-ul">
                            <div v-for="item in four" :class="item.class" :key="item.id">
                                {{item.content}}
                            </div>
                        </transition-group>
                    </draggable>
                </div>
                <div class="drag-box-item">
                    <div class="item-title">03</div>
                    <draggable v-model="done" @remove="removeHandle" :options="dragOptions">
                        <transition-group tag="div" id="done" class="item-ul">
                            <div v-for="item in three" :class="item.class" :key="item.id">
                                {{item.content}}
                            </div>
                        </transition-group>
                    </draggable>
                </div>
                <div class="drag-box-item">
                    <div class="item-title">02</div>
                    <draggable v-model="done" @remove="removeHandle" :options="dragOptions">
                        <transition-group tag="div" id="done" class="item-ul">
                            <div v-for="item in two" :class="item.class" :key="item.id">
                                {{item.content}}
                            </div>
                        </transition-group>
                    </draggable>
                </div>
                <div class="drag-box-item">
                    <div class="item-title">01</div>
                    <draggable v-model="done" @remove="removeHandle" :options="dragOptions">
                        <transition-group tag="div" id="done" class="item-ul">
                            <div v-for="item in one" :class="item.class" :key="item.id">
                                {{item.content}}
                            </div>
                        </transition-group>
                    </draggable>
                </div>
            </div> -->
        </div>
    </section>
</template>

<script>
import draggable from 'vuedraggable';
import Axios from 'axios';
export default {
    name: 'draglist',
    data() {
        return {
            dragOptions: {
                animation: 120,
                scroll: true,
                group: 'sortlist',
                ghostClass: 'ghost-style'
            },
            selectedId: '',
            shipdata: [],
            info: {
                sev: []
            }
        };
    },
    components: {
        draggable
    },
    created() {
        // this.getData();
        Axios.get(this.url.url + '/get_shipname').then((res) => {
            // console.log(res);
            this.shipdata = res.data.list;
        });
    },
    methods: {
        selectchange() {
            let param = new URLSearchParams();
            param.append('id', this.selectedId);
            Axios({
                method: 'post',
                url: this.url.url + '/post_outvis_data',
                data: param
            }).then((res) => {
                console.log(res);
                this.info = res.data.info;
            });
        },
        removeHandle(event) {
            console.log(event);
            this.$message.success(`从 ${event.from.id} 移动到 ${event.to.id} `);
        }
    }
};
</script>

<style scoped>
.drag-box {
    display: flex;
    user-select: none;
}
.drag-box-item {
    flex: 1;
    /* max-width: 330px;
        min-width: 300px; */
    background-color: #eff1f5;
    margin-right: 16px;
    border-radius: 6px;
    border: 1px #e1e4e8 solid;
}
.item-title {
    padding: 8px 8px 8px 12px;
    font-size: 24px;
    line-height: 1.5;
    color: #24292e;
    font-weight: 600;
    text-align: center;
}
.item-ul {
    padding: 0 8px 8px;
    height: 500px;
    overflow-y: scroll;
    text-align: center;
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
.ghost-style {
    display: block;
    color: transparent;
    border-style: dashed;
}
</style>
