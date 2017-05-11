"""
Test C96704, with API update.
"""

from pprint import pprint
from testrail import *
import os
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Testrail API credentials
client = APIClient('https://openstax.testrail.net')
client.user = os.environ['TESTRAIL_USER']
client.password = os.environ['TESTRAIL_KEY']

url = 'https://oscms-qa.openstax.org/'

driver = webdriver.Chrome()
driver.execute_script('window.focus()')
driver.set_window_position(720, 0)  # fullscreen:1280|laptop:720
driver.set_window_size(720, 800)  # fullscreen:1280,1360|laptop:720,800
driver.get(url)

wait = WebDriverWait(driver, 10)

# look for Explore All Subjects button
try:
    eas_button = wait.until(
        EC.element_to_be_clickable(
            (By.CLASS_NAME, 'explore-all')
        )
    )

    eas_button.click()
except:
    print ('Explore All Subjects button not clickable')
    driver.quit()
    raise SystemExit

# xpath for AP microecon book cover == functional test of all content loading on the page
xpath_apmicro = "//div/div[3]/div[1]/div/div[5]/div/div[3]/h3/img"

# look for the AP Microecon book cover
try:
    apmicro = wait.until(
                    EC.presence_of_element_located(
                            (By.XPATH, xpath_apmicro)
                    )
                  )

    if apmicro:
        print (driver.current_url + ': PASS, found cover img for Principles of AP Microeconomics')
        client.send_post(
            'add_result/130344',
            {'status_id':1, 'comment': 'Passed (Testrail)'}
        )
        results = client.send_get('get_results/130344&limit=1')
        pprint (results)
except:
    print (driver.current_url + ': Fail, cover img for Principles of AP Microeconomics not found')
finally:
    driver.quit()
