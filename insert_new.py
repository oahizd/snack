#该文件主要实现将txt文件传入mysql数据库
import pymysql
import re
# import snaker
# snaker.main()

#变量初始化
con=pymysql.connect(            #需要在本地MySQL当中建立一个库，在库里建一个表用来存放数据
    host='localhost',
    port=3306,
    user='root',
    passwd='12345678',
    db='test',
    charset='utf8',
    )
def insert(con,id,score):
    #数据库游标！
    cue = con.cursor()
    # print("mysql connect success")  # 测试语句，这在程序执行时非常有效的理解程序是否执行到这一步
    #try-except捕获执行异常
    try:
        cue.execute(
            "insert into test_table2 (id,score) values(%s,%s)",
            [id,score,])
        #执行sql语句
        # print("insert success")  # 测试语句
    except Exception as e:
        print('Insert error:', e)
        con.rollback()
        #报错反馈
    else:
        con.commit()
        #真正的执行语句
def read():
    filename=r'scoring.txt'
    #按行读取txt文本文档
    with open(filename, 'r') as f:
        datas = f.readlines()
    #遍历文件
    for data in datas:
        txt=re.split(r'\t|\n',data)
        id=txt[0]
        score=txt[1]
        insert(con, id, score)
        #调用insert方法
    print("数据插入完成！")
read()
#执行read函数
con.close()
#关闭连接