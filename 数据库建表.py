import pymysql
conn = pymysql.connect('域名',user = "root",passwd = "密码",db = "库名")
cursor=conn.cursor()
print(cursor)
cursor.execute('drop table if exists user')
sql="""CREATE TABLE IF NOT EXISTS `user` (
      `name` vaechar(20) NOT NULL AUTO_INCREMENT,
      `score` numeric(10,2) NOT NULL,
      PRIMARY KEY (`name`)
    ) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=0"""
cursor.execute(sql)
cursor.close()
conn.close()
print('succeed')
#在数据库中建表