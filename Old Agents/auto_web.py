from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def search_amazon(query):
    """
    Automates a search on Amazon.
    """
    driver = webdriver.Chrome()  # Ensure you have ChromeDriver installed
    driver.get("https://www.amazon.com")
    search_box = driver.find_element("id", "twotabsearchtextbox")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)