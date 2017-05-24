from selenium import webdriver
from bs4 import BeautifulSoup
import time

class InstagramScraper():
	base_url = "https://www.instagram.com/"
	user_name = None
	
	def __init__(self,username):
		self.user_name = username
	
	def initiate_browser(self):
		self.driver = webdriver.PhantomJS()
	        self.driver.set_window_size(1120, 550)
		return self.driver
		
	def make_request(self):
		link = self.base_url + self.user_name
		driver = self.initiate_browser()
		driver.get(link)
		return driver

	def scroll_page(self):
		driver_obj = self.make_request()
		driver_obj.find_element_by_link_text('Load more').click()
                lastHeight = driver_obj.execute_script("return document.body.scrollHeight")
		while True:
                	driver_obj.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                	time.sleep(1)
                	newHeight = driver_obj.execute_script("return document.body.scrollHeight")
                	if newHeight == lastHeight:
                        	break
                	lastHeight = newHeight
                html_source = driver_obj.page_source
		return html_source
			
		
		
	def parse_posts(self):
		posts_parse = self.scroll_page()
		soup_object = BeautifulSoup(posts_parse)
                link_posts = [x for x in soup_object.findAll('img')]
                return link_posts

instagram_scrapper = InstagramScraper("priyankachopra")
print(instagram_scrapper.parse_posts())

	
	

