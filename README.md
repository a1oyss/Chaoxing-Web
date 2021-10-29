# Chaoxing-Web
超星学习通签到vue版

项目参考[chaoxing_auto_sign](https://github.com/mkdir700/chaoxing_auto_sign)，在local版本的基础上加了一个前端页面，挂在服务器上之后就可以远程签到。

## 功能介绍
1. 普通签到
2. 手势签到
3. 位置签到
4. 二维码签到
5. ~~拍照签到~~

二维码签到直接在前端页面上传二维码图片解码，获取enc参数签到。

## 环境部署
### 前端
修改frontend/plugins/axios.js中的baseURL，改为自己服务器地址。
```
let config = {
  baseURL:'http://127.0.0.1:8000/'
};

```
打包
```
cd frontend
npm run build
cp dist/* ../backend/public/
```
### 后端
使用docker搭建
```
cd backend
docker-compose up -d
```


