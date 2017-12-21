#!/user/bin/python
# -*- coding : utf-8 -*-

import mysql.connector

#创建config存储连接数据库所需的参数
config = {'host':'127.0.0.1',
'user':'root',
'password':'123456',
'port':'3306',
'database':'world',
'charset':'utf8'}

createDbSql = "create database  if not exists `world`; "
useDbSql = 'use world;'
createTableSql = 'CREATE TABLE IF NOT EXISTS `city` (\
  `ID` int(11) NOT NULL,\
  `Name` char(35) NOT NULL ,\
  `CountryCode` char(3) NOT NULL ,\
  `District` char(20) NOT NULL ,\
  `Population` int(11) NOT NULL ,\
  PRIMARY KEY (`ID`),\
  KEY `CountryCode` (`CountryCode`),\
  CONSTRAINT `city_ibfk_1` FOREIGN KEY (`CountryCode`) REFERENCES `country` (`Code`)\
    ) ENGINE=InnoDB AUTO_INCREMENT=4080 DEFAULT CHARSET=latin1;'

conn = mysql.connector.connect(**config)
print ('创建数据库连接成功')

cursor = conn.cursor()
print ('创建cursor成功')

#执行sql语句
#创建数据库
cursor.execute(createDbSql)
print ('成功创建数据库')

cursor.execute (useDbSql)
print('成功切换数据库')

cursor.execute(createTableSql)
print('成功创建数据表')

cursor.execute ('select * from city t where t.Name =\'SÃ£o Leopoldo\';')

values=cursor.fetchall()

print (values)

#关闭连接
cursor.close()