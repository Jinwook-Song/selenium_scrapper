from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# option to be kept open
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=chrome_options
)
driver.get("https://google.com")

search_bar = driver.find_element_by_class_name("gLFyf")
search_bar.send_keys("hello")
search_bar.send_keys(Keys.ENTER)

search_results = driver.find_elements_by_class_name("g")

for search_result in search_results:
    title = search_result.find_element_by_tag_name("h3")
    if title:
        print(title.text)


driver.quit()
