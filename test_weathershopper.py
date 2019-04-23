"""
SCOPE:
1) Launch Firefox driver
2) Navigate to weathershopper
3) Add items to cart
4) click cart button

"""

import time
from selenium import webdriver

# Create an instance of Firefox WebDriver
driver = webdriver.Firefox()
# Maximize the browser window
driver.maximize_window()
# Navigate to weathershopper page       
driver.get("http://weathershopper.pythonanywhere.com/moisturizer")
# Find the element containing in page
text_aloe = driver.find_element_by_xpath("//div[contains(@class,'text-center col-4')]")

price_aloe = table.find_elements_by_xpath("//p[contains(text(),'Price')]")
