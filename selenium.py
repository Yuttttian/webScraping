from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

driver = webdriver.Chrome(executable_path='/Users/yutian.lei/Downloads/chromedriver')
driver.implicitly_wait(10)
driver.set_script_timeout(120)
driver.set_page_load_timeout(10)

# (1)
driver.get("https://google.com");
inp = driver.find_element_by_css_selector("input[type=text]")
inp.send_keys("askew\n")
driver.save_screenshot('screenshot1.png')
time.sleep(2)

ele = driver.find_element_by_css_selector("input[type=text]")
ele.clear()
ele.send_keys("google in 1998\n")
driver.save_screenshot('screenshot2.png')
time.sleep(2)

# (2)
# click on Deal of the Day, read and print the left time
driver.get("https://www.bestbuy.com/")

# if pop up window
try:
    svg = driver.find_element_by_class_name("c-close-icon-svg");
    svg.click()
    time.sleep(2)
except Exception as ex:
    print('didn\'t pop up Windows')

deal = driver.find_element_by_xpath("//a[text()='Deal of the Day']")
deal.click()

left_time = driver.find_element_by_css_selector("span[data-testid='expiration-message']")
print(left_time.text)
time.sleep(2)

# click on the Deal of the Day (the actual product)
deal2 = driver.find_element_by_css_selector("a.wf-offer-link")
deal2.click()
time.sleep(2)

# click on its reviews and save the resulting HTML
reviews = driver.find_element_by_xpath("//span[text()='Reviews']");
reviews.click()
filePath = os.getcwd()+"/bestbuy_deal_of_the_day.htm"
with open(filePath, "w") as f:
    f.write(driver.page_source)

# time.sleep(2)
driver.quit()
