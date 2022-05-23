<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item> <i class="el-icon-lx-cascades"></i> 进口货物货位信息 </el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="container">
            <div class="handle-box">
                <el-select
                    v-model="selectedId"
                    filterable
                    placeholder="船舶名 必填项！！！"
                    class="handle-select mr10"
                    @change="selectchange"
                >
                    <el-option v-for="item in shipdata" :key="item.id" :label="item.ship_name" :value="item.id"></el-option>
                </el-select>
                <el-button type="primary" icon="el-icon-download" @click="downloadFile">导出</el-button>
            </div>
            <el-table
                :data="tableData"
                border
                class="table"
                ref="multipleTable"
                header-cell-class-name="table-header"
                @selection-change="handleSelectionChange"
            >
                <!-- <el-table-column prop="id" label="ID" width="55" align="center"></el-table-column> -->
                <el-table-column prop="bw" label="岸桥"></el-table-column>
                <el-table-column prop="incount" label="进口"></el-table-column>
                <el-table-column prop="outcount" label="出口"></el-table-column>
                <el-table-column prop="allcount" label="总钩"></el-table-column>
                <el-table-column prop="inkcg" label="开舱盖"></el-table-column>
                <el-table-column prop="incxx" label="卸超限"></el-table-column>
                <el-table-column prop="outkcg" label="关舱盖"></el-table-column>
                <el-table-column prop="outcxx" label="装超限"></el-table-column>
                <el-table-column prop="zsc" label="总时"></el-table-column>
                <el-table-column prop="eff" label="计划效率"></el-table-column>
            </el-table>
            <div class="pagination">
                <el-pagination
                    background
                    layout="total, prev, pager, next"
                    :current-page="query.pageIndex"
                    :page-size="query.pageSize"
                    :total="pageTotal"
                    @current-change="handlePageChange"
                ></el-pagination>
            </div>
        </div>
    </div>
</template>

<script>
import Axios from 'axios';
const axios = require('axios');
import { fetchData } from '../../api/index';
export default {
    name: 'basetable',
    data() {
        return {
            query: {
                address: '',
                name: '',
                pageIndex: 1,
                pageSize: 10
            },
            tableData: [],
            multipleSelection: [],
            delList: [],
            editVisible: false,
            insertVisible: false,
            pageTotal: 0,
            edit_form: {},
            insert_form: {},
            idx: -1,
            id: -1,
            selectedId: '',
            shipdata: [],
            cargo_type: ''
        };
    },
    created() {
        // this.getData();
        Axios.get(this.url.url + '/get_shipname').then((res) => {
            // console.log(res);
            this.shipdata = res.data.list;
        });
    },
    methods: {
        downloadFile() {
            return new Promise((resolve, reject) => {
                let param = new URLSearchParams();
                param.append('ship_id', this.selectedId);
                // console.log(`${url} 请求数据，参数=>`, JSON.stringify(options))
                // axios.defaults.headers['content-type'] = 'application/json;charset=UTF-8'
                axios({
                    method: 'post',
                    url: this.url.url + '/export_plan_data', // 请求地址
                    data: param, // 参数
                    responseType: 'blob' // 表明返回服务器返回的数据类型
                }).then(
                    (response) => {
                        // console.log("下载响应",response)
                        resolve(response.data);
                        let blob = new Blob([response.data], {
                            type: 'application/octet-stream'
                        });
                        // console.log(blob)
                        let fileName = this.shipdata[this.selectedId - 1].ship_name + '作业信息编制.xls';
                        // 切割出文件名
                        // let fileNameEncode = response.headers['content-disposition'].split('filename=')[1];
                        // // 解码
                        // let fileName = decodeURIComponent(fileNameEncode);
                        // console.log("fileName",fileName)
                        // if (window.navigator.msSaveOrOpenBlob) {
                        //     // console.log(2)
                        //     navigator.msSaveBlob(blob, fileName);
                        // } else {
                        // console.log(3)
                        var link = document.createElement('a');
                        link.href = window.URL.createObjectURL(blob);
                        link.download = fileName;
                        link.click();
                        //释放内存
                        window.URL.revokeObjectURL(link.href);
                        // }
                    },
                    (err) => {
                        reject(err);
                    }
                );
            });
        },
        selectchange() {
            let param = new URLSearchParams();
            param.append('id', this.selectedId);
            Axios({
                method: 'post',
                url: this.url.url + '/post_plan_data',
                data: param
            }).then((res) => {
                console.log(res);
                this.tableData = res.data.res;
            });
        },

        // 删除操作
        handleDelete(index, row) {
            // 二次确认删除
            this.$confirm('确定要删除吗？', '提示', {
                type: 'warning'
            })
                .then(() => {
                    let del_id = this.tableData[index].id;
                    let param = new URLSearchParams();
                    param.append('del_id', del_id);
                    param.append('id', this.selectedId);
                    Axios({
                        method: 'post',
                        url: this.url.url + '/del_incargo_data',
                        data: param
                    });
                    this.$message.success('删除成功');
                    this.tableData.splice(index, 1);
                })
                .catch(() => {});
        },
        // 多选操作
        handleSelectionChange(val) {
            this.multipleSelection = val;
        },
        delAllSelection() {
            const length = this.multipleSelection.length;
            let str = '';
            this.delList = this.delList.concat(this.multipleSelection);
            for (let i = 0; i < length; i++) {
                str += this.multipleSelection[i].name + ' ';
            }
            this.$message.error(`删除了${str}`);
            this.multipleSelection = [];
        },
        // 编辑操作
        handleEdit(index, row) {
            this.idx = index;
            this.edit_form = row;
            this.editVisible = true;
        },
        // 保存编辑
        saveEdit() {
            this.editVisible = false;
            this.$message.success(`修改第 ${this.idx + 1} 行成功`);
            this.$set(this.tableData, this.idx, this.edit_form);
        },
        handleInsert(index, row) {
            // this.idx = index;
            // this.edit_form = row;
            this.insertVisible = true;
        },
        saveInsert() {
            this.insertVisible = false;
            let param = new URLSearchParams();
            param.append('name', this.insert_form.name);
            param.append('type', this.cargo_type);
            param.append('col', this.insert_form.col);
            param.append('layer', this.insert_form.layer);
            param.append('ship_id', this.selectedId);
            Axios({
                method: 'post',
                url: this.url.url + '/insert_incargo_data',
                data: param
            });
            this.$message.success('新增成功');
            location.reload();
            // this.$set(this.tableData, this.idx, this.edit_form);
        },
        // 分页导航
        handlePageChange(val) {
            this.$set(this.query, 'pageIndex', val);
            this.getData();
        }
    }
};
</script>

<style scoped>
.handle-box {
    margin-bottom: 20px;
}

.handle-select {
    width: 120px;
}

.handle-input {
    width: 300px;
    display: inline-block;
}
.table {
    width: 100%;
    font-size: 14px;
}
.red {
    color: #ff0000;
}
.mr10 {
    margin-right: 10px;
}
.table-td-thumb {
    display: block;
    margin: auto;
    width: 40px;
    height: 40px;
}
</style>
