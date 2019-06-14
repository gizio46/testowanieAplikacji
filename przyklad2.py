# Grzegorz Paszek

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path = ChromeDriverManager().install())
#driver.maximize_window();
driver.implicitly_wait(1)

driver.get("https://demoqa.com/tooltip-and-double-click/")

driver.get_screenshot_as_file("captures/before.png")

elementToClick = driver.find_element_by_xpath("//*[@id='doubleClickBtn']")

ActionChains(driver).double_click(elementToClick).perform()

driver.implicitly_wait(3)

alert = driver.switch_to.alert
alertStr = alert.text
alert.accept()

if "You are seeing this message" in alertStr:
    print('OK')
    driver.get("https://google.com")
    driver.get_screenshot_as_file("captures/after.png")
    driver.quit()
else:
    print('Error')
    driver.quit()

