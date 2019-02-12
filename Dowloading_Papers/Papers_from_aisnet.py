#######################################################
#UTF-8 Encoded
#Created Date - Feb 3rd, 2019
# Author - Raghav Ramky
#Stage_2: Dowloading files from AISNET
#######################################################
from selenium import webdriver
from credentials import *

import pandas as pd
import datetime
import random
import shutil
import time
import csv
import os

def move_downloads(destination_path):
	source = '/home/raghavramky/Downloads/'
	files = os.listdir(source)
	for f in files:
	        shutil.move(source + f, destination_path)

def directory_module(x):

	AIS_opensrc = '/home/raghavramky/Documents/AISNET/Open_Source_Papers'
	AIS_social = '/home/raghavramky/Documents/AISNET/Social_Media_Papers'
	AIS_crowd = '/home/raghavramky/Documents/AISNET/CrowdFunding_Papers'

	if(x == 1):
		if not os.path.exists(AIS_crowd):
			os.makedirs(AIS_crowd)
			return AIS_crowd
	if(x == 2):
		if not os.path.exists(AIS_opensrc):
			os.makedirs(AIS_opensrc)
			return AIS_opensrc
	if(x == 3):
		if not os.path.exists(AIS_social):
			os.makedirs(AIS_social)
			return AIS_social

def AIS_Module(link):
	driver.get(link)
	time.sleep(random.randint(5, 10))
	downloadpdf_button = driver.find_element_by_id('pdf')
	downloadpdf_button.click()

if __name__ == '__main__':
	#Calculating the start time of the code
	start = time.time()

	informs_links = []
	ais_links = []

	# detect the current working directory and print it
	#path = os.getcwd()

	#Loading the consolidated CSV From the below path into a Pandas Data Frame
	#https://drive.google.com/drive/u/1/folders/16c9uS0XyN4QjZv6ooH9Ohb3T6I6xdZGm
	df = pd.read_csv("/home/raghavramky/Documents/Paper_Links.csv")	

	#Loading Chrome Driver in Selenium
	chromeOptions = webdriver.ChromeOptions()

	# To Disable the Automatic PDF Viewer in Chrome and override it to download the pdf directly
	prefs = {"plugins.always_open_pdf_externally": True}
	chromeOptions.add_experimental_option("prefs",prefs)
	driver = webdriver.Chrome(chrome_options = chromeOptions)

	#Loading the AISNET Page and Logging in
	driver.get(AISNET_Login_Page)
	email = driver.find_element_by_id('id_username')
	email.click()
	email.send_keys(USR_NM)
	pwd = driver.find_element_by_id('id_password')
	pwd.click()
	pwd.send_keys(PWD)

	login_button = driver.find_element_by_xpath("//button[@class='btn btn-primary']")
	login_button.click()
	time.sleep(random.randint(2, 5))

	"""
	for crowd_link in df["PUBS_CROWD"]:
	for opensrc_link in df["PUB_OPENSRC"]:
	for social_link in df["PUBS_SOCIAL"]:
	"""
	path = directory_module(1)
	for crowd_link in df["AIS_CROWDFUNDING"]:
		try: 
			AIS_Module(crowd_link)
			move_downloads(path)
		except:
			pass
	
	path = directory_module(2)
	for opensrc_link in df["AIS_OPENSRC"]:
		try:
			AIS_Module(opensrc_link)
			move_downloads(path)
		except:
			pass

	path = directory_module(3)
	for social_link in df["AIS_SOCIAL"]:
		try: 
			AIS_Module(social_link)
			move_downloads(path)
		except:
			pass

	#Log Module {Can be Detached anytime}
	end = time.time()
	program = (end - start)
	start_time = datetime.datetime.fromtimestamp(start).strftime('%Y-%m-%d %H:%M:%S')
	end_time = datetime.datetime.fromtimestamp(end).strftime('%Y-%m-%d %H:%M:%S')

	csv_ais = open('Aisnet_LogFile.csv', 'a')
	writer_ais = csv.writer(csv_ais)
	writer_ais.writerow([start_time, end_time, program])