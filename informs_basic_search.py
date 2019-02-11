from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import random
import socket
import time

file_path='/MachintoshHD/Users/shailysaigal/Downloads'
driver = webdriver.Chrome()

driver.get("https://pubsonline.informs.org")
time.sleep(5)

nbutton=driver.find_element_by_xpath("//a[@class='btn ib-blue-bg cookiePolicy-popup__close close']")
nbutton.click()
time.sleep(5)

#search_box = driver.find_element_by_name("AllField")
search_box=driver.find_elements_by_xpath("//input[@name='AllField']")
time.sleep(10)
search_box[2].send_keys("open source")
time.sleep(5)
search_box[2].send_keys(Keys.RETURN)
time.sleep(random.randint(15, 20))

url = driver.current_url
actual_url=url+"&startPage=0&pageSize=100"
print(actual_url)
driver.get(actual_url)
time.sleep(random.randint(15, 20))

#page_size=driver.find_element_by_xpath('//a[@href="https://pubsonline.informs.org/action/doSearch?AllField=open+source&amp;startPage=0&amp;pageSize=100"]')
#page_size.click()

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


