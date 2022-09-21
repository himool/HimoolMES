# Himool MES制造执行系统

### 公司介绍
盒木科技([官网地址](https://www.himool.com/home))专注于仓储物流和生产制造行业数字化系统的研发和实施。Himool是盒木科技自主研发的软件产品系列品牌,目前已发布Himool WMS仓库管理系统，Himool WCS仓库控制系统,Himool MES制造执行系统，Himool ERP进销存管理系统及Himool AMS资产管理系统。欢迎合作伙伴，代理商或者客户微信扫描下方客户经理二维码或电话18761717855体验咨询。<br /><br />
![微信](https://gitee.com/himool/erp/raw/master/img/%E5%BE%AE%E4%BF%A1.png)

#### 项目介绍
开源制造执行系统MES，采用前后端分离技术，api使用restful协议，方便二次开发，后端使用Python，Django，DRF等技术，前端代码使用AntD进行构建，包含看板管理、生产管理、设备管理、质量管理等模块。功能模块持续更新中。。。
* Gitee地址: [Gitee](https://gitee.com/himool/mes)
* Demo地址: [Demo](http://114.218.158.78:15000/) &nbsp;&nbsp;公司编号: admin  测试帐号：admin  密码：admin

### 使用前须知
* 软件开放源码(发行协议:GPL-3.0)，个人用户可免费学习使用，但禁止任何单位或个人修改软件后再次发行的行为。商业使用需得到我司授权，否则我们将通过法律途径解决侵权问题。
* 我们欢迎对开源技术感兴趣的朋友一起加入到我们项目中来完善系统功能并为客户提供服务。欢迎扫描下方二维码添加技术交流群，添加时请备注来意

   ![微信群](https://gitee.com/himool/erp/raw/master/img/%E5%BE%AE%E4%BF%A1%E7%BE%A4.png)

### 硬件要求及开发环境
* Python版本为V3.9+
* Django版本为V3.2+
* Django-rest-framework版本为V3.12+
* Vue版本为2.6+
* 数据库为MySQL
* 前端组件为AntD
* 其他Python包可参考requirements.txt文件

### 搭建运行环境
* pip install -r requirements.txt
* cd frontend  #进入frontend文件夹
* npm install -g @vue/cli  #安装vue脚手架
* npm install  #安装依赖包

### 本地运行
1. 启动后端服务
    python manage.py runserver
2. 启动前端服务
    npm run serve
3. 浏览器访问前端地址
    
### PC界面截图
![看板管理](https://gitee.com/himool/mes/raw/master/img/%E7%9C%8B%E6%9D%BF%E7%AE%A1%E7%90%86.png)
![生产管理](https://gitee.com/himool/mes/raw/master/img/%E7%94%9F%E4%BA%A7%E7%AE%A1%E7%90%86.png)
![质量管理](https://gitee.com/himool/mes/raw/master/img/%E8%B4%A8%E9%87%8F%E7%AE%A1%E7%90%86.png)
![设备管理](https://gitee.com/himool/mes/raw/master/img/%E8%AE%BE%E5%A4%87%E7%AE%A1%E7%90%86.png)