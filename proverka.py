from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.cart_page import CartPage
from pages.client_information_page_copy import ClientInformationPageCopy
from pages.delivery_address_info import DeliveryAddressPage
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.sub_subcategory import SubSubcategoryPage
from pages.sub_subsubcategory import SubSubSubcategoryPage
from pages.subcategory_page import SubcategoryPage


def miu():

    driver = webdriver.Firefox()
    driver.maximize_window()
    print("Start TEST #1")
    driver.get("https://www.sima-land.ru/10329831/karnavalnyy-kostyum-zloveschaya-koldunya-plate-shlyapa-sumka-chulki-rost-104-110-cm/")
    res = driver.find_element(By.XPATH, "//h1[@data-testid='product-name']").text
    print(res)

miu()

