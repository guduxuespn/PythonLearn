#!/usr/bin/python
# -*- coding : utf-8 -*-

import sqlite3
import os

pathOfInsertIntoDataToCity = os.path.abspath('.\.\sql\insertIntoDataToCity.sql')
#os.open('././sql/insertIntoDataToCity.sql')
print(pathOfInsertIntoDataToCity)
f=open(pathOfInsertIntoDataToCity)


conn = sqlite3.connect('mysqliteDemo')
print ('成功创建conn连接对象')

cursor = conn.cursor()
print ('成功创建cursor对象')

createDbSql = "create database  if not exists `world`; "
useDbSql = 'use world;'
createTableSql = 'CREATE TABLE IF NOT EXISTS `city` (\
  `ID` int(11) PRIMARY KEY NOT NULL,\
  `Name` char(35) NOT NULL ,\
  `CountryCode` char(3) NOT NULL ,\
  `District` char(20) NOT NULL ,\
  `Population` int(11) NOT NULL \
    );'


selectDataSql ='select * from city t where t.Name =\'Kabul\';'


# cursor.execute(createDbSql)
# cursor.execute (useDbSql)
cursor.execute(createTableSql)
print ('创建数据表成功')

cursor.executescript('.\.\sql\insertIntoDataToCity.sql')

cursor.execute("INSERT INTO `city` (`ID`, `Name`, `CountryCode`, `District`, `Population`) VALUES (1, 'Kabul', 'AFG', 'Kabol', 1780000),(2, 'Qandahar', 'AFG', 'Qandahar', 237500)")
	 


content=cursor.execute (selectDataSql)
print ('成功查询数据')




print (content)

values = cursor.fetchall()

print (values)

cursor.close()

conn.close()

