#!/usr/bin/python
# -*- coding : utf-8 -*-

import sqlite3

conn = sqlite3.connect('mysqliteDemo')
print ('成功创建conn连接对象')

cursor = conn.cursor()
print ('成功创建cursor对象')

dropsqlstmt ='drop table persons ;'
createtablesqlstmt = "CREATE TABLE Persons  (Id_P int NOT NULL,LastName varchar(255) NOT NULL,FirstName varchar(255),Address varchar(255),City varchar(255))"                  
insertintosqlstmt = "insert into  Persons (Id_P,LastName,FirstName,Address,City) values (0,'san','zhang','abc','xian')"

cursor.execute(dropsqlstmt)
cursor.execute (createtablesqlstmt)
print ('创建数据表成功')

cursor.execute (insertintosqlstmt)
print ('成功插入数据')
selectsqlstmt = 'select * from persons'

content = cursor.execute (selectsqlstmt)

print (content)

values = cursor.fetchall()

print (values)

cursor.close()

conn.close()

