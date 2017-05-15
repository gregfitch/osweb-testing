"""
Test C96861: Click license link in footer.
"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common import action_chains
import sys

url = 'https://oscms-qa.openstax.org/'

driver = webdriver.Chrome()
driver.set_window_position(720, 0)  # fullscreen:1280|laptop:720
driver.set_window_size(720, 800)  # fullscreen:1280,1360|laptop:720,800
driver.execute_script('window.focus()')
driver.get(url)

wait = WebDriverWait(driver, 10)

xpath_license = '//a[@href="/license"]'

# try clicking the link
try:
    link =  wait.until(
                EC.element_to_be_clickable(
                        (By.XPATH, xpath_license)
                )
              )

    link.click()
except:
    print ('FAIL, License link not found')
    driver.quit()
    sys.exit()

# check if license page content loads
try:
    loaded = wait.until(
                EC.presence_of_element_located(
                        (By.CLASS_NAME, 'loaded')
                )
              )
    print ('PASS: License page content loaded')
except:
    print ('FAIL: License page content not loaded')
finally:
    driver.quit()
