<template>
<el-tabs type="border-card">
  <el-tab-pane label="用户管理">
    <user-form></user-form>
  </el-tab-pane>
  <el-tab-pane label="签到">
    <user-sign></user-sign>
  </el-tab-pane>
</el-tabs>
</template>
<script>
import UserForm from './UserForm'
import UserSign from './UserSign.vue';
export default {
  name: "Index",
  data() {
    return {
      
    }
  },
  components:{
    UserForm,
    UserSign
  }
};
</script>
<style scoped>
</style>