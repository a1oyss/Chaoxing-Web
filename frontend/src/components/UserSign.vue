<template>
  <div>
    <el-tabs v-model="activeName" type="card">
      <el-tab-pane label="普通\手势\位置签到" name="first">
          <general></general>
      </el-tab-pane>
      <el-tab-pane label="拍照签到" name="third">拍照签到</el-tab-pane>
      <el-tab-pane label="二维码签到" name="fourth">
        <QRSign></QRSign>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>
<script>
import General from './type/General.vue';
import QRSign from './type/QRSign.vue'
export default {
    name:'UserSign',
    data() {
      return {
        activeName: 'first'
      };
    },
    components:{
        General,
        QRSign
    }
  };
</script>
<style scoped>
</style>
