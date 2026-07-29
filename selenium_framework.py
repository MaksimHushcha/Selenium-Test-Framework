from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('window-size=1920x1080')
# options.add_argument('headless') - to run without ui
options.add_experimental_option("detach", True) # to prevent browser from closing
driver = webdriver.Chrome(options=options)
driver.set_window_size(1920, 1080)
driver.get("https://testpages.eviltester.com/")
assert driver.current_url == "https://testpages.eviltester.com/"
assert driver.title == "Software Testing Practice Pages, Apps, and Challenges"

driver.get("https://testpages.eviltester.com/pages/input-elements/text-inputs/")
assert driver.current_url == "https://testpages.eviltester.com/pages/input-elements/text-inputs/"
assert driver.title == "Text Input Elements - Events Display Test Page | Test Pages"