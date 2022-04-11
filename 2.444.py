from email import message
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import math
browser = webdriver.Chrome('C:/Users/Demo/Downloads/chromedriver_win32_/chromedriver.exe')
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)
option1 = WebDriverWait(browser, 12).until( EC.text_to_be_present_in_element((By.ID, 'price'), "$100")
    )
button = browser.find_element(By.ID, "book")
button.click()
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
x_element = browser.find_element_by_xpath("//*[@id='input_value']")
x = x_element.text
y = calc(x)
Element = browser.find_element_by_id("answer")
Element.send_keys(y)
submit = browser.find_element_by_css_selector("[type='submit']").click()
