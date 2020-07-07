# -*- coding: utf-8 -*-
import pymysql


#连接数据库
config = {'host':'',
          'port':3306,
          'user':'mysite',
          'passwd':'300716',
          'charset':'utf8mb4',
          'local_infile':1
          }
conn = pymysql.connect(**config)
cur = conn.cursor()


#load_csv函数，参数分别为csv文件路径，表名称，数据库名称
def load_csv(csv_file_path,table_name,database='mysite'):
    #打开csv文件
    file = open(csv_file_path, 'r', encoding='utf-8')
    #读取csv文件第一行字段名，创建表
    reader = file.readline()
    b = reader.split(',')
    colum = ''
    for a in b:
        colum = colum + a + ' varchar(255),'
    colum = colum[:-1]
    #编写sql，create_sql负责创建表，data_sql负责导入数据
    delete_sql = 'drop table if exists movie'
    create_sql = 'create table if not exists ' + table_name + ' ' + '(' + colum + ')' + ' DEFAULT CHARSET=utf8'
    data_sql = "LOAD DATA LOCAL INFILE '%s' INTO TABLE %s FIELDS TERMINATED BY ',' LINES TERMINATED BY '\\r\\n' IGNORE 1 LINES" % (csv_file_path,table_name)
 
    #使用数据库
    cur.execute('use %s' % database)
    #设置编码格式
    cur.execute('SET NAMES utf8;')
    cur.execute('SET character_set_connection=utf8;')
    #执行delete_sql，删除表
    cur.execute(delete_sql)
    #执行create_sql，创建表
    cur.execute(create_sql)
    #执行data_sql，导入数据
    cur.execute(data_sql)
    conn.commit()
    #关闭连接
    conn.close()
    cur.close()

# title	level	dramaType	score	formerName	region	language	premiereDate	type
# def load_once(csv_file_path,table_name,database='test',info):
#     insert_sql = "INSERT INTO 'movie' ('title', 'level', 'dramaType', 'score', 'formerName', 'region', 'language', 'premiereDate', 'type') VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')"
#     .format(info['title',])

    

if __name__ == "__main__":
    load_csv('C:/wwwroot/ningning99.cn/mysite/spider/result.csv','movie')
    # load_csv('D:/Software/PythonProject/mysite/spider/result.csv','movie')
