"""
Test C96700: Clicking on Let Us Know takes them to the renewal form
"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

url = 'https://oscms-qa.openstax.org/'

driver = webdriver.Chrome()
driver.execute_script('window.focus()')
driver.set_window_position(720, 0)  # fullscreen:1280|laptop:720
driver.set_window_size(720, 800)  # fullscreen:1280,1360|laptop:720,800
driver.get(url)

wait = WebDriverWait(driver, 10)

renewal_form_button = wait.until(
                EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, '.full>.quote>a')
                )
              )

renewal_form_button.send_keys('\n')

print (driver.current_url)

# check for the last form element to make sure page content loaded
try:
    feedback_form = wait.until(
                        EC.presence_of_element_located(
                                (By.TAG_NAME, 'textarea')
                        )
                      )
    if feedback_form:
        print('PASS: Feedback form found on Renewal form')
except:
    print('FAIL: Feedback form not found')
finally:
    driver.quit()
