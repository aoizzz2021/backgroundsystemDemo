<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item> <i class="el-icon-lx-cascades"></i> 出口货物堆存信息 </el-breadcrumb-item>
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
                <el-button type="primary" icon="el-icon-delete" class="handle-del mr10" @click="delAllSelection">批量删除</el-button>
                <!-- <el-input v-model="query.name" placeholder="贝位" class="handle-input mr10"></el-input>
                <el-button type="primary" icon="el-icon-search" @click="handleSearch">搜索</el-button> -->
                <el-button type="primary" icon="el-icon-plus" @click="handleInsert">新增</el-button>
            </div>
            <el-table
                :data="tableData"
                border
                class="table"
                ref="multipleTable"
                header-cell-class-name="table-header"
                @selection-change="handleSelectionChange"
            >
                <el-table-column type="selection" width="55" align="center"></el-table-column>
                <el-table-column prop="id" label="ID" width="55" align="center"></el-table-column>
                <el-table-column prop="bw" label="贝位名称"></el-table-column>
                <el-table-column prop="all_count" label="货物数量"></el-table-column>
                <el-table-column prop="cold_count" label="冷藏箱数量"></el-table-column>
                <el-table-column prop="danger_count" label="危险箱数量"></el-table-column>
                <el-table-column prop="over_count" label="超限箱数量"></el-table-column>
                <el-table-column prop="normal_count" label="普通箱数量"></el-table-column>
                <el-table-column label="操作" width="180" align="center">
                    <template slot-scope="scope">
                        <!-- <el-button
                            type="text"
                            icon="el-icon-edit"
                            @click="handleEdit(scope.$index, scope.row)"
                        >编辑</el-button> -->
                        <el-button type="text" icon="el-icon-delete" class="red" @click="handleDelete(scope.$index, scope.row)"
                            >删除</el-button
                        >
                    </template>
                </el-table-column>
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

        <!-- 编辑弹出框 -->
        <el-dialog title="编辑" :visible.sync="editVisible" width="30%">
            <el-form ref="edit_form" :model="edit_form" label-width="70px">
                <el-form-item label="贝位名称">
                    <el-input v-model="edit_form.bw"></el-input>
                </el-form-item>
                <el-form-item label="货物数量">
                    <el-input v-model="edit_form.all_count"></el-input>
                </el-form-item>
                <el-form-item label="冷藏箱数量">
                    <el-input v-model="edit_form.cold_count"></el-input>
                </el-form-item>
                <el-form-item label="危险箱数量">
                    <el-input v-model="edit_form.danger_count"></el-input>
                </el-form-item>
                <el-form-item label="超限箱数量">
                    <el-input v-model="edit_form.over_count"></el-input>
                </el-form-item>
                <el-form-item label="普通箱数量">
                    <el-input v-model="edit_form.normal_count"></el-input>
                </el-form-item>
            </el-form>
            <span slot="footer" class="dialog-footer">
                <el-button type="primary" @click="saveEdit">确 定</el-button>
                <el-button @click="editVisible = false">取 消</el-button>
            </span>
        </el-dialog>

        <!-- 新增弹出框 -->
        <el-dialog title="新增" :visible.sync="insertVisible" width="30%">
            <el-form ref="insert_form" :model="insert_form" label-width="70px">
                <el-form-item label="贝位名称">
                    <el-input v-model="insert_form.bw"></el-input>
                </el-form-item>
                <el-form-item label="货物数量">
                    <el-input v-model="insert_form.all_count"></el-input>
                </el-form-item>
                <el-form-item label="冷藏箱数量">
                    <el-input v-model="insert_form.cold_count"></el-input>
                </el-form-item>
                <el-form-item label="危险箱数量">
                    <el-input v-model="insert_form.danger_count"></el-input>
                </el-form-item>
                <el-form-item label="超限箱数量">
                    <el-input v-model="insert_form.over_count"></el-input>
                </el-form-item>
                <el-form-item label="普通箱数量">
                    <el-input v-model="insert_form.normal_count"></el-input>
                </el-form-item>
            </el-form>
            <span slot="footer" class="dialog-footer">
                <el-button type="primary" @click="saveInsert">确 定</el-button>
                <el-button @click="editVisible = false">取 消</el-button>
            </span>
        </el-dialog>
    </div>
</template>

<script>
import Axios from 'axios';
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
            shipdata: []
        };
    },
    created() {
        Axios.get(this.url.url + '/get_shipname').then((res) => {
            console.log(res);
            this.shipdata = res.data.list;
        });
    },
    methods: {
        selectchange() {
            let param = new URLSearchParams();
            param.append('id', this.selectedId);
            Axios({
                method: 'post',
                url: this.url.url + '/post_outbei_data',
                data: param
            }).then((res) => {
                console.log(res);
                this.tableData = res.data.list;
            });
        },

        // 触发搜索按钮
        handleSearch() {
            this.$set(this.query, 'pageIndex', 1);
            this.getData();
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
                    Axios({
                        method: 'post',
                        url: this.url.url + '/del_outbei_data',
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
            console.log(this.insert_form);
            param.append('name', this.insert_form.bw);
            param.append('all_count', this.insert_form.all_count);
            param.append('cold_count', this.insert_form.cold_count);
            param.append('danger_count', this.insert_form.danger_count);
            param.append('over_count', this.insert_form.over_count);
            param.append('normal_count', this.insert_form.normal_count);
            param.append('ship_id', this.selectedId);
            Axios({
                method: 'post',
                url: this.url.url + '/insert_outbei_data',
                data: param
            });
            this.$message.success(`新增成功`);
            // location.reload();
            
            console.log(this.insert_form);
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
