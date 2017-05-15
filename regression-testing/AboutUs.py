"""
Test C96855: Click on "About us" at the top of the page. 
The user will be presented with a description on OpenStax as well as a brief bio on each staff member and Strategic advisor.
"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

url = 'https://oscms-qa.openstax.org/'

driver = webdriver.Chrome()
driver.maximize_window() # required to display the header links
driver.execute_script('window.focus()')
driver.get(url)

wait = WebDriverWait(driver, 10)

# look for the link
xpath_about = '//a[@href="/about"]'

link =  wait.until(
                EC.element_to_be_clickable(
                        (By.XPATH, xpath_about)
                )
              )

# simulate a click to get around the overlay issue hiding the click in the header
link.send_keys('\n')

# check if page content loads
try:
    wait.until(
                EC.presence_of_element_located(
                        (By.CSS_SELECTOR, '.about-page')
                )
              )
    print ('PASS: About page content loaded')
except:
    print ('FAIL: page content not loaded')
finally:
    driver.quit()
