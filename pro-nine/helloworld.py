#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Jason Mess


# 导入Flask类
# 第三次
# 第四次
from flask import Flask
# Flask函数接收一个参数__name__，它会指向程序所在的包

app = Flask(__name__)


# 装饰器的作用是将路由映射到视图函数 index
@app.route('/')
def index():
    return 'Hello World'
# Flask应用程序实例的 run 方法 启动 WEB 服务器


# url_map 将装饰器路由和视图的对应关系保存起来
if __name__ == '__main__':
    app.run()

# 程序员修改的第一行代码

