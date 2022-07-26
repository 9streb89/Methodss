# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.action_chains import ActionChains
# import time
# from pymongo import MongoClient
# from pprint import pprint
#
# options = Options()
# options.add_argument("start-maximized")
#
# s = Service('./chromedriver')
# driver = webdriver.Chrome(service=s, options=options)
#
# driver.get("https://www.mvideo.ru")
#
#
# articles = driver.find_elements(By.XPATH, '//h2[contains(@class,"title")]')
# actions = ActionChains(driver)
# actions.move_to_element(articles[2])
# actions.perform()
# time.sleep(5)
# button = driver.find_element(By.XPATH, "//button[@class= 'tab-button ng-star-inserted']")
# button.click()
#
# trend = []
#
# elem_in_trend = driver.find_elements(By.XPATH, "//mvid-shelf-group//mvid-product-cards-group//div[@class='title']")
# for elem in elem_in_trend:
#     one_trend = {}
#     name = elem.text
#     link = elem.find_element(By.XPATH, "./a").get_attribute('href')
#
#     one_trend['name'] = name
#     one_trend['link'] = link
#     one_trend['website'] = 'https://www.mvideo.ru'
#
#     trend.append(one_trend)
#
# pprint(trend)
#
# client = MongoClient('127.0.0.1', 27017)
#
# db = client['items_in_trend']
# items_in_trend = db.items_in_trend
#
#
# for item in trend:
#     items_in_trend.insert_one(item)
#
#
# for item in items_in_trend.find({}):
#     pprint(item)
