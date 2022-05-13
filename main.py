from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

KEWWORD = "buy domain"


# option to be kept open
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=None
)
driver.get("https://google.com")

search_bar = driver.find_element_by_class_name("gLFyf")
search_bar.send_keys(KEWWORD)
search_bar.send_keys(Keys.ENTER)

search_results = driver.find_elements_by_class_name("g")

for idx, search_result in enumerate(search_results):
    search_result.screenshot(f"screenshots/{KEWWORD}_{idx}.png")


driver.quit()
