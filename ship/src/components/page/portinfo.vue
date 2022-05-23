<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-lx-calendar"></i> 在港作业信息</el-breadcrumb-item>
                <el-breadcrumb-item>在港作业信息</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="container">
            <div class="content-title">上传船舶信息</div>
            <el-row :gutter="20" type="flex">
                <el-col :span="8">
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
                        <div style="margin-top: 10%">
                            <el-button type="primary" icon="el-icon-upload">保存</el-button>
                            <el-button type="primary" icon="el-icon-download" @click="downloadFile">导出</el-button>
                        </div>
                    </div>
                </el-col>
                <el-col :span="10">
                    <el-upload
                        class="upload-demo"
                        :action="in_web_url"
                        :data="ship_id"
                        :on-success="handleSuccess_in"
                        :on-preview="handlePreview"
                        :on-remove="handleRemove"
                        :before-remove="beforeRemove"
                        multiple
                        :limit="1"
                        :on-exceed="handleExceed"
                        :file-list="fileList"
                    >
                        <i class="el-icon-upload"></i>
                        <div class="el-upload__text"><em>点击上传进口数据</em></div>
                    </el-upload>
                </el-col>

                <el-col :span="10">
                    <el-upload
                        class="upload-demo"
                        :action="out_web_url"
                        :data="ship_id"
                        :on-success="handleSuccess_out"
                        :on-preview="handlePreview"
                        :on-remove="handleRemove"
                        :before-remove="beforeRemove"
                        multiple
                        :limit="1"
                        :on-exceed="handleExceed"
                        :file-list="fileList"
                    >
                        <i class="el-icon-upload"></i>
                        <div class="el-upload__text"><em>点击上传出口数据</em></div>
                    </el-upload>
                </el-col>
            </el-row>
        </div>
        <div class="container">
            <el-row :gutter="20" type="flex">
                <el-col :span="12">
                    <div class="content-title">进口</div>
                    <el-table
                        :data="intableData"
                        border
                        class="table"
                        ref="multipleTable"
                        header-cell-class-name="table-header"
                        @selection-change="handleSelectionChange"
                    >
                        <el-table-column type="selection" width="55" align="center"></el-table-column>
                        <el-table-column prop="id" label="ID" width="55" align="center"></el-table-column>
                        <el-table-column prop="bw" label="贝位"></el-table-column>
                        <el-table-column prop="col" label="列"></el-table-column>
                        <el-table-column prop="layer" label="层数"></el-table-column>
                        <el-table-column prop="over_count" label="超限箱"></el-table-column>
                        <el-table-column prop="normal_count" label="普通箱"></el-table-column>
                        <el-table-column prop="cold_count" label="冷藏箱"></el-table-column>
                        <el-table-column prop="danger_count" label="危险箱"></el-table-column>
                        <el-table-column prop="all_count" label="总箱数"></el-table-column>
                    </el-table>
                </el-col>

                <el-col :span="12">
                    <div class="content-title">出口</div>
                    <el-table
                        :data="outtableData"
                        border
                        class="table"
                        ref="multipleTable"
                        header-cell-class-name="table-header"
                        @selection-change="handleSelectionChange"
                    >
                        <el-table-column type="selection" width="55" align="center"></el-table-column>
                        <el-table-column prop="id" label="ID" width="55" align="center"></el-table-column>
                        <el-table-column prop="bw" label="贝位"></el-table-column>
                        <el-table-column prop="col" label="列"></el-table-column>
                        <el-table-column prop="layer" label="层数"></el-table-column>
                        <el-table-column prop="over_count" label="超限箱"></el-table-column>
                        <el-table-column prop="normal_count" label="普通箱"></el-table-column>
                        <el-table-column prop="cold_count" label="冷藏箱"></el-table-column>
                        <el-table-column prop="danger_count" label="危险箱"></el-table-column>
                        <el-table-column prop="all_count" label="总箱数"></el-table-column>
                    </el-table>
                </el-col>
            </el-row>
        </div>
    </div>
</template>

<script>
import Axios from 'axios';
const axios = require('axios');
export default {
    data() {
        return {
            fileList: [],
            intableData: [],
            outtableData: [],
            in_web_url: '',
            out_web_url: '',
            shipdata: [],
            selectedId: '',
            ship_id: {}
        };
    },
    created() {
        (this.in_web_url = this.url.url + '/get_in_file'), (this.out_web_url = this.url.url + '/get_out_file');
        Axios.get(this.url.url + '/get_shipname').then((res) => {
            console.log(res);
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
                    url: this.url.url + '/export_file_data', // 请求地址
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
                        let fileName = this.shipdata[this.selectedId - 1].ship_name + '在港作业信息.xls';
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
        handleExport() {
            Axios.get(this.url.url + '/export_file_data').then((res) => {
                console.log(res);
                // this.intableData = res.data.list;
            });
        },
        selectchange() {
            this.ship_id['id'] = this.selectedId;
            let param = new URLSearchParams();
            param.append('id', this.selectedId);
            Axios({
                method: 'post',
                url: this.url.url + '/post_ship_data',
                data: param
            }).then((res) => {
                console.log(res);
                this.intableData = res.data.in_res;
                this.outtableData = res.data.out_res;
            });
        },
        handleRemove(file, fileList) {
            console.log(file, fileList);
        },
        handleSuccess_in(file) {
            this.$message.warning('进口文件上传成功！');
            let param = new URLSearchParams();
            param.append('ship_name', this.selectedId);
            Axios.get(this.url.url + '/get_in_file_data').then((res) => {
                console.log(res.msg);
                this.intableData = res.data.list;
            });
        },
        handleSuccess_out(file) {
            this.$message.warning('出口文件上传成功！');
            Axios.get(this.url.url + '/get_out_file_data').then((res) => {
                console.log(res);
                this.outtableData = res.data.list;
            });
        },
        handlePreview(file) {
            console.log(file);
        },
        handleExceed(files, fileList) {
            this.$message.warning(
                `当前限制选择 1 个文件，本次选择了 ${files.length} 个文件，共选择了 ${files.length + fileList.length} 个文件`
            );
        },
        beforeRemove(file) {
            return this.$confirm(`确定移除 ${file.name}？`);
        }
    }
};
</script>

<style scoped>
.handle-box {
    margin-bottom: 20px;
}
.content-title {
    font-weight: 400;
    line-height: 50px;
    margin: 10px 0;
    font-size: 22px;
    color: #1f2f3d;
}
.content-btn {
    /* font-weight: 400; */
    line-height: 50px;
    margin: 10% 10%;
    font-size: 22px;
    color: #1f2f3d;
}
.pre-img {
    width: 100px;
    height: 100px;
    background: #f8f8f8;
    border: 1px solid #eee;
    border-radius: 5px;
}
.crop-demo {
    display: flex;
    align-items: flex-end;
}
.crop-demo-btn {
    position: relative;
    width: 100px;
    height: 40px;
    line-height: 40px;
    padding: 0 20px;
    margin-left: 30px;
    background-color: #409eff;
    color: #fff;
    font-size: 14px;
    border-radius: 4px;
    box-sizing: border-box;
}
.crop-input {
    position: absolute;
    width: 100px;
    height: 40px;
    left: 0;
    top: 0;
    opacity: 0;
    cursor: pointer;
}
</style>