
# coding: utf-8

# In[1]:


import requests
import selenium
import pymysql
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


conn=pymysql.connect(user='EDYR', passwd='edyr1221', host='edyrdb.cfhg3eem9b5e.us-east-2.rds.amazonaws.com', db='edyrdb', charset='utf8')

cur= conn.cursor()

#max page 찾기
path='C:/Users/고예랑/Desktop/chromedriver.exe'
driver=webdriver.Chrome(path)
driver.get('http://new.sungshin.ac.kr/web/kor/comm010101?p_p_id=EXT_BBS&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-1&p_p_col_pos=1&p_p_col_count=2&_EXT_BBS_struts_action=%2Fext%2Fbbs%2Fview&_EXT_BBS_sCategory=&_EXT_BBS_sTitle=&_EXT_BBS_sWriter=&_EXT_BBS_sTag=&_EXT_BBS_sContent=&_EXT_BBS_sCategory2=&_EXT_BBS_sKeyType=&_EXT_BBS_sKeyword=&_EXT_BBS_curPage=1')
a=driver.find_elements_by_xpath('//*[@id="p_p_id_EXT_BBS_"]/div/div/div[2]/table[2]/tbody/tr/td[2]/div/a[11]')
driver.get(a[0].get_attribute('href'))
href=driver.current_url
#print(href)

max=href[-3:-1]+href[-1]
max=int(max)
#print(max)



# In[13]:


import pymysql

conn=pymysql.connect(user='EDYR', passwd='edyr1221', host='edyrdb.cfhg3eem9b5e.us-east-2.rds.amazonaws.com', db='edyrdb', charset='utf8')

cursor= conn.cursor()


sql= """
     create table haksa28(
            title nvarchar(1000) primary key,
            href nvarchar(1000) ,
            article nvarchar(4000)
            )
   
"""


cursor.execute(sql)
conn.commit()


# In[14]:


url=[]
name=[]
article=[]
page = 110
k = 0
aa = 0
while page <= 110:
    url='http://new.sungshin.ac.kr/web/kor/comm010101?p_p_id=EXT_BBS&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-1&p_p_col_pos=1&p_p_col_count=2&_EXT_BBS_struts_action=%2Fext%2Fbbs%2Fview&_EXT_BBS_sCategory=&_EXT_BBS_sTitle=&_EXT_BBS_sWriter=&_EXT_BBS_sTag=&_EXT_BBS_sContent=&_EXT_BBS_sCategory2=&_EXT_BBS_sKeyType=&_EXT_BBS_sKeyword=&_EXT_BBS_curPage=111'
    source_code=requests.get(url)
    plain_text=source_code.text
    soup=BeautifulSoup(plain_text,'html.parser')
    page = page + 1
    for link in soup.select('td > a'):
        href= link.get('href') 
        title=link.get_text(strip = True)
#         print(title)
#         sql = 'INSERT INTO haksa21 (title) VALUES("' + str(title.encode('utf8')) + '")'
#         sql = 'INSERT INTO haksa23 (title,href) VALUES("' + str(title) + '","' + str(href) + '")'
#         sql = 'INSERT INTO haksa10 (title) VALUES("' + title.decode('euc-kr') + '")'
#         print(sql)

        source_code=requests.get(href)
        plain_text=source_code.text
        soup=BeautifulSoup(plain_text,'html.parser')
    
    
# 
        for contents in soup.select('#p_p_id_EXT_BBS_ > div > div > div.contents > table.bbs-body'):
                        article = contents.text
                        print(title)
                        
                        sql = 'INSERT INTO haksa28 (title,href,article) VALUES("' + str(title) + '","' + str(href) + '","' + str(article) +'")'
#                                     sql = 'INSERT INTO haksa24 (title,href) VALUES("' + str(title) + '","' + str(href) +'")'
                        cursor.execute(sql)
                        conn.commit()
#                                        print(contents.text)
#                                         article += contents.text


#                                         print(article)
#                                         sql="""
#                                             insert ignore into haksa values(href, title, article)
#                                         """
#                                         cursor.execute(sql)
        conn.commit()
                                            
        
    
cursor.execute(sql)    
conn.commit()
       
#     sql = 'INSERT INTO haksa14 (title) VALUES("'+ str('abcd') + '")'
#     cursor.execute(sql)


# In[305]:


conn.commit()


# In[6]:


sql = "SELECT * FROM haksa26"
cursor.execute(sql)
result = cursor.fetchall()
for row_data in result:
    print(row_data[0])
    print(row_data[1])
    print(row_data[2])

