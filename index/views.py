from django.shortcuts import render
from django.http import HttpResponse
import pymysql

# Create your views here.


def indexView(request):
     # 1.我们先建立数据库的连接信息
    mysql = pymysql.connect(host="127.0.0.1",user="mysite",password="300716",db="mysite",port=3306,charset='utf8')

    #2.新建个查询页面
    cursor = mysql.cursor()
        
    #3编写sql
#     sql1 = 'select title from testmodel_movie'
#     sql2 = 'select level from testmodel_movie '
#     sql3 = 'select dramaType from testmodel_movie '
#     sql4 = 'select score from testmodel_movie '
#     sql5 = 'select formerName from testmodel_movie '
#     sql6 = 'select region from testmodel_movie '
#     sql7 = 'select language from testmodel_movie '
#     sql8 = 'select premiereDate from testmodel_movie '
#     sql9 = 'select type from testmodel_movie '

    sql10 = 'select * from movie'

    #4.执行sql保存结果
    # cursor.execute(sql1)
    # titles = cursor.fetchall() #用于返回多条数据
    # cursor.execute(sql2)
    # levels = cursor.fetchall() #用于返回多条数据
    # cursor.execute(sql3)
    # dramaTypes = cursor.fetchall() #用于返回多条数据
    # cursor.execute(sql4)
    # scores = cursor.fetchall() #用于返回多条数据
    # cursor.execute(sql5)
    # formerNames = cursor.fetchall() #用于返回多条数据
    # cursor.execute(sql6)
    # regions = cursor.fetchall() #用于返回多条数据
    # cursor.execute(sql7)
    # languages = cursor.fetchall() #用于返回多条数据
    # cursor.execute(sql8)
    # premiereDates = cursor.fetchall() #用于返回多条数据
    # cursor.execute(sql9)
    # types = cursor.fetchall() #用于返回多条数据
    # length=range(len(titles))
    
    cursor.execute(sql10)
    alldata = cursor.fetchall()     
    
    #5.关闭查询
    cursor.close()

    #关闭数据库
    mysql.close()

    #6.传参
    return render(request, 'index.html',locals())

def showView(request):
    nameValue = request.GET.get('name')
    keyValue = request.GET.get('key')
    
      # 1.我们先建立数据库的连接信息
    mysql = pymysql.connect(host="127.0.0.1",user="mysite",password="300716",db="mysite",port=3306,charset='utf8')

    #2.新建个查询页面
    cursor = mysql.cursor()
        
    #3编写sql
#     sql1 = 'select title from testmodel_movie'
#     sql2 = 'select level from testmodel_movie '
#     sql3 = 'select dramaType from testmodel_movie '
#     sql4 = 'select score from testmodel_movie '
#     sql5 = 'select formerName from testmodel_movie '
#     sql6 = 'select region from testmodel_movie '
#     sql7 = 'select language from testmodel_movie '
#     sql8 = 'select premiereDate from testmodel_movie '
#     sql9 = 'select type from testmodel_movie '
    if str(keyValue)=="电视剧":
        sql10 = 'select * from movie where '+str(nameValue)+" like '%剧%' "
    else:
        sql10 = 'select * from movie where '+str(nameValue)+' = "'+str(keyValue) +'"'

    #4.执行sql保存结果
    # cursor.execute(sql1)
    # titles = cursor.fetchall() #用于返回多条数据
    # cursor.execute(sql2)
    # levels = cursor.fetchall() #用于返回多条数据
    # cursor.execute(sql3)
    # dramaTypes = cursor.fetchall() #用于返回多条数据
    # cursor.execute(sql4)
    # scores = cursor.fetchall() #用于返回多条数据
    # cursor.execute(sql5)
    # formerNames = cursor.fetchall() #用于返回多条数据
    # cursor.execute(sql6)
    # regions = cursor.fetchall() #用于返回多条数据
    # cursor.execute(sql7)
    # languages = cursor.fetchall() #用于返回多条数据
    # cursor.execute(sql8)
    # premiereDates = cursor.fetchall() #用于返回多条数据
    # cursor.execute(sql9)
    # types = cursor.fetchall() #用于返回多条数据
    # length=range(len(titles))
    
    cursor.execute(sql10)
    alldata = cursor.fetchall()     
    
    #5.关闭查询
    cursor.close()

    #关闭数据库
    mysql.close()
    return render(request, 'show.html',locals())




