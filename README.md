# fetch2mongodb
佛系程序员的开源爬虫项目，无框架，纯自我修行 -。-

一、没有装逼的英文文档。

二、可能配置说明方面会有点残缺，直接反馈吧。

三、如果连反馈都没有，叼，就这样吧。

五、中国人是不能有four的。


### 这项目用mongodb作为存储的，我的是3.2。

### 项目里的依赖我忘了，你看到缺什么就添加什么吧，我先列一下我记得的：

- requests
- mongoengine
- logging

### 配置项在config目录里

- default.py
    - database #数据库配置
    - runMode #运行时的配置
        - name #项目名

。。。。。。。。。。。

叼，太多，记不住了，你去运行一下就行了，慢慢玩。。。有问题Q我。

### 开始之前，先运行一下这个命令【python run.py config ybducom】，将配置config/json/cfg/里的【ybducom】json配置导入到库的cfg表里。

### 可以运行【python main.py】了。