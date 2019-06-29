from selenium import webdriver
browser=webdriver.Firefox()
type(browser)
browser.get('http://inventwithpython.com') 
browser.close()
