import Vue from 'vue';
import Router from 'vue-router';

Vue.use(Router);

export default new Router({
    routes: [
        {
            path: '/',
            redirect: '/dashboard'
        },
        {
            path: '/',
            component: () => import(/* webpackChunkName: "home" */ '../components/common/Home.vue'),
            meta: { title: '自述文件' },
            children: [
                {
                    path: '/dashboard',
                    component: () => import(/* webpackChunkName: "dashboard" */ '../components/page/Dashboard.vue'),
                    meta: { title: '系统首页' }
                },
                {
                    path: '/portinfo',
                    component: () => import(/* webpackChunkName: "table" */ '../components/page/portinfo.vue'),
                    meta: { title: '在港作业信息管理' }
                },
                {
                    path: '/table',
                    component: () => import(/* webpackChunkName: "table" */ '../components/page/BaseTable.vue'),
                    meta: { title: '用户管理' }
                },
                {
                    path: '/shipinfo',
                    component: () => import(/* webpackChunkName: "shipinfo" */ '../components/page/shipinfo.vue'),
                    meta: { title: '船舶信息管理' }
                },
                {
                    path: '/operationplan',
                    component: () => import(/* webpackChunkName: "shipinfo" */ '../components/page/operationplan.vue'),
                    meta: { title: '作业计划编制' }
                },
                {
                    path: '/cargostorage_in',
                    component: () => import(/* webpackChunkName: "shipinfo" */ '../components/page/cargostorage_in.vue'),
                    meta: { title: '货物堆存信息页面--进口' }
                },
                {
                    path: '/cargostorage_out',
                    component: () => import(/* webpackChunkName: "shipinfo" */ '../components/page/cargostorage_out.vue'),
                    meta: { title: '货物堆存信息页面--出口' }
                },
                {
                    path: '/cargolocation_in',
                    component: () => import(/* webpackChunkName: "shipinfo" */ '../components/page/cargolocation_in.vue'),
                    meta: { title: '货物货位信息页面--进口' }
                },
                {
                    path: '/cargolocation_out',
                    component: () => import(/* webpackChunkName: "shipinfo" */ '../components/page/cargolocation_out.vue'),
                    meta: { title: '货物货位信息页面--出口' }
                },
                {
                    path: '/schedule_in',
                    component: () => import(/* webpackChunkName: "shipinfo" */ '../components/page/schedule_in.vue'),
                    meta: { title: '进出口工作时间计划表--进口' }
                },
                {
                    path: '/schedule_out',
                    component: () => import(/* webpackChunkName: "shipinfo" */ '../components/page/schedule_out.vue'),
                    meta: { title: '进出口工作时间计划表--出口' }
                },
                {
                    // 拖拽列表组件
                    path: '/drag_in',
                    component: () => import(/* webpackChunkName: "drag" */ '../components/page/DragList_in.vue'),
                    meta: { title: '货物货位信息页面可视化--进口' }
                },
                {
                    // 拖拽列表组件
                    path: '/drag_out',
                    component: () => import(/* webpackChunkName: "drag" */ '../components/page/DragList_out.vue'),
                    meta: { title: '货物货位信息页面可视化--出口' }
                },
            ]
        },
        {
            path: '/login',
            component: () => import(/* webpackChunkName: "login" */ '../components/page/Login.vue'),
            meta: { title: '登录' }
        },
        {
            path: '*',
            redirect: '/404'
        }
    ]
});
