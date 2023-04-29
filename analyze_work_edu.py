import csv
import re

work_list=[]
edu_list=[]

def check_whether_time(part):
    for i in range(1980,2024):
        if part.find(str(i))!=-1:
            return True
    
    for i in ["January","February","March","April","May","June","July","August","September","October","November","December"]: 
        if part.find(i)!=-1:
            return True
    
    return False



### for work

with open ("perfect_user_data.csv","r",newline="") as csvfile:
    rows=csv.reader(csvfile)

    
    ### Naive Crawl for job list (slot before time)

    ### we can design more rule like the slot space to precisely get it

    ### we can regular these varifying jobs to normal jobs like 20 category (by hard code?)

    for row_num,i in enumerate(rows):
        i=i[0]
        analyza_row=i.split("、、、")
        work_list.append([])
        for index,work_part in enumerate(analyza_row):
            if check_whether_time(work_part) == True and index-1 >=0:
                #print("get work : ", analyza_row[index-1])
                work_list[row_num].append(analyza_row[index-1])
            else:
                pass


with open ("perfect_user_data.csv","r",newline="") as csvfile:
    rows=csv.reader(csvfile)
    ### for edu
    for i in rows:
        #print(i[1])
        if i[1]=="":
            edu_list.append(i[1])
        else:
            temp_edu=""
            if i[1].find("High school")!=-1:
                temp_edu="High School"
            if i[1].find("College")!=-1 or i[1].find("Bachelor")!=-1 or i[1].find("University")!=-1:
                temp_edu="University"
            if i[1].find("Master")!=-1 or i[1].find("Graduate School")!=-1:
                temp_edu="Master"

            if temp_edu=="":
                temp_edu="" 
                print("Error convertion check ",i)

            edu_list.append(temp_edu)


#### now you can use edu_list , work_list for each user

print("Edu length=",len(edu_list))
print("Work length=",len(work_list))

"""
for index,i in enumerate(work_list):
    print(i)
    if index >= 50:
        break
"""


