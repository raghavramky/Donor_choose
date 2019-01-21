from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options

chromeoptions = Options()
driver = webdriver.Chrome(executable_path="C:\\Users\\vivek4\\Downloads\\chromedriver\\chromedriver.exe", chrome_options=chromeoptions) 

#driver = webdriver.Chrome()
driver.get("https://aisel.aisnet.org/do/search")
time.sleep(2)
#x=driver.page_source
search_box = driver.find_element_by_name("q")
time.sleep(3)
search_box.send_keys("crowdfunding")
search_button = driver.find_element_by_name("query")
search_box.send_keys(Keys.RETURN)
time.sleep(2)

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
time.sleep(2)

end_date=driver.find_element_by_name("end_date")
end_date.click()
end_date.send_keys("12/31/2015")
time.sleep(2)

#driver.find_element_by_xpath('//*[@type='radio']')

time.sleep(2)
                             
search_button = driver.find_element_by_id("do-search-advanced")
search_button.send_keys(Keys.RETURN)


header_list=driver.find_element_by_xpath("//span[@class='title']")
header = driver.find_elements_by_xpath("//a[@href]")


'''
time.sleep(3)
for headers in item.find_element_by_class_name('grid_10'):
    header_list=headers.find_element_by_xpath("//span[@class='title']").text
    
    
num_header=len(header)
for span in header:
    print(span.text+ "\n")
'''
    


#driver.close()




