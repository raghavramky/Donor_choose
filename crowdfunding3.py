from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import random
import time
import datetime
import socket
from selenium.webdriver.chrome.options import Options

file_path='/MachintoshHD/Users/shailysaigal/Downloads'
chromeoptions = Options()
if socket.gethostname()=='c063144':
    driver = webdriver.Chrome(executable_path="C:\\Users\\vivek4\\Downloads\\chromedriver\\chromedriver.exe", chrome_options=chromeoptions)
    file_path='C:\\Users\\vivek4\\Downloads\\'
else:
    driver = webdriver.Chrome()

driver.get("https://aisel.aisnet.org/do/search")
time.sleep(5)
search_box = driver.find_element_by_name("q")
time.sleep(3)
search_box.send_keys("crowdfunding")
search_button = driver.find_element_by_name("query")
search_box.send_keys(Keys.RETURN)
time.sleep(random.randint(15, 20))

adv=driver.find_element_by_id("switch-to-advanced")
adv.click()
time.sleep(random.randint(15, 20))

start_date=driver.find_element_by_name("start_date")
start_date.click()
start_date.send_keys("01/01/1985")
time.sleep(5)
time.sleep(random.randint(15, 20))

end_date=driver.find_element_by_name("end_date")
end_date.click()

end=time.time()

end_date.send_keys(datetime.datetime.fromtimestamp(end).strftime('%m/%d/%Y '))
time.sleep(random.randint(10, 15))

search_button = driver.find_element_by_id("do-search-advanced")
search_button.send_keys(Keys.RETURN)

time.sleep(random.randint(10, 15))


url = driver.current_url
actual_url=url+"publication_type%3AJournal#"
print(actual_url)
driver.get(actual_url)

time.sleep(random.randint(15, 20))

nbutton1=driver.find_element_by_xpath("//a[@aria-label='dismiss cookie message']")
nbutton1.click()

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