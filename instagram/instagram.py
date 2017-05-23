from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep


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

	def parse_posts(self):
		posts = self.make_request()
		posts_parse = posts.page_source
		soup_object = BeautifulSoup(posts_parse)
                link_posts = [x['src'] for x in soup_object.findAll('img')]
                return link_posts

instagram_scrapper = InstagramScraper("priyankachopra")
print(instagram_scrapper.parse_posts())

	
	

