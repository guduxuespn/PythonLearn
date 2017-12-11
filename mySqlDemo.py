import mysql.connector

#创建config存储连接数据库所需的参数
config = {'host':'127.0.0.1',
'user':'root',
'password':'123456',
'port':'3306',
'database':'world',
'charset':'utf8'}

conn = mysql.connector.connect(**config)
print ('创建数据库连接成功')

cursor = conn.cursor()
print ('创建cursor成功')

cursor.execute ('select * from city t where t.Name =\'SÃ£o Leopoldo\';')

values=cursor.fetchall()

print (values)

#关闭连接
cursor.close()