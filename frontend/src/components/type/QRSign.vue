<template>
  <div class="qr-pannel">
    <el-input placeholder="请输入内容" v-model="result" :disabled="true">
    </el-input>
    <qrcode-capture @decode="onDecode" style="display: block"/>
    <el-button type="primary" @click="onSign">二维码签到</el-button>
    <result-table :resultData="data"></result-table>
  </div>
</template>
<script>
import {QrcodeCapture} from "vue-qrcode-reader";
import ResultTable from "./ResultTable.vue";
export default {
  components: { QrcodeCapture, ResultTable },
  data() {
    return {
      result: "",
      data:[]
    };
  },
  methods: {
    onDecode(result) {
      this.result = result;
    },
    onSign() {
      let enc = this.result.split("&")[3];
      this.axios.get("/qr_sign?" + enc).then((response) => {
        console.log(response);
        this.$store.commit("show");
        console.log(response.data);
        this.data = response.data;
      });
    },
  },
};
</script>
<style scoped>
.qr-pannel {
  width: 500px;
  margin: 0 auto;
  line-height: 50px;
}
</style>