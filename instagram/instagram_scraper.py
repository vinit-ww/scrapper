from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from BeautifulSoup import BeautifulSoup
# import time
import traceback


#Driver class to check whether driver is mozilla or firefox
class Instagram:
    url = "https://www.instagram.com/priyankachopra/"

    def __init__(self):
        return self.url

    # This is the factory method
    @staticmethod
    def scrap(self,driver):
        if (driver == "chrome"):
            return "chrome"
        elif (driver == "mozilla"):
            return "mozilla"
        else:
            return None

#Extract with Chrome 
class Chrome(Instagram):
    driver_ = "chrome"

    def __init__(self):
        self.url = Instagram.__init__(self)

    def driver_chrome_check(self):
        return Instagram.scrap(self,self.driver_)

    def scraped_with_chrome(self):
        if self.driver_chrome_check() is None:
            pass
        else:
            try:
                #import pdb;pdb.set_trace()
                options = webdriver.ChromeOptions();
                options.add_argument("--disable-extensions");
                options.add_argument("test-type");
                options.add_argument("--ignore-certificate-errors");
                options.add_argument("no-sandbox");
                driver = webdriver.Chrome(chrome_options=options)
                driver.get(self.url)
                html_source = driver.page_source
                driver.quit()
                return html_source
            except Exception as e:
                traceback.print_exc(e)
        return "The end"

#Extract with mozilla
class Mozilla(Instagram):
    driver_ = "mozilla"

    def __init__(self):
        self.url = Instagram.__init__(self)

    def driver_mozilla_check(self):
        return Instagram.scrap(self,self.driver_)

    def scraped_with_mozilla(self):
        if self.driver_mozilla_check() is None:
            pass
        else:
            try:
                fp=webdriver.FirefoxProfile()
                driver = webdriver.Firefox(fp)
                driver.get(self.url)
                html_source = driver.page_source
                driver.quit()
                return html_source
            except Exception as e:
                traceback.print_exc(e)
        return "The end"
        
#Using Beautiful soup to extract posts
class PostScraped(Mozilla,Chrome):

    def post_scraped(self,driver):
        if Mozilla().driver_mozilla_check() in driver:
            try:
                html_source_mozilla = Mozilla().scraped_with_mozilla()
                soup_mozilla = BeautifulSoup(html_source_mozilla)
                link_mozilla = [x['src'] for x in soup_mozilla.findAll('img')]
                return link_mozilla
            except Exception as e:
                traceback.print_exc(e)
        elif Chrome().driver_chrome_check() in driver:
            try:    
                html_source_chrome = Chrome().scraped_with_chrome()
                soup_chrome = BeautifulSoup(html_source_chrome)
                link_chrome = [x['src'] for x in soup_chrome.findAll('img')]
                return link_chrome
            except Exception as e:
                traceback.print_exc(e)
        return "The end"


#to scrap from chrome just change to "chrome" inside the function of object PostScraped
posts_mozilla = PostScraped().post_scraped("mozilla")
print(posts_mozilla)
