# Grzegorz Paszek

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path = ChromeDriverManager().install())
#driver.maximize_window();
driver.implicitly_wait(1)

driver.get("https://demoqa.com/droppable/")

driver.get_screenshot_as_file("captures/before.png")

elementToDrag = driver.find_element_by_xpath("//*[@id='draggable']")
elementToDrop = driver.find_element_by_xpath("//*[@id='droppable']")

ActionChains(driver).drag_and_drop(elementToDrag, elementToDrop).perform()

driver.get_screenshot_as_file("captures/after.png")

driver.quit()
