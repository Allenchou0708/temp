#!/usr/bin/env python
# coding: utf-8

# # 打開瀏覽器

user_cache=str(6)

from time import sleep
import os
import logging as log
from sys import argv,exit
from os.path import join
from time import sleep
from tqdm import tqdm 
from lxml import html
import pandas as pd
from random import uniform
from random import randrange
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import csv
import time
import urllib.request
from datetime import datetime,timedelta
from random import randint
#import mysql.connector
from datetime import date
from datetime import datetime
from JOJO import Zawarudo,Star_Platinum_Zawarudo,Roundabout,Havens_Door
import mysql.connector
from selenium.webdriver.common.by import By
import requests
import random

def to_buttom(driver,stop_time=15):
    scroll_amount = 300 ### more like people and without lag
    till_bottom = False
    loading_time = 0
    fail_bottom = False
    while (not till_bottom):
        print("Pull down",end=" ")
        #紀錄現在位置 + 下拉

        tree = html.fromstring(driver.page_source)
        find=tree.xpath("//div[@class='x1qjc9v5 x1q0q8m5 x1qhh985 xu3j5b3 xcfux6l x26u7qi xm0m39n x13fuv20 x972fbf x1ey2m1c x9f619 x78zum5 xds687c xdt5ytf x1iyjqo2 xs83m0k x1qughib xat24cr x11i5rnm x1mh8g0r xdj266r x2lwn1j xeuugli x18d9i69 x4uap5 xkhd6sd xexx8yu x10l6tqk x17qophe x13vifvy x1ja2u2z']/a/@href") ### Find all photo href
        if len(find)>=140: ### have read too many photo link
            print("Has collect enough photo link '_' ")
            break

        current_y = driver.execute_script("return window.pageYOffset;")            
        driver.execute_script("window.scrollBy(0, %d);" %(scroll_amount))    #下拉300

        #電腦讀取時間
        Star_Platinum_Zawarudo(stop_time,stop_time+5) ## 要讓照片讀取

        #頁面無法下拉 + 沒有在loading才能離開下拉功能
        if (driver.execute_script("return window.pageYOffset;") == current_y):
            till_bottom =True
        #不然就繼續迴圈
    print("\nDONE")


# options.add_experimental_option("detach", True)
# proxy = '163.172.190.160:8811'
# chrome_options.add_argument('--proxy-server=https://%s' % proxy )


from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
#options.add_argument(r"--user-data-dir=/home/mamao")
prefs = {"profile.managed_default_content_settings.images": 1} # 2:NO 圖片 / 1:有圖片
options.add_experimental_option("prefs", prefs)

options.add_argument("--lang=en-us")
#options.add_argument("--start-maximized")
options.add_argument(r"--user-data-dir=/home/mamao/user_cache/test"+user_cache)

#driver = webdriver.Chrome(options = options, executable_path = './chromedriver.exe')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

def Get_user_photo(user_primary_key,user_url):
    
    up_limit_of_photo=80

    try:
        driver.get(user_url)
    except:
        print("Can't goto user_www_page,break")
        return

    Star_Platinum_Zawarudo(10,15)

    while_limit=0
    find=[] 
    ### CAN Cooperate into big while

    while len(find)==0:

        if while_limit==0:
            for x in range(randint(3,4)):
                move=random.choice([200,250,300,350,400])
                driver.execute_script("window.scrollBy(0,"+str(move)+")")
                print("scroll: ",move)
                time.sleep(random.uniform(5,15))
        else:
            move=random.choice([200,250,300,350,400])
            driver.execute_script("window.scrollBy(0,"+str(move)+")")
            print("scroll: ",move)
            time.sleep(random.uniform(5,15))    
        
        tree = html.fromstring(driver.page_source) 
        
        ###find=tree.xpath("//a[text() = 'See all photos']/@href") Can't use this cause the html file
        find=tree.xpath("//div[@class='x9f619 x1n2onr6 x1ja2u2z x78zum5 x2lah0s x1qughib x1qjc9v5 xozqiw3 x1q0g3np']/a/@href") 
        #Havens_Door(driver,"photo_find_see_all_photo"+str(while_limit))
        
        print("original find=",find)
        for i in find:
            if i.find("login")!=-1:
                find.remove(i)
                continue
            if i.find("friend")!=-1:
                find.remove(i)
                continue
            if i.find("notifications")!=-1:
                find.remove(i)
                continue
            if i.find("year-overviews")!=-1:
                find.remove(i)
                continue
            
        print("in ",while_limit,"round, find=",find)
        
        while_limit+=1
        if while_limit>=40:
            break
    
    try:
        photo_page_url=find[0]
        driver.get(find[0]) ### Into Photo Page
    except:
        print("Can't find photo page link")
        return 0
    
    Star_Platinum_Zawarudo(5,10)

    to_buttom(driver)

    tree = html.fromstring(driver.page_source)

    find=tree.xpath("//div[@class='x1qjc9v5 x1q0q8m5 x1qhh985 xu3j5b3 xcfux6l x26u7qi xm0m39n x13fuv20 x972fbf x1ey2m1c x9f619 x78zum5 xds687c xdt5ytf x1iyjqo2 xs83m0k x1qughib xat24cr x11i5rnm x1mh8g0r xdj266r x2lwn1j xeuugli x18d9i69 x4uap5 xkhd6sd xexx8yu x10l6tqk x17qophe x13vifvy x1ja2u2z']/a/@href") ### Find all photo href

    link_list=[]
    video_number=0
    for index,link in enumerate(find):
        if link.find("video") != -1:
            video_number+=1
            continue
        link_list.append(link)

    print("Media Length = ",len(find))
    print("Video Length = ",video_number)
    print("Photo Length =",len(link_list))
    
    total_photo=len(link_list)
    print("test: available photo len = ",total_photo)

    Havens_Door(driver,"user_photo_in_the_photo_page")

    try: ### actually m_photo_url
        mbasic_photo_url=link_list[0].replace("https://www.facebook.com","https://m.facebook.com")
        print("\n%1 photo:",mbasic_photo_url)
    except:
        print("No photo, or has error in finding first photo")
        return

    try:
        driver.get(mbasic_photo_url)    ### go to photo[0]
        Star_Platinum_Zawarudo(15,20)
    except:
        print("Can't go to m")

    ###################################### DE to here

    issue_photo=0
    if total_photo<=40:
        uplimit_issue_photo=5
    else:
        uplimit_issue_photo=10

    for i in range(total_photo):
        
        if i >= up_limit_of_photo:
            print("too many photos")
            break

        if issue_photo>uplimit_issue_photo:

            ### Record to DB

            mydb = mysql.connector.connect(
                host="localhost",
                user="allenchou",
                passwd="dmlab62296",
                database="fb"
            )
            mycursor = mydb.cursor()
            try:
                sqlfunc = "INSERT INTO photo_break(user_id,recrawl,abandon) VALUE (%s,%s,%s)"
                mycursor.execute(sqlfunc,(user_url[24:],False,False))
                mydb.commit()
            except:
                print("Error: Writing into photo_break")

            print("Can't read too much photo, break")
            break


        tree = html.fromstring(driver.page_source)
        find=tree.xpath("//div[@class='area error']")
        
        if len(find) !=0 : ### 讀取失敗
            print("error happen")
            if i+1>=total_photo:
                break
            else:
                print("photo["+str(i)+"] has issue")
                driver.get(photo_page_url)
                Star_Platinum_Zawarudo(5,10)
                to_buttom(driver)
                tree = html.fromstring(driver.page_source)
                find=tree.xpath("//div[@class='x1qjc9v5 x1q0q8m5 x1qhh985 xu3j5b3 xcfux6l x26u7qi xm0m39n x13fuv20 x972fbf x1ey2m1c x9f619 x78zum5 xds687c xdt5ytf x1iyjqo2 xs83m0k x1qughib xat24cr x11i5rnm x1mh8g0r xdj266r x2lwn1j xeuugli x18d9i69 x4uap5 xkhd6sd xexx8yu x10l6tqk x17qophe x13vifvy x1ja2u2z']/a/@href")
                print("find_length=",len(find))
                print(find[i+1].replace("https://www.facebook.com","https://mbasic.facebook.com"))
                mbasic_photo_url=find[i+1].replace("https://www.facebook.com","https://mbasic.facebook.com")
                driver.get(mbasic_photo_url)
       
        else:    
            
           #### MAX the photo and Click Next
            tree = html.fromstring(driver.page_source)
            find=tree.xpath("//a[text() = 'View Full Size']/@href")  ### You can change to text()=View Full Size
            

            #print("find_length=",len(find))
            # print(find[0]) ### 全畫面照片的連結

            if len(find)==0:
                print("It has issue finding the link to full-size picture")
                ### 最好加個Photo Failed
                print("driver.title,",driver.title)
                if driver.title.find("You’re Temporarily Blocked")!=-1:

                    ### account_retu
                    mydb = mysql.connector.connect(
                        host="localhost",
                        user="allenchou",
                        passwd="dmlab62296",
                        database="fb"
                    )
                    mycursor = mydb.cursor()

                    try:
                        sqlfunc = "UPDATE fb_id SET photo_finished = '0' WHERE user_id ='"+ user_url[24:] + "';"
                        mycursor.execute(sqlfunc)
                        mydb.commit()
                    except:
                        print("Back to normal (in db) error")

                    print("Being Banned, THE account is back to normal")
                    exit()

                Havens_Door(driver,"user_photos_6_check_Full_Size")
                issue_photo+=1
                continue

            if find[0].find("https:") !=0: ###正常抓到會從/開始
                driver.get("https://mbasic.facebook.com"+find[0])
            else:   ###處理refference的網址
                print("photo["+str(i)+"] has issue")

                redo_limit=3
                now_redo=0
                stop_time=15

                while True:
                    driver.get(photo_page_url)
                    Star_Platinum_Zawarudo(5,10)
                    to_buttom(driver,stop_time)
                    tree = html.fromstring(driver.page_source)
                    find=tree.xpath("//div[@class='x1qjc9v5 x1q0q8m5 x1qhh985 xu3j5b3 xcfux6l x26u7qi xm0m39n x13fuv20 x972fbf x1ey2m1c x9f619 x78zum5 xds687c xdt5ytf x1iyjqo2 xs83m0k x1qughib xat24cr x11i5rnm x1mh8g0r xdj266r x2lwn1j xeuugli x18d9i69 x4uap5 xkhd6sd xexx8yu x10l6tqk x17qophe x13vifvy x1ja2u2z']/a/@href")
                    print("find_length=",len(find))
                    if i+1<len(find):
                        break
                    now_redo+=1
                    stop_time+=5
                    print("Fail for refind the photo")
                    if now_redo>=redo_limit:
                        break

                if now_redo>=redo_limit:
                    print("Redo too much time, Next user")
                    break
                    
                print(find[i+1].replace("https://www.facebook.com","https://mbasic.facebook.com"))
                mbasic_photo_url=find[i+1].replace("https://www.facebook.com","https://mbasic.facebook.com")
                driver.get(mbasic_photo_url)
                continue

            Star_Platinum_Zawarudo(5,10)

            tree = html.fromstring(driver.page_source)
            find=tree.xpath("//img/@src")
            print("find=",find) ### 在全畫面照片取得url
            if len(find)==0:
                print("It has issue downloading full-size picture")
                ### 最好加個Photo Failed
                break
            photo_back = requests.get(find[0])

            try:
                os.mkdir('/home/mamao/get_photo/'+str(user_primary_key)) 
            except:
                print("Has establish the same folder")
            
            try:
                with open('/home/mamao/get_photo/'+str(user_primary_key)+'/'+str(i)+'.jpg', "wb") as file:
                    file.write( photo_back.content)
            except :
                print("It has the same_name file")

            Star_Platinum_Zawarudo(5,10)
            driver.get(mbasic_photo_url)
            print("return back")
            Star_Platinum_Zawarudo(5,10)

           # tree = html.fromstring(driver.page_source)
           # find=tree.xpath("//a[@class='t']/@href")
            #find_1=tree.xpath("//a[@class='r']/@href")
            #find_2=tree.xpath("//a[@class='s']/@href")
            #next_list=[len(find),len(find_1),len(find_2)]
           # candidate_url=[find,find_1,find_2]

            #next_url=""
            #for index, i in enumerate(next_list):
            #    if i <2:
            #        continue
            #    else:
            #        next_url= candidate_url[index][1]
            #        break

            #if next_url=="":
            #    print("Can't go to next photo")
            #    Zawarudo(180)
            #    break
            #else:
            #    mbasic_photo_url="https://mbasic.facebook.com"+next_url

                ### ###
            next_num=i+1
            try:
                print("next_num=",next_num)
                mbasic_photo_url=link_list[next_num]
                mbasic_photo_url=mbasic_photo_url.replace("https://www.facebook.com","https://m.facebook.com")
            except:
                print("Issue finding next m-photo")
                break
            print("\n%",i+1," ",mbasic_photo_url)
            driver.get(mbasic_photo_url)
            Star_Platinum_Zawarudo(5,10)


def choose_user(test_mode=False):

    if test_mode==True:
        return "/ariel.schuler?eav=AfZ-dml_SEHlybvHAV06IojsvA_xQgGopbUBd92SLPWhI77_zQwSN6dN1qpggCaX6nU&fref=nf&rc=p&__tn__=R"

    ###改用database
    mydb = mysql.connector.connect(
        host="localhost",
        user="allenchou",
        passwd="dmlab62296",
        database="fb"
    )
    mycursor = mydb.cursor()

    try:
        sqlfunc = "SELECT DISTINCT user_id FROM fb_id WHERE photo_finished='0' AND too_few='0' AND finished='1' AND no_like='0' LIMIT 1 ;"
        mycursor.execute(sqlfunc)
        re = mycursor.fetchone()
        post=re[0]
        
    except:
        print("All of the user's photo has been collect")
        exit()

    sqlfunc = "UPDATE fb_id SET photo_finished = '1' WHERE user_id ='"+ post + "';"

    try:
        mycursor.execute(sqlfunc)
        mydb.commit()
    except:
        print("Modify photo_finished error")
    
    return post


def modify_photo_finished(user_id):

    ###改用database
    mydb = mysql.connector.connect(
        host="localhost",
        user="allenchou",
        passwd="dmlab62296",
        database="fb"
    )
    mycursor = mydb.cursor()


### Start of the code
    
number_of_user=10
how_many_run=2

begin = datetime.now()
print("*** start: ", begin,"\n")

for run in range(how_many_run):
    for i in range(number_of_user):

        print("NO."+str(i))
        
        user_url=choose_user()
       
        file_name=user_url
        file_name=file_name.replace("?","")
        file_name=file_name.replace("=","")
        file_name=file_name.replace("&","")
        file_name=file_name.replace(" ","")
        user_primary_key=file_name

        print("user_id=",user_url)
        print("user_primary_key=",user_primary_key)

        user_url="https://www.facebook.com"+user_url
        print("user_url=",user_url)

        start = time.time()

        Get_user_photo(user_primary_key,user_url)
        
        end = time.time()
        print ("This photo spend: " , end-start)
        Star_Platinum_Zawarudo(5,10)

        print("======")

        check_time=datetime.now()
        if check_time-begin > timedelta(hours=3): ###
            print("We have crawl the photo too long")
            break

        Star_Platinum_Zawarudo(60,120)
    
    ending = datetime.now()
    print("****** Run ",run," end at : ", ending)
    print("****** This run cose : ", ending - begin)

    rest_min=randint(40,80)
    print("We will rest ",rest_min," mins")
    for i in range(rest_min) :
        sleep(60)

ending = datetime.now()
print("*** end: ", ending)
print("*** total time:", ending - begin)
