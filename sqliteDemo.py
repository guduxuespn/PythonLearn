#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('mysqliteDemo')
print ('成功创建conn连接对象')

cursor = conn.cursor()
print ('成功创建cursor对象')

dropsqlstmt ='drop table persons ;'
sqlstmt = "CREATE TABLE Persons  (Id_P int NOT NULL,LastName varchar(255) NOT NULL,FirstName varchar(255),Address varchar(255),City varchar(255))"                  

cursor.execute(dropsqlstmt)
cursor.execute (sqlstmt)
print ('创建数据表成功')

selectsqlstmt = 'select * from persons'

content = cursor.execute (selectsqlstmt)

print (content)


