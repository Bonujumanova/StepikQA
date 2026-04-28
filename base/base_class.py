import datetime
from pathlib import Path
import os


class Base:
    def __init__(self, driver):
        self.driver = driver


    def get_current_url(self):
        get_url: str = self.driver.current_url
        print("Current url: " + get_url)

    @staticmethod
    def assert_product_name(cart_product, selected_product) -> bool:
        try:
            assert selected_product == cart_product
            print("Product check - OK")
            return True
        except AssertionError as e:
            print(f"ERROR: {e}")
            return False

    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
        screenshot_name = "screenshot" + now_date + ".png"
        self.driver.save_screenshot(Path(f"/home/bonu/Documents/QA/SiteParser/screen/{screenshot_name}"))
        print("Screenshot is done")

