# backgroundsystemDemo
vue+django+mysql的一个船舶信息管理的demo

前端vue后端django数据库mysql

首页：
简单的数据图表展示
有个draggable组件，可拖拽的，效果看起来很不错

![1](https://user-images.githubusercontent.com/89622860/169769006-54c87d0a-ef27-4e33-bb0a-2a812bf10970.jpg)



数据页面：
基本的文件上传 数据解析 图表展示这些

![2](https://user-images.githubusercontent.com/89622860/169769020-a5304126-8f2b-450a-90e3-d61dfa940708.jpg)


用户管理：
基本的用户管理功能


![3](https://user-images.githubusercontent.com/89622860/169769035-79ace9af-6f7e-407b-bfd3-877dd3b836e5.jpg)


生成数据是利用的xlwt写成excel，然后后端读取excel转成文件流传给前端完成下载
