import pymysql
db = pymysql.connect(host='localhost',user='用户名',db='本地数据库名',
                     password='密码',port=3306,charset='utf8')
cursor = db.cursor()
cursor.execute('select user,score from table order by score') #table表用user和score属性存放用户名和历史最高分数
aa = cursor.fetchmany(n) #获取排名前n位玩家的数据
for a in aa:
        print(a)
db.close()