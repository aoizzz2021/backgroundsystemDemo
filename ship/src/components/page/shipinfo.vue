<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item>
                    <i class="el-icon-lx-cascades"></i> 船舶信息管理
                </el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="container">
            <div class="handle-box">
                <!-- <el-button
                    type="primary"
                    icon="el-icon-delete"
                    class="handle-del mr10"
                    @click="delAllSelection"
                >批量删除</el-button> -->
                <!-- <el-input v-model="query.name" placeholder="船舶名" class="handle-input mr10"></el-input>
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
                <el-table-column prop="ship_name" label="船舶名"></el-table-column>
                <el-table-column prop="ship_len" label="船长"></el-table-column>
                <el-table-column prop="ship_width" label="船宽"></el-table-column>
                <el-table-column prop="ship_maxcase" label="最大箱量"></el-table-column>
                <el-table-column prop="ship_dwt" label="载重吨"></el-table-column>
                <el-table-column label="型深">
                    <template slot-scope="scope">{{scope.row.ship_depth}} m </template>
                </el-table-column>
                <el-table-column label="舱位宽度">
                    <template slot-scope="scope">{{scope.row.ship_sw}} m </template>
                </el-table-column>
                <el-table-column label="普箱高度">
                    <template slot-scope="scope">{{scope.row.ship_cbh}} m </template>
                </el-table-column>
                <el-table-column label="高箱高度">
                    <template slot-scope="scope">{{scope.row.ship_hbh}} m </template>
                </el-table-column>
                <el-table-column label="转锁高度">
                    <template slot-scope="scope">{{scope.row.ship_rlh}} m </template>
                </el-table-column>
                <el-table-column label="设计起升">
                    <template slot-scope="scope">{{scope.row.ship_dl}} m </template>
                </el-table-column>
                <el-table-column label="半速起升">
                    <template slot-scope="scope">{{scope.row.ship_hl}} m </template>
                </el-table-column>
                <el-table-column label="全速起升">
                    <template slot-scope="scope">{{scope.row.ship_al}} m </template>
                </el-table-column>
                <el-table-column label="码头标高">
                    <template slot-scope="scope">{{scope.row.ship_we}} m </template>
                </el-table-column>
                <el-table-column prop="ship_idh" label="进港吃水-艏"></el-table-column>
                <el-table-column prop="ship_idr" label="进港吃水-艉"></el-table-column>
                <el-table-column prop="ship_idm" label="进港吃水-均"></el-table-column>
                <el-table-column prop="ship_th" label="潮高"></el-table-column>
                <el-table-column prop="ship_afhc" label="进港层高-普"></el-table-column>
                <el-table-column prop="ship_afhh" label="进港层高-高"></el-table-column>
                <el-table-column prop="ship_wh" label="作业高度"></el-table-column>
                <el-table-column prop="ship_ihmin" label="建议抹高-最少"></el-table-column>
                <el-table-column prop="ship_ihmax" label="建议抹高-均衡"></el-table-column>
                <el-table-column label="操作" width="180" align="center">
                    <template slot-scope="scope">
                        <!-- <el-button
                            type="text"
                            icon="el-icon-edit"
                            @click="handleEdit(scope.$index, scope.row)"
                        >编辑</el-button> -->
                        <el-button
                            type="text"
                            icon="el-icon-delete"
                            class="red"
                            @click="handleDelete(scope.$index, scope.row)"
                        >删除</el-button>
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
                <el-form-item label="船舶名">
                    <el-input v-model="edit_form.ship_name"></el-input>
                </el-form-item>
                <el-form-item label="船长">
                    <el-input v-model="edit_form.ship_len"></el-input>
                </el-form-item>
                <el-form-item label="船宽">
                    <el-input v-model="edit_form.ship_width"></el-input>
                </el-form-item>
                <el-form-item label="最大箱量">
                    <el-input v-model="edit_form.ship_maxcase"></el-input>
                </el-form-item>
                <el-form-item label="载重吨">
                    <el-input v-model="edit_form.ship_dwt"></el-input>
                </el-form-item>
                <el-form-item label="型深">
                    <el-input v-model="edit_form.ship_depth"></el-input>
                </el-form-item>
                <el-form-item label="舱位宽度">
                    <el-input v-model="edit_form.ship_sw"></el-input>
                </el-form-item>
                <el-form-item label="普箱高度">
                    <el-input v-model="edit_form.ship_cbh"></el-input>
                </el-form-item>
                <el-form-item label="高箱高度">
                    <el-input v-model="edit_form.ship_hbh"></el-input>
                </el-form-item>
                <el-form-item label="转锁高度">
                    <el-input v-model="edit_form.ship_rlh"></el-input>
                </el-form-item>
                <el-form-item label="设计起升">
                    <el-input v-model="edit_form.ship_dl"></el-input>
                </el-form-item>
                <el-form-item label="半速起升">
                    <el-input v-model="edit_form.ship_hl"></el-input>
                </el-form-item>
                <el-form-item label="全速起升">
                    <el-input v-model="edit_form.ship_al"></el-input>
                </el-form-item>
                <el-form-item label="码头标高">
                    <el-input v-model="edit_form.ship_we"></el-input>
                </el-form-item>
                <el-form-item label="进港吃水-艏">
                    <el-input v-model="edit_form.ship_idh"></el-input>
                </el-form-item>
                <el-form-item label="进港吃水-艉">
                    <el-input v-model="edit_form.ship_idr"></el-input>
                </el-form-item>
                <el-form-item label="进港吃水-均">
                    <el-input v-model="edit_form.ship_idm"></el-input>
                </el-form-item>
                <el-form-item label="潮高">
                    <el-input v-model="edit_form.ship_th"></el-input>
                </el-form-item>
                <el-form-item label="进港层高-普">
                    <el-input v-model="edit_form.ship_afhc"></el-input>
                </el-form-item>
                <el-form-item label="进港层高-高">
                    <el-input v-model="edit_form.ship_afhh"></el-input>
                </el-form-item>
                <el-form-item label="作业高度">
                    <el-input v-model="edit_form.ship_wh"></el-input>
                </el-form-item>
                <el-form-item label="建议抹高-最少">
                    <el-input v-model="edit_form.ship_ihmin"></el-input>
                </el-form-item>
                <el-form-item label="建议抹高-均衡">
                    <el-input v-model="edit_form.ship_ihmax"></el-input>
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
                <el-form-item label="船舶名">
                    <el-input v-model="insert_form.ship_name"></el-input>
                </el-form-item>
                <el-form-item label="船长">
                    <el-input v-model="insert_form.ship_len"></el-input>
                </el-form-item>
                <el-form-item label="船宽">
                    <el-input v-model="insert_form.ship_width"></el-input>
                </el-form-item>
                <el-form-item label="最大箱量">
                    <el-input v-model="insert_form.ship_maxcase"></el-input>
                </el-form-item>
                <el-form-item label="载重吨">
                    <el-input v-model="insert_form.ship_dwt"></el-input>
                </el-form-item>
                <el-form-item label="型深">
                    <el-input v-model="insert_form.ship_depth"></el-input>
                </el-form-item>
                <el-form-item label="舱位宽度">
                    <el-input v-model="insert_form.ship_sw"></el-input>
                </el-form-item>
                <el-form-item label="普箱高度">
                    <el-input v-model="insert_form.ship_cbh"></el-input>
                </el-form-item>
                <el-form-item label="高箱高度">
                    <el-input v-model="insert_form.ship_hbh"></el-input>
                </el-form-item>
                <el-form-item label="转锁高度">
                    <el-input v-model="insert_form.ship_rlh"></el-input>
                </el-form-item>
                <el-form-item label="设计起升">
                    <el-input v-model="insert_form.ship_dl"></el-input>
                </el-form-item>
                <el-form-item label="半速起升">
                    <el-input v-model="insert_form.ship_hl"></el-input>
                </el-form-item>
                <el-form-item label="全速起升">
                    <el-input v-model="insert_form.ship_al"></el-input>
                </el-form-item>
                <el-form-item label="码头标高">
                    <el-input v-model="insert_form.ship_we"></el-input>
                </el-form-item>
                <el-form-item label="进港吃水-艏">
                    <el-input v-model="insert_form.ship_idh"></el-input>
                </el-form-item>
                <el-form-item label="进港吃水-艉">
                    <el-input v-model="insert_form.ship_idr"></el-input>
                </el-form-item>
                <el-form-item label="进港吃水-均">
                    <el-input v-model="insert_form.ship_idm"></el-input>
                </el-form-item>
                <el-form-item label="潮高">
                    <el-input v-model="insert_form.ship_th"></el-input>
                </el-form-item>
                <el-form-item label="进港层高-普">
                    <el-input v-model="insert_form.ship_afhc"></el-input>
                </el-form-item>
                <el-form-item label="进港层高-高">
                    <el-input v-model="insert_form.ship_afhh"></el-input>
                </el-form-item>
                <el-form-item label="作业高度">
                    <el-input v-model="insert_form.ship_wh"></el-input>
                </el-form-item>
                <el-form-item label="建议抹高-最少">
                    <el-input v-model="insert_form.ship_ihmin"></el-input>
                </el-form-item>
                <el-form-item label="建议抹高-均衡">
                    <el-input v-model="insert_form.ship_ihmax"></el-input>
                </el-form-item>
            </el-form>
            <span slot="footer" class="dialog-footer">
                <el-button type="primary" @click="saveEdit">确 定</el-button>
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
            id: -1
        };
    },
    created() {
        this.getData();
    },
    methods: {
        // 获取 easy-mock 的模拟数据
        getData() {
            // fetchData(this.query).then(res => {
            //     console.log(res);
            //     this.tableData = res.list;
            //     this.pageTotal = res.pageTotal || 50;
            // });
            // 本机ip
            Axios.get(this.url.url+'/get_ship_data').then(res=>{
                console.log(res)
                this.tableData = res.data.list;
                this.pageTotal = res.data.pageTotal || 50;
            })
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
                    let del_id = this.tableData[index].id
                    let param = new URLSearchParams()
                    param.append('del_id', del_id)
                    Axios({
                        method: 'post',
                        url: this.url.url+'/del_ship_data',
                        data: param
                    })
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
            let param = new URLSearchParams()
            param.append('ship_name', this.insert_form.ship_name)
            param.append('ship_len', this.insert_form.ship_len)
            param.append('ship_width', this.insert_form.ship_width)
            param.append('ship_maxcase', this.insert_form.ship_maxcase)
            param.append('ship_dwt', this.insert_form.ship_dwt)
            param.append('ship_depth', this.insert_form.ship_depth)
            param.append('ship_sw', this.insert_form.ship_sw)
            param.append('ship_cbh', this.insert_form.ship_cbh)
            param.append('ship_hbh', this.insert_form.ship_hbh)
            param.append('ship_rlh', this.insert_form.ship_rlh)
            param.append('ship_dl', this.insert_form.ship_dl)
            param.append('ship_hl', this.insert_form.ship_hl)
            param.append('ship_al', this.insert_form.ship_al)
            param.append('ship_we', this.insert_form.ship_we)
            param.append('ship_idh', this.insert_form.ship_idh)
            param.append('ship_idr', this.insert_form.ship_idr)
            param.append('ship_idm', this.insert_form.ship_idm)
            param.append('ship_th', this.insert_form.ship_th)
            param.append('ship_afhc', this.insert_form.ship_afhc)
            param.append('ship_afhh', this.insert_form.ship_afhh)
            param.append('ship_wh', this.insert_form.ship_wh)
            param.append('ship_ihmin', this.insert_form.ship_ihmin)
            param.append('ship_ihmax', this.insert_form.ship_ihmax)
            Axios({
                method: 'post',
                url: this.url.url+'/insert_bei_data',
                data: param
            })
            location.reload()
            this.$message.success(`用户新增成功`);
            console.log(this.insert_form)
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
