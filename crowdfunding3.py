from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

file_path='/MachintoshHD/Users/shailysaigal/Downloads'
#csv_file=open('links.csv','w')
#writer_main = csv.writer(csv_file)
#writer_main.writerow(['Project Links'])

driver = webdriver.Chrome()
driver.get("https://aisel.aisnet.org/do/search")
time.sleep(2)
#x=driver.page_source
search_box = driver.find_element_by_name("q")
time.sleep(3)
search_box.send_keys("crowdfunding")
search_button = driver.find_element_by_name("query")
search_box.send_keys(Keys.RETURN)
time.sleep(1)

adv=driver.find_element_by_id("switch-to-advanced")
adv.click()
time.sleep(2)

#search_box = driver.find_element_by_name("value_1")
#search_box.send_keys("crowd funding")
#time.sleep(2)

start_date=driver.find_element_by_name("start_date")
start_date.click()
start_date.send_keys("01/01/2015")
#search_box.send_keys("01/01/2015")
time.sleep(3)

end_date=driver.find_element_by_name("end_date")
end_date.click()
end_date.send_keys("12/31/2015")
time.sleep(2)

#driver.find_element_by_xpath('//*[@type='radio']')

time.sleep(3)
                             
search_button = driver.find_element_by_id("do-search-advanced")
search_button.send_keys(Keys.RETURN)

result=driver.find_element_by_id("results-facets")
facet_pub=result.find_element_by_class("facet")
journal=facet_pub.find_element_by_link_text("Journal")
time.sleep(5)
journal.click()
time.sleep(15)
#hrefs=[]
count=0
header_list=driver.find_element_by_xpath("//div[@id='results-list']")
header_title=header_list.find_elements_by_xpath("//span[@class='title']")
with open('links.csv','a') as f:
    for header in header_title:
        count+=1
        
        headers= header.find_element_by_tag_name('a')
        x=headers.get_attribute('href')
        
        #print(x)
        f.write(x+" \n")
        #hrefs.append(header)
    print(count)
    f.close()
    #print(hrefs)

    


#driver.close()




