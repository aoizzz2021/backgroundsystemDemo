<template>
    <div class="sidebar">
        <el-menu
            class="sidebar-el-menu"
            :default-active="onRoutes"
            :collapse="collapse"
            background-color="#324157"
            text-color="#bfcbd9"
            active-text-color="#20a0ff"
            unique-opened
            router
        >
            <template v-for="item in items">
                <template v-if="item.subs">
                    <el-submenu :index="item.index" :key="item.index">
                        <template slot="title">
                            <i :class="item.icon"></i>
                            <span slot="title">{{ item.title }}</span>
                        </template>
                        <template v-for="subItem in item.subs">
                            <el-submenu v-if="subItem.subs" :index="subItem.index" :key="subItem.index">
                                <template slot="title">{{ subItem.title }}</template>
                                <el-menu-item v-for="(threeItem, i) in subItem.subs" :key="i" :index="threeItem.index">{{
                                    threeItem.title
                                }}</el-menu-item>
                            </el-submenu>
                            <el-menu-item v-else :index="subItem.index" :key="subItem.index"
                                ><i :class="subItem.icon"></i>{{ subItem.title }}</el-menu-item
                            >
                        </template>
                    </el-submenu>
                </template>
                <template v-else>
                    <el-menu-item :index="item.index" :key="item.index">
                        <i :class="item.icon"></i>
                        <span slot="title">{{ item.title }}</span>
                    </el-menu-item>
                </template>
            </template>
        </el-menu>
    </div>
</template>

<script>
import bus from '../common/bus';
export default {
    data() {
        return {
            collapse: false,
            items: [
                {
                    icon: 'el-icon-lx-home',
                    index: 'dashboard',
                    title: '系统首页'
                },
                {
                    icon: 'el-icon-ship',
                    index: 'shipinfo',
                    title: '船舶信息管理'
                },
                {
                    icon: 'el-icon-tickets',
                    index: 'portinfo',
                    title: '在港作业信息管理'
                },
                {
                    icon: 'el-icon-s-grid',
                    index: 'cargostorage',
                    title: '货物堆存信息页面',
                    subs: [
                        {
                            icon: 'el-icon-caret-left',
                            index: 'cargostorage_in',
                            title: '进口'
                        },
                        {
                            icon: 'el-icon-caret-right',
                            index: 'cargostorage_out',
                            title: '出口'
                        }
                    ]
                },
                {
                    icon: 'el-icon-s-grid',
                    index: 'cargolocation',
                    title: '货物货位信息页面',
                    subs: [
                        {
                            icon: 'el-icon-caret-left',
                            index: 'cargolocation_in',
                            title: '进口'
                        },
                        {
                            icon: 'el-icon-caret-right',
                            index: 'cargolocation_out',
                            title: '出口'
                        }
                    ]
                },
                {
                    icon: 'el-icon-pie-chart',
                    index: 'drag',
                    title: '货物堆存信息可视化',
                    subs: [
                        {
                            icon: 'el-icon-caret-left',
                            index: 'drag_in',
                            title: '进口'
                        },
                        {
                            icon: 'el-icon-caret-right',
                            index: 'drag_out',
                            title: '出口'
                        }
                    ]
                },
                {
                    icon: 'el-icon-date',
                    index: 'schedule',
                    title: '进出口工作时间计划表',
                    subs: [
                        {
                            icon: 'el-icon-caret-left',
                            index: 'schedule_in',
                            title: '进口'
                        },
                        {
                            icon: 'el-icon-caret-right',
                            index: 'schedule_out',
                            title: '出口'
                        }
                    ]
                },
                {
                    icon: 'el-icon-date',
                    index: 'operationplan',
                    title: '作业计划编制'
                },
                {
                    icon: 'el-icon-lx-cascades',
                    index: 'table',
                    title: '用户管理'
                }
            ],
            username:localStorage.getItem('ms_username'),
        };
    },
    computed: {
        onRoutes() {
            return this.$route.path.replace('/', '');
        }
    },
    created() {
        if(this.username != 'admin')
        {
            this.items = [
                {
                    icon: 'el-icon-lx-home',
                    index: 'dashboard',
                    title: '系统首页'
                },
                {
                    icon: 'el-icon-ship',
                    index: 'shipinfo',
                    title: '船舶信息管理'
                },
                {
                    icon: 'el-icon-tickets',
                    index: 'portinfo',
                    title: '在港作业信息管理'
                },
                {
                    icon: 'el-icon-s-grid',
                    index: 'cargostorage',
                    title: '货物堆存信息页面',
                    subs: [
                        {
                            icon: 'el-icon-caret-left',
                            index: 'cargostorage_in',
                            title: '进口'
                        },
                        {
                            icon: 'el-icon-caret-right',
                            index: 'cargostorage_out',
                            title: '出口'
                        }
                    ]
                },
                {
                    icon: 'el-icon-s-grid',
                    index: 'cargolocation',
                    title: '货物货位信息页面',
                    subs: [
                        {
                            icon: 'el-icon-caret-left',
                            index: 'cargolocation_in',
                            title: '进口'
                        },
                        {
                            icon: 'el-icon-caret-right',
                            index: 'cargolocation_out',
                            title: '出口'
                        }
                    ]
                },
                {
                    icon: 'el-icon-pie-chart',
                    index: 'drag',
                    title: '货物堆存信息可视化',
                    subs: [
                        {
                            icon: 'el-icon-caret-left',
                            index: 'drag_in',
                            title: '进口'
                        },
                        {
                            icon: 'el-icon-caret-right',
                            index: 'drag_out',
                            title: '出口'
                        }
                    ]
                },
                {
                    icon: 'el-icon-date',
                    index: 'schedule',
                    title: '进出口工作时间计划表',
                    subs: [
                        {
                            icon: 'el-icon-caret-left',
                            index: 'schedule_in',
                            title: '进口'
                        },
                        {
                            icon: 'el-icon-caret-right',
                            index: 'schedule_out',
                            title: '出口'
                        }
                    ]
                },
                {
                    icon: 'el-icon-date',
                    index: 'operationplan',
                    title: '作业计划编制'
                },
            ]
        }
        // 通过 Event Bus 进行组件间通信，来折叠侧边栏
        bus.$on('collapse', (msg) => {
            this.collapse = msg;
            bus.$emit('collapse-content', msg);
        });
    }
};
</script>

<style scoped>
.sidebar {
    display: block;
    position: absolute;
    left: 0;
    top: 70px;
    bottom: 0;
    overflow-y: scroll;
}
.sidebar::-webkit-scrollbar {
    width: 0;
}
.sidebar-el-menu:not(.el-menu--collapse) {
    width: 250px;
}
.sidebar > ul {
    height: 100%;
}
</style>
