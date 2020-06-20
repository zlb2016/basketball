# 篮球数据分析系统
## NBA球员数据分析
- 在backend文件夹下更新laravel依赖包：composer install
- 在frontend文件夹中更新node依赖：npm install
- 在frontend文件夹中执行npm run dev
- 配置laravel 环境：.env
- 在backend文件夹生成key： php artisan key:generate
- 在backend文件夹配置laravel-admin: 
- - php artisan vendor:publish --provider="Encore\Admin\AdminServiceProvider"
- - php artisan admin:install
- 在backend文件夹下的中数据库：php artisan migrate
- 在backend文件夹下配置JWT：php artisan jwt:secret
- 在backend文件夹下创建public文件夹的链接（前端访问public文件夹）：php artisan storage:link
- 在backend文件夹下启动：php artisan serve
- 执行数据填充命令：php artisan db:seed 出错时，解决方法如下：composer dump-autoload
- 进入登录页面，需要执行 php artisan db:seed  ,登录名可以更改，密码是secret
## 篮球机器视觉分析

​	1.运行机器视觉分析：需要使用python3+pyqt5环境

​	2.在环境中进入basketballtrain文件夹，运行命令：

​		python  main.py即可运行