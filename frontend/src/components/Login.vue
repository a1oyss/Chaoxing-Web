<template>
    <el-form
      :model="loginForm"
      status-icon
      :rules="loginRules"
      ref="loginForm"
      class="loginForm"
    >
    <h1>超星学习通签到</h1>
      <el-form-item prop="username">
        <el-input
          type="text"
          v-model="loginForm.username"
          autocomplete="off"
          placeholder="账号"
        ></el-input>
      </el-form-item>
      <el-form-item prop="password">
        <el-input
          type="password"
          v-model="loginForm.password"
          autocomplete="off"
          placeholder="密码"
        ></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm('loginForm')"
          >提交</el-button
        >
        <el-button @click="resetForm('loginForm')">重置</el-button>
      </el-form-item>
    </el-form>
</template>
<script>
export default {
  el: "#app",
  data() {
    return {
      loginForm: {
        username: "",
        password: "",
      },
      rules: {
        username: [{ required: true, message: "请输入用户名", trigger: blur }],
        password: [{ required: true, message: "请输入密码", trigger: blur }],
      },
    };
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          // this.VueAxios.post("api/login")
          //   .then((response) => {
          //     if (this.loginForm.username==='admin'&&this.loginForm.password==='admin') {
          //       this.$store.commit('login',this.loginForm)
          //       //跳转index页面
          //     }
          //   })
          //   .catch((response) => {
          //     console.log("error:" + response);
          //   });
          this.$store.commit('login',this.loginForm)
          let path = this.$route.query.redirect
          this.$router.replace({path: path === '/' || path === undefined ? '/index' : path})
        }
      });
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    },
  },
};
</script>
<style scoped>
.loginForm{
  width: 300px;
  margin: 0 auto;
  border: 1px solid #eeeeee;
  padding: 30px;
  border-radius: 4px;
}
</style>