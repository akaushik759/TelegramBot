from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 

import requests
import random
import time

def scrape_website_events(category):
	if category not in ['hackathons','workshops','internships','scholarships','quizzes','competitions','cultural','festivals']:
		return False

	count = 0
	result = []
	url = 'https://dare2compete.com/e/'+category+'?&filters=engineering students&types=eligible'

	# initiating the webdriver. Parameter includes the path of the webdriver. 
	op = webdriver.ChromeOptions()
	op.add_argument('headless')
	driver = webdriver.Chrome(options=op)

	#driver = webdriver.Chrome('/usr/bin/chromedriver')  
	driver.get(url)  
  
	# this is just to ensure that the page is loaded 
	time.sleep(3)  
  
	html = driver.page_source 
 
	soup = BeautifulSoup(html, 'html.parser')

	for div in soup.findAll("div", {"class": "listing"}):
		opportunity = {}

		#Title
		heading_div = div.find("span", attrs={"class": "ng-star-inserted"})
		opportunity['title'] = heading_div.text

		#Organisation
		org_div = div.find("h3", attrs={"class": ["double-wrap","cursor-pointer","ng-star-inserted"]})
		opportunity['organisation'] = org_div.text

		#Dates
		date_div = div.find("div", attrs={"class": ["date"]})
		opportunity['date'] = date_div.text

		#Link
		link_div = div.find("a", attrs={"class": ["img"]})
		opportunity['link'] = 'https://dare2compete.com'+link_div['href']

		result.append(opportunity)

		count = count+1
		if count>9:
			break
	driver.close()
	return result

def scrape_website_articles(category):

	count = 0
	result = []
	url = 'https://dare2compete.com/e/'+category

	# initiating the webdriver. Parameter includes the path of the webdriver. 
	op = webdriver.ChromeOptions()
	op.add_argument('headless')
	driver = webdriver.Chrome(options=op)
  
	# this is just to ensure that the page is loaded 
	time.sleep(3)  
  
	html = driver.page_source 
 
	soup = BeautifulSoup(html, 'html.parser')

	for div in soup.findAll("a", {"class": "listing"}):

		opportunity = {}

		#Title
		heading_div = div.find("h2")
		opportunity['title'] = heading_div.text

		#Description
		desc_div = div.find("p", attrs={"class": "ng-star-inserted"})
		opportunity['description'] = desc_div.text

		#Link
		opportunity['link'] = 'https://dare2compete.com'+div['href']

		result.append(opportunity)

		count = count+1
		if count>4:
			break

	return result

