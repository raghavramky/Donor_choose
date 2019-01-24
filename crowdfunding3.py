from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import random

file_path='/MachintoshHD/Users/shailysaigal/Downloads'
#csv_file=open('links.csv','w')
#writer_main = csv.writer(csv_file)
#writer_main.writerow(['Project Links'])

driver = webdriver.Chrome()
driver.get("https://aisel.aisnet.org/do/search")
time.sleep(5)
#x=driver.page_source
search_box = driver.find_element_by_name("q")
time.sleep(3)
search_box.send_keys("crowdfunding")
search_button = driver.find_element_by_name("query")
search_box.send_keys(Keys.RETURN)
time.sleep(random.randint(15, 20))

adv=driver.find_element_by_id("switch-to-advanced")
adv.click()
time.sleep(random.randint(15, 20))

#search_box = driver.find_element_by_name("value_1")
#search_box.send_keys("crowd funding")
#time.sleep(2)

start_date=driver.find_element_by_name("start_date")
start_date.click()
start_date.send_keys("01/01/2015")
#search_box.send_keys("01/01/2015")
time.sleep(random.randint(15, 20))

end_date=driver.find_element_by_name("end_date")
end_date.click()
end_date.send_keys("12/31/2015")
time.sleep(random.randint(10, 15))

#driver.find_element_by_xpath('//*[@type='radio']')


                             
search_button = driver.find_element_by_id("do-search-advanced")
search_button.send_keys(Keys.RETURN)

time.sleep(random.randint(10, 15))
'''result=driver.find_element_by_id("results-facets")
facet_pub=result.find_element_by_class_name("facet")
time.sleep(2)
journal_class=facet_pub.find_element_by_class_name("facet-publication_type")
journal=journal_class.find_element_by_link_text("Journal")

time.sleep(5)
journal.click()
'''

#result=driver.find_element_by_xpath("//a")
#journal=driver.find_element_by_link_text("Journal")
'''journal_class=driver.find_element_by_class_name("facet-publication_type")
journal=journal_class.find_element_by_link_text("Journal")
time.sleep(10)
journal.click()
'''

url = driver.current_url
actual_url=url+"publication_type%3AJournal#"
print(actual_url)
driver.get(actual_url)

time.sleep(random.randint(15, 20))

#hrefs=[]

header_list=driver.find_element_by_xpath("//div[@id='results-list']")
header_title=header_list.find_elements_by_xpath("//span[@class='title']")
with open('links.csv','a') as f:
    for header in header_title:
        headers= header.find_element_by_tag_name('a')
        x=headers.get_attribute('href')
        #print(x)
        f.write(x+" \n")
        #hrefs.append(header)
    f.close()
    #print(hrefs)
time.sleep(random.randint(10, 20))
    
driver.close()