没问题！既然已经修复了，那就不需要在文档里提那些糟心的报错了。



这是一个\*\*干净、专业\*\*的版本，专门针对你现在的项目状态（后端 5000，前端 8081/8082）。你可以直接复制下面的内容到 `README.md` 中。



---



```markdown

\# ✈️ Python Flask + Vue 旅游网站系统



这是一个基于 Python Flask 后端和 Vue.js 前端的前后端分离旅游管理系统。包含管理员后台管理系统和前台用户界面。



\## 🛠️ 技术栈 (Tech Stack)



\### 后端 (Backend)

\- \*\*Language\*\*: Python 3.8+

\- \*\*Framework\*\*: Flask

\- \*\*ORM\*\*: SQLAlchemy

\- \*\*Database\*\*: MySQL (推荐) / SQL Server

\- \*\*Auth\*\*: JWT (JSON Web Token)



\### 前端 (Frontend)

\- \*\*Framework\*\*: Vue.js 2.x

\- \*\*UI Component\*\*: Element UI

\- \*\*Build Tool\*\*: Webpack / Vue CLI

\- \*\*Style\*\*: Sass/SCSS



---



\## 📂 目录结构 (Directory Structure)



```text

python1s2c1/

├── api/

│   ├── templates/front/admin/   # 管理后台前端源码 (Vue + ElementUI)

│   ├── templates/front/front/   # 用户前台前端源码 (Vue)

│   ├── models/                  # 数据库模型

│   └── ...

├── config.ini                   # 数据库连接配置文件

├── configs.py                   # 项目全局配置

├── run.py                       # 后端启动入口

├── requirements.txt             # Python 依赖列表

└── ...



```



---



\## 🚀 快速开始 (Quick Start)



\### 1. 数据库准备 (Database)



1\. 确保本地已安装 MySQL (5.7 或 8.0)。

2\. 创建数据库（例如 `travel\_db`）。

3\. 将 `db/` 目录下的 SQL 文件导入数据库。

4\. 修改根目录下的 `config.ini` 文件，配置你的数据库账号密码：

```ini

\[sql]

type = mysql

host = 127.0.0.1

port = 3306

user = root

passwd = 你的密码

db = 你的数据库名



```







\### 2. 后端启动 (Backend)



在项目根目录下打开终端：



```bash

\# 1. 安装依赖

pip install -r requirements.txt



\# 2. 启动服务 (默认运行在 5000 端口)

python run.py run



```



\### 3. 管理后台启动 (Admin Frontend)



打开新的终端窗口：



```bash

\# 1. 进入后台目录

cd api/templates/front/admin



\# 2. 安装依赖 (推荐使用淘宝镜像)

npm config set registry \[https://registry.npmmirror.com](https://registry.npmmirror.com)

npm install



\# 3. 启动后台 (运行在 8081 端口)

npm run serve



```



\### 4. 用户前台启动 (User Frontend)



打开新的终端窗口：



```bash

\# 1. 进入前台目录

cd api/templates/front/front



\# 2. 安装依赖

npm install



\# 3. 启动前台

npm run serve



```



---



\## 📝 功能模块 (Features)



\* \*\*用户模块\*\*: 注册、登录、个人中心、我的收藏

\* \*\*景点管理\*\*: 景点列表、景点详情、门票预订

\* \*\*资讯模块\*\*: 旅游资讯发布与浏览

\* \*\*交互模块\*\*: 评论留言、评分反馈

\* \*\*系统管理\*\*: 用户权限管理、轮播图配置



---



\## 🔑 默认账号 (Default Account)



\* \*\*管理员账号\*\*: `admin`

\* \*\*密码\*\*: `123456`



---



\## ⚠️ 开发环境注意 (Notes)



如果遇到 `node-sass` 或 `sass-loader` 版本报错，请执行以下命令修复依赖：



```bash

npm uninstall node-sass

npm install -D sass sass-loader@10




```



```

<img width="1269" height="646" alt="827801d29ea9ef2701cd5abefe9af766" src="https://github.com/user-attachments/assets/11d8113a-25cc-4b55-88b4-2b37aa91c77e" />
<img width="1272" height="641" alt="635e37dab93f6186b320d4a83de686db" src="https://github.com/user-attachments/assets/1f195945-5415-4673-a3d6-7825e1049804" />
<img width="1278" height="569" alt="739b8a333521e0056eaea3410743f147" src="https://github.com/user-attachments/assets/8c590baa-01e5-4f11-bcf3-51fb6c689627" />
<img width="1280" height="656" alt="129a7f58c84a8c1256bdca4e60b8de41" src="https://github.com/user-attachments/assets/51492dd5-5b8a-495b-b701-45dd20be58a0" />

```

