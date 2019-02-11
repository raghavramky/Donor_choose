from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import random
import socket
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.firefox.options import Options


#file_path='/MachintoshHD/Users/shailysaigal/Downloads'

#driver=webdriver.Firefox()

driver=webdriver.Firefox()

#driver = webdriver.Firefox(firefox_options=self.options);
#options.headless = True
#driver=webdriver.Firefox(options=options)
#driver = webdriver.Firefox(executable_path='/MachintoshHD/Users/shailysaigal/Downloads/geckodriver')

driver.get("https://aisel.aisnet.org/do/search")
time.sleep(5)


adv=driver.find_element_by_id("switch-to-advanced")
adv.click()
time.sleep(random.randint(20,30))

nbutton1=driver.find_element_by_xpath("//a[@aria-label='dismiss cookie message']")
nbutton1.click()

select_fr = Select(driver.find_element_by_id("field_1"))
select_fr.select_by_index(1)

select_fr = Select(driver.find_element_by_id("results-format"))
select_fr.select_by_index(1)

search_box = driver.find_element_by_id("value_1")
search_box.send_keys("crowdfunding")
time.sleep(random.randint(10,15))

search_button = driver.find_element_by_id("do-search-advanced")
search_button.click()
time.sleep(random.randint(20,40))

driver.close()