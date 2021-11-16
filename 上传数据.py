import pymysql
conn=pymysql.connect('域名','root','密码')
conn.select_db('库名')
cur=conn.cursor()
sql="insert into user values(%s,%d)"
insert=cur.executemany(sql,[name,score])     # 玩家和分数
print('输入分数',insert)
cur.close()
conn.commit()
conn.close()
print('sql succeed')
#上传数据