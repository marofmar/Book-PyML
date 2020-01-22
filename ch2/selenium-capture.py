# from selenium.webdriver import Firefox, FirefoxOptions

# url = "http://www.naver.com/"

# options = FirefoxOptions()
# options.add_argument('-headless') 

# browser = Firefox(options = options) 

# browser.get(url) 
 
# browser.save_screenshot("Website.png")
# browser.quit()

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome(chrome_options=options)

driver.get('https://python.org')
driver.save_screenshot("screenshot.png")

driver.close()