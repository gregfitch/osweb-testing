"""
Test C96699
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

css_homepage_quote = '.quotes>div.full'

try:
    hp_quote = wait.until(
                    EC.presence_of_element_located(
                            (By.CSS_SELECTOR, css_homepage_quote)
                    )
                  )

    quote_text = hp_quote.get_attribute('textContent')

    if hp_quote:
        print ('Professor quote shown, PASS')
        print (quote_text)
except:
    print ('Professor quote not found, Fail')
finally:
    driver.quit()
