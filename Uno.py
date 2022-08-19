from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time




def get_pars_table():
    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(chrome_options=options, executable_path=r'/home/gl/Parser/chromedriver')
    driver.get('https://www.sberbank.ru/ru/quotes/currencies')
    time.sleep(12)
    prs_element = driver.find_elements("xpath", "//*[@id='page-main']/div[2]/div[3]/div[1]/div/div[2]/div/div/div/div[1]/div/div/div[3]/table/tbody")
    print(prs_element[0].text)





if __name__ == "__main__":
    get_pars_table()


