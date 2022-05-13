from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

KEWWORD = "python"


# option to be kept open
chrome_options = Options()
chrome_options.add_experimental_option("detach", False)

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=chrome_options
)
driver.get("https://google.com")

# Web Element API
search_bar = driver.find_element_by_class_name("gLFyf")
search_bar.send_keys(KEWWORD)
search_bar.send_keys(Keys.ENTER)

# Wait for Chrome
ad_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "tvcap"))
)

# Search Results
search_results = driver.find_elements_by_class_name("g")

for idx, search_result in enumerate(search_results):
    search_result.screenshot(f"screenshots/{KEWWORD}_{idx}.png")
