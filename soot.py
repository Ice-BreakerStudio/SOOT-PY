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
    # ��������
    db = pymysql.connect(host='localhost',
                         user='',
                         password='',
                         db='',
                         charset="utf8")    
    
    # ʹ��cursor()������ȡ�����α� 
    cursor = db.cursor()
    
    # SQL �������
    sql = 'INSERT IGNORE INTO yingchao (host, guest, round, time) VALUES (%s, %s, %s, %s)'
    try:
        # ִ��sql���
        cursor.execute(sql, (host, guest, mround, time))
        # �ύ�����ݿ�ִ��
        db.commit()
    except:
        # �������������ع�
        db.rollback()
    
    # �ر����ݿ�����
    db.close()    




for i in matchfather:
    pname=i.find('a')
    matchtime=i.find('span').string
    #��ȡ����˫��
    preal=pname.find('strong').string
    #���ַ�������VS�𿪳��б�
    teams=preal.split(" VS ")
    #������������������
    roundname=teams[0]
    mroundnum =re.search('Ӣ����(.*)��',roundname).end()
    mround =roundname[0:mroundnum]
    teams[0]=re.sub('Ӣ����(.*)��(\s)',"",teams[0])
    teams.append(mround)
    teams.append(matchtime)
    print (teams)
    #�������ݿ�
    insert_table(teams[0],teams[1],teams[2],teams[3])
    
    

print("All Done")