#######################################################
#UTF-8 Encoded
#Created Date - Feb 3rd, 2019
# Author - Raghav Ramky
#Stage_2: Dowloading files from AISNET
#######################################################
from selenium import webdriver
import datetime
import random
import time
import csv

#Calculating the start time of the code
start = time.time()

informs_links = []
ais_links = []

#To Read from our CSV File
with open('Book1.csv') as csv_file:
	csv_reader= csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			line_count += 1
		else:
			ais_links.append(row[0])
			informs_links.append(row[1])
			line_count += 1

#Loading Chrome Driver in Selenium
driver = webdriver.Chrome()

#Aisnet Page
for instance, link in enumerate(ais_links):
	driver.get(link)
	time.sleep(random.randint(5, 10))
	downloadpdf_button = driver.find_element_by_id('pdf')
	downloadpdf_button.click()

#informs Page
for instance, links in enumerate(informs_links):
	driver.get(links)
	time.sleep(random.randint(5, 10))
	downloadpdf_button = driver.find_element_by_xpath("//div[@class='btn']")
	downloadpdf_button.click()

#Log Module {Can be Detached anytime}
end = time.time()
program = (end - start)
start_time = datetime.datetime.fromtimestamp(start).strftime('%Y-%m-%d %H:%M:%S')
end_time = datetime.datetime.fromtimestamp(end).strftime('%Y-%m-%d %H:%M:%S')

csv_ais = open('Aisnet_LogFile.csv', 'a')
writer_ais = csv.writer(csv_ais)
writer_ais.writerow([start_time, end_time, program])
