from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import random
import time
import datetime
import socket
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

file_path='/MachintoshHD/Users/shailysaigal/Downloads'
chromeoptions = Options()
if socket.gethostname()=='c063144':
    driver = webdriver.Chrome(executable_path="C:\\Users\\vivek4\\Downloads\\chromedriver\\chromedriver.exe", chrome_options=chromeoptions)
    file_path='C:\\Users\\vivek4\\Downloads\\'
else:
    driver = webdriver.Chrome()

driver.get("https://aisel.aisnet.org/do/search")
time.sleep(random.randint(20,30))
adv=driver.find_element_by_id("switch-to-advanced")
adv.click()
time.sleep(random.randint(20,30))

nbutton1=driver.find_element_by_xpath("//a[@aria-label='dismiss cookie message']")
nbutton1.click()

select_fr = Select(driver.find_element_by_id("field_1"))
select_fr.select_by_index(1)

search_box = driver.find_element_by_id("value_1")
time.sleep(3)
search_box.send_keys("crowdfunding")
time.sleep(random.randint(20,30))
#start_date=driver.find_element_by_name("start_date")
#start_date.click()
#start_date.send_keys("01/01/1985")
#time.sleep(random.randint(20,30))

#end_date=driver.find_element_by_name("end_date")
#end_date.click()
#end=time.time()
#end_date.send_keys(datetime.datetime.fromtimestamp(end).strftime('%m/%d/%Y '))
time.sleep(3)
search_button = driver.find_element_by_id("do-search-advanced")
search_button.submit()
#search_button.send_keys(Keys.RETURN)
time.sleep(random.randint(60,70))


#search_button = driver.find_element_by_name("query")
#search_box.send_keys(Keys.RETURN)
#abstract=driver.find_element_by_xpath("//select[@name='field_1']/option[text()='Abstract']")
#abstract.click()

#time.sleep(random.randint(10, 15))

url = driver.current_url
actual_url=url+"publication_type%3AJournal#"
print(actual_url)
time.sleep(10)
driver.get(actual_url)
time.sleep(random.randint(15, 20))

while(True):
    header_list=driver.find_element_by_xpath("//div[@id='results-list']")
    header_title=header_list.find_elements_by_xpath("//span[@class='title']")
    with open('links2.csv','a') as f:
        for header in header_title:
           headers= header.find_element_by_tag_name('a')
           x=headers.get_attribute('href')
           f.write(x+" \n")
        f.close()
    time.sleep(10)
    
    try:
        nbutton=driver.find_element_by_xpath("//a[@id='next-page']")
        nbutton.click()
        time.sleep(random.randint(15, 20))
    except:
        print("No more pages..")
        break

driver.close()
