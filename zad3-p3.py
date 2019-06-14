# Grzegorz Paszek

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from random import randint

driver = webdriver.Chrome(executable_path = ChromeDriverManager().install())
#driver.maximize_window();
driver.implicitly_wait(1)

driver.get("https://demoqa.com/checkboxradio/")

driver.get_screenshot_as_file("captures/before.png")

radioCityRandom = str(randint(1, 3))

radioCityToClick = driver.find_element_by_xpath("//*[@id='content']/div[2]/div/fieldset[1]/label[" + radioCityRandom + "]")
radioCityToClick.click()

for i in range(1, 5):
    j = str(i)
    radioStarToClick = driver.find_element_by_xpath("//*[@id='content']/div[2]/div/fieldset[2]/label[" + j + "]")
    radioStarToClick.click()

bedTypeFieldset = driver.find_elements_by_xpath("//*[@id='content']/div[2]/div/fieldset[3]/label")

for bedType in bedTypeFieldset:
    bedType.click()

driver.get_screenshot_as_file("captures/after.png")
driver.quit()
