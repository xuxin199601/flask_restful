#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "", "students", charset='utf8' )

cursor = db.cursor()
sql = "delete from student where id = 1"
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 提交修改
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()

# 使用 fetchone() 方法获取一条数据
# data = cursor.fetchone()

# print("Database version :", data)

# 关闭数据库连接
db.close()