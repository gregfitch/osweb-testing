"""
Test C96702: In reduced screen size, hamburger menu appears
"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

url = 'https://oscms-qa.openstax.org/'

driver = webdriver.Chrome()
driver.execute_script('window.focus()')
driver.set_window_position(720, 0)  # fullscreen:1280|laptop:720
driver.set_window_size(600, 800)  # fullscreen:1280,1360|laptop:720,800
driver.get(url)

wait = WebDriverWait(driver, 10)

try:
    hamburger = wait.until(
                        EC.presence_of_element_located(
                                (By.CSS_SELECTOR, '.expand')
                        )
                      )

    if hamburger.is_displayed():
        print ('PASS: hamburger menu displayed in reduced screen size')
    else:
        print ('FAIL: hamburger menu not displayed')
except:
    print ('FAIL: hamburger menu element not found')

finally:
    driver.quit()
