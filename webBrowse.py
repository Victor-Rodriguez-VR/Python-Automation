from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
messageField.send_keys('Doing your mom')
showMessageButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')
showMessageButton.click()

aField = driver.find_element_by_xpath('//*[@id="sum1"]')
bField = driver.find_element_by_xpath('//*[@id="sum2"]')
sumField = driver.find_element_by_xpath('//*[@id="gettotal"]/button')
aField.send_keys('50')
bField.send_keys('60')
sumField.click()