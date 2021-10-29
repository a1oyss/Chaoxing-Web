<template>
  <div>
    <el-table :data="tableData" style="width: 100%">
      <el-table-column prop="name" label="姓名" width="120"> </el-table-column>
      <el-table-column
        prop="username"
        label="用户名"
        width="180"
      ></el-table-column>
      <el-table-column prop="password" label="密码"></el-table-column>
      <el-table-column label="操作" width="140">
        <template slot-scope="scope">
          <el-button @click="handleClick(scope.row)" type="text">编辑</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-dialog title="修改信息" :visible.sync="dialogFormVisible">
      <el-form :model="form">
        <el-form-item label="姓名">
          <el-input v-model="form.name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="用户名">
          <el-input v-model="form.username" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="密码">
          <el-input v-model="form.password" autocomplete="off" show-password></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="onEdit">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>
<script>
export default {
  data() {
    return {
      dialogFormVisible: false,
      tableData: [],
      form: {
        name: "",
        username: "",
        password: ""
      },
    };
  },
  methods:{
    handleClick(row){
      this.form=row
      this.dialogFormVisible=true
    },
    onEdit(){

    }
  },
  mounted(){
      this.axios.get('/config')
      .then((response)=>{
        response.data.forEach((e)=>{
          this.tableData.push(e)
        })
      })
  }
};
</script>
<style scoped>
</style>