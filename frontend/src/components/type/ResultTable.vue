<template>
  <el-dialog title="签到结果" :visible="this.$store.state.resultShow" @close='closeDialog'>
    <el-table :data="resultData">
      <el-table-column
        property="name"
        label="姓名"
        width="150"
      ></el-table-column>
      <el-table-column
        property="classname"
        label="课程名称"
        width="200"
      ></el-table-column>
      <el-table-column property="date" label="日期"></el-table-column>
      <el-table-column property="status" label="状态"></el-table-column>
    </el-table>
  </el-dialog>
</template>
<script>
export default {
  name: "ResultTable",
  props:['resultData'],
  data() {
    return {
    };
  },
  methods:{
      closeDialog(){
        this.$store.commit('hide')
      }
  }
};
</script>
<style scoped>
</style>