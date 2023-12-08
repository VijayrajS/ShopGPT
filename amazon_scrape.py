from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

def scrape_product_info(web):

    driver_path = './chromedriver'

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    driver.get(web)

    table_content = driver.find_element(By.ID, "productDetails_detailBullets_sections1")
    driver.implicitly_wait(5)

    print(table_content)


    driver.quit()

    return table_content

def scrape_imgs(web):

    driver_path = './chromedriver'

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    driver.get(web)

    img = driver.find_element(By.ID, "imgTagWrapperId")
    driver.implicitly_wait(5)

    print(img)


    driver.quit()

    return img.get_attribute("src")



