<template>
  <el-container>
    <el-aside>
      <el-form label-width="80px">
        <el-form-item label="签到位置">
          <el-input v-model="positionForm.name" disabled></el-input>
        </el-form-item>
        <el-form-item label="经度">
          <el-input v-model="positionForm.longitude"></el-input>
        </el-form-item>
        <el-form-item label="纬度">
          <el-input v-model="positionForm.latitude"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="generalSign">签到</el-button>
        </el-form-item>
      </el-form>
    </el-aside>
    <result-table :resultData="data"></result-table>
  </el-container>
</template>
<script>
import ResultTable from './ResultTable.vue';
export default {
  components: { ResultTable },
  name: "General",
  data() {
    return {
      positionForm: {
        name:'',
        longitude:'',
        latitude:''
      },
      data:[]
    };
  },
  methods:{
      generalSign(){
        this.axios.get('/sign')
        .then((response)=>{
          console.log(response)
          this.$store.commit('show')
          this.data=response.data
        })
      },
      savePos(){

      }
  },
  mounted(){
    this.axios.get('/pos')
    .then((response)=>{
      this.positionForm=response.data
    })
  }
};
</script>
<style scoped>
.el-container{
    margin-left: 30px;
}
</style>