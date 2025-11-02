from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep, time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

sleep(3)
try:
    language_select = driver.find_element(By.ID, value="langSelect-EN")
    language_select.click()
    sleep(1)
except NoSuchElementException:
    print("Either no language pop up or just straight old no luck")


sleep(1)
clicker_on = True
cookie_button = driver.find_element(By.ID, value="bigCookie")

game_time = time() + 60 * 1
shopping_time = time() + 5

while clicker_on:
    cookie_button.click()

    if time() > shopping_time:
        try:
            cookie_currency = driver.find_element(By.ID, value="cookies")
            cookie_count = int(cookie_currency.text.split()[0].replace(",",""))
            products = driver.find_elements(by=By.CSS_SELECTOR, value="div[id^='product']")

            most_expensive_item = None
            for product in reversed(products):
                if "enabled" in product.get_attribute("class"):
                    most_expensive_item = product
                    break

            if most_expensive_item:
                most_expensive_item.click()
        except (NoSuchElementException, ValueError):
            print("No cookies or items found")

        shopping_time = time() + 5

    if time() > game_time:
        try:
            cookie_per_second = driver.find_element(By.ID, value="cookiesPerSecond")
            print(f"{cookie_per_second.text}")
        except NoSuchElementException:
            print("Your final cookie count is not available at the moment")
        clicker_on = False
        driver.quit()