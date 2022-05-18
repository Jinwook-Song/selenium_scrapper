from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class GoogleKeywordScreenshooter:
    def __init__(
        self,
        keyword,
        screenshot_dir="screenshots",
    ):
        self.keyword = keyword
        self.screenshot_dir = screenshot_dir

        self.chrome_options = Options()
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
        )

    def start(self):
        self.driver.get("https://google.com")

        # Web Element API
        search_bar = self.driver.find_element(by=By.CLASS_NAME, value="gLFyf")
        search_bar.send_keys(self.keyword)
        search_bar.send_keys(Keys.ENTER)

        # Wait for Chrome
        ad_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "tvcap"))
        )

        # Delete AD element
        if ad_element:
            self.driver.execute_script(
                """
                const ad = arguments[0]
                ad.parentElement.removeChild(ad)
                """,
                ad_element,
            )

        # Search Results
        search_results = self.driver.find_elements(by=By.CLASS_NAME, value="g")

        for idx, search_result in enumerate(search_results):
            try:
                search_result.screenshot(
                    f"{self.screenshot_dir}/{self.keyword}_{idx}.png"
                )
            except Exception:
                pass

    def finish(self):
        self.driver.quit()


domain_competitors = GoogleKeywordScreenshooter("buy domain")
python_competitors = GoogleKeywordScreenshooter("python books")
domain_competitors.start()
domain_competitors.finish()
python_competitors.start()
python_competitors.finish()
