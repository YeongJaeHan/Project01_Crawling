
##영재
from selenium import webdriver
import time


import pymongo
import cx_Oracle as oci

import requests
import json

conn=pymongo.MongoClient('192.168.99.100',32766)

db=conn.get_database("2019")  

table=db.get_collection("12")

conn=oci.connect('admin/1234@192.168.99.100:32764/xe', encoding='utf-8')

cursor=conn.cursor()




options=webdriver.ChromeOptions()
options.add_argument('headless')  #크롬이 실행은 되지만 안보임(백그라운드에서 돌아간다.)

options.add_argument("disable-gpu")   
options.add_argument("lang=ko_KR")    
#냅다 정보를 긁어오는게 아니라 창을 열어서 정보를 긁어온다. 
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 

driver=webdriver.Chrome('./chromedriver.exe',chrome_options=options)


for i in range(10,51,10):
    #for j in [10,19]:
        driver.get("https://datalab.naver.com/keyword/realtimeList.naver?age={}s&datetime=2020-01-14T12%3A56%3A00#none".format(i))
        print('=================',i,'================')
        time.sleep(3)
        ########방법1################################
        tag1=driver.find_element_by_class_name('item_num')
        tag2=driver.find_element_by_class_name('item_title')
        #######방법2#################################
        # tag=driver.find_elements_by_tag_name("span")


        for tmp in range(0,len(tag1),1):
            print(tmp.text.split("\n"))
            
            
            #################20200116############################
 from selenium import webdriver
import time


import pymongo
import cx_Oracle as oci

import requests
import json

######웹을 불러서 값얻어내기#######################
options=webdriver.ChromeOptions()
options.add_argument('headless')

options.add_argument("disable-gpu")   
options.add_argument("lang=ko_KR")    
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 

driver=webdriver.Chrome('./chromedriver.exe',chrome_options=options)
url="https://datalab.naver.com/keyword/realtimeList.naver?age={}s&datetime={}-{}-{}T{}%3A00%3A00&where=main".format('10','2020','01','16','11')

driver.get(url)

tag=driver.find_element_by_class_name('ranking_box').find_elements_by_tag_name('li')
time.sleep(3)


#######몽고에 저장하기################
conn=pymongo.MongoClient('192.168.99.100',32766)
db=conn.get_database("team") 
coll=db.get_collection("p20200116") #collection생성


rank=list()
word=list()

for tmp in tag:
    dict0=dict()
    book=tmp.text.split("\n")

    dict0['rank']=book[0]
    dict0['word']=book[1]
    dict0['day']='20200116'
    dict0['time']='11'
    coll.insert_one(dict0)

conn.close()
    
#######본격 정보 모으기#######
for m in ['01','02','03','04','05','06','07','08','09','10','11','12']:
    if (m=='01' or m=='03' or m=='05' or m=='07' or m=='08' or m=='10' or m=='12'):
        for d in range(1,32,1):
            for h in range()
            print("https://datalab.naver.com/keyword/realtimeList.naver?age=20s&datetime=2020-{}-{}T{0:2}%3A00%3A00&where=main".format(m, i))
    else:
        for i in range(1,31,1):
            print("https://datalab.naver.com/keyword/realtimeList.naver?age=20s&datetime=2020-{}-{}T14%3A00%3A00&where=main".format(m, i))


