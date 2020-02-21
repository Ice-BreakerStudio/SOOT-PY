# SOOT-Python
## 简介
这里是Soot APP的爬虫库，用于爬取网络上我们所需的信息并存入MySQL数据库
## 配置
- 编译与运行前请安装Python3
- 另外需要安装扩展包
  - BeautifulSoup4
  - html5lib
  - PyMySQL
```
pip install beautifulsoup4
pip install html5lib
pip install PyMySQL
```

由于是爬取数据后存入数据库中，我们也需要配置MySQL数据库
这里我们以英超赛程为例
新建一个名为yingchao的表，如图四个字段

![image](https://raw.githubusercontent.com/Ice-BreakerStudio/SOOT-PY/master/README.assets/mysql1.png)

并且设置主键，防止插入重复数据，如图

![image](https://raw.githubusercontent.com/Ice-BreakerStudio/SOOT-PY/master/README.assets/mysql2.png)

并且在Python文件的21-25行处

```python
db = pymysql.connect(host='localhost',
                         user='',
                         password='',
                         db='',
                         charset="utf8")
```

配置好自己的MySQL相关变量

## 运行

进入Python文件所在路径，执行

```
python soot.py
```

即可获取未来几日的英超赛程信息
