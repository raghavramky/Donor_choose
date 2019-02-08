from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import random
import socket
import time
from selenium.webdriver.support.select import Select

#file_path='/MachintoshHD/Users/shailysaigal/Downloads'

key1=input("Enter a keyword to be searched::")
field1=input("Enter the field to be searched::")
print("Do you want to insert more keywords")
choice1=input("Enter your choice(Yes/No)::")
if(choice1=="Yes"):
    key2=input("Enter a keyword to be searched::")
    field2=input("Enter the field to be searched::")
    print("Do you want to insert more keywords")
    choice2=input("Enter your choice(Yes/No)::")
    if(choice2=="Yes"):
        key3=input("Enter a keyword to be searched::")
        field3=input("Enter the field to be searched::")
    else:
        key3=""
        field3=""
else:
    key2=""
    field2=""
    key3=""
    field3=""

if(field1=="Anywhere" or field1=="anywhere"):
    field1="AllField"
elif(field1=="Title" or field1=="title"):
    field1="Title"
elif(field1=="Author" or field1=="author"):
    field1="Contrib"
elif(field1=="Keyword" or field1=="keyword"):
    field1="Keyword"
else:
    field1=""


if(field2=="Anywhere" or field2=="anywhere"):
    field2="AllField"
elif(field2=="Title" or field2=="title"):
    field2="Title"
elif(field2=="Author" or field2=="author"):
    field2="Contrib"
elif(field2=="Keyword" or field2=="keyword"):
    field2="Keyword"
else:
    field2=""


if(field3=="Anywhere" or field3=="anywhere"):
    field3="AllField"
elif(field3=="Title" or field3=="title"):
    field3="Title"
elif(field3=="Author" or field3=="author"):
    field3="Contrib"
elif(field3=="Keyword" or field3=="keyword"):
    field3="Keyword"
else:
    field3="AllField"

#print(type(key1))
if(key1.find(' ',1)!=-1):
    key1=key1.replace(' ','+')
    
if(key2.find(' ',1)!=-1):
    key2=key2.replace(' ','+')

if(key3.find(' ',1)!=-1):
    key3=key3.replace(' ','+')
    #print("%s"%key1)

#print("%s  %s"%(key1,field1))
#print("%s  %s"%(key2,field2))
#print("%s  %s"%(key3,field3))

driver = webdriver.Chrome()
driver.get("https://pubsonline.informs.org")
time.sleep(5)
url = driver.current_url
actual_url=url+"action/doSearch?field1="+field1+"&text1="+key1+"&field2="+field2+"&text2="+key2+"&field3="+field3+"&text3="+key3+"&publication=&Ppub=&Ppub=&AfterMonth=&AfterYear=&BeforeMonth=&BeforeYear="
print(actual_url)
#time.sleep(10)
driver.get(actual_url)
time.sleep(random.randint(10, 20))

nbutton=driver.find_element_by_xpath("//a[@class='btn ib-blue-bg cookiePolicy-popup__close close']")
nbutton.click()
time.sleep(5)

while(True):
    header_list=driver.find_element_by_xpath("//ul[@class='rlist search-result__body items-results ']")
    header_box=header_list.find_elements_by_xpath("//div[@class='item__body']")                                       

    time.sleep(random.randint(15, 20))
    with open('links.csv','a') as f:
        for header in header_box:
            headers=header.find_element_by_tag_name('a')
            x=headers.get_attribute('href')
            f.write(x+"\n")
        f.close
    time.sleep(random.randint(15, 30))
    try:
        next_button=driver.find_element_by_xpath("//a[@title='Next Page']")
        next_button.send_keys(Keys.RETURN)
        time.sleep(random.randint(10, 15))
    except:
        print("No more pages..")
        break

driver.close()