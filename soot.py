# coding=gbk
import  urllib.request
import pymysql
import re
from bs4 import BeautifulSoup



headers ={'User-Agent':'Mozilla/5.0 (Linux; Android 4.2.1; M040 Build/JOP40D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.59 Mobile Safari/537.36'}
url = "http://www.cicizuqiu.com/zhibo/yingchao/"
req = urllib.request.Request(url=url,headers=headers)
res = urllib.request.urlopen(req)
html = res.read().decode("gbk")
soup = BeautifulSoup(html,"html5lib")
matchfather=soup.find("div",id="JM_List").find_all('td',class_="L")



def insert_table(host, guest, mround,time):
    # 建立连接
    db = pymysql.connect(host='localhost',
                         user='',
                         password='',
                         db='',
                         charset="utf8")    
    
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()
    
    # SQL 插入语句
    sql = 'INSERT IGNORE INTO yingchao (host, guest, round, time) VALUES (%s, %s, %s, %s)'
    try:
        # 执行sql语句
        cursor.execute(sql, (host, guest, mround, time))
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
    
    # 关闭数据库连接
    db.close()    




for i in matchfather:
    pname=i.find('a')
    matchtime=i.find('span').string
    #获取比赛双方
    preal=pname.find('strong').string
    #将字符串从用VS拆开成列表
    teams=preal.split(" VS ")
    #将比赛轮数单独出来
    roundname=teams[0]
    mroundnum =re.search('英超第(.*)轮',roundname).end()
    mround =roundname[0:mroundnum]
    teams[0]=re.sub('英超第(.*)轮(\s)',"",teams[0])
    teams.append(mround)
    teams.append(matchtime)
    print (teams)
    #插入数据库
    insert_table(teams[0],teams[1],teams[2],teams[3])
    
    

print("All Done")