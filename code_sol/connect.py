'''
from selenium import webdriver
driver=webdriver.Chrome()                      
#wait = WebDriverWait(driver, 720) 
driver.get('http://selenium-python.readthedocs.io/getting-started.html')
driver.close()
#testing introduction page
'''
#from pyvirtualdisplay import Display
from selenium import webdriver

#display = Display(visible=0, size=(800, 600))
#display.start()
driver = webdriver.Chrome('/home/shivam/Downloads/chromedriver')
driver.get('http://selenium-python.readthedocs.io/getting-started.html')