from django.http import HttpResponse
from selenium import webdriver
from django.http import HttpResponse
import os
import time


# scraping restaurants
def get_restaurant_name(request):
    driver = webdriver.Chrome(os.environ.get('CHROMEDRIVER_PATH'))
    stations = ['선정릉', '삼성중앙', '선릉']
    for station in stations:
        print("present station: ", station)
        driver.get(f'https://map.naver.com/v5/search/{station}%20음식점')
        driver.implicitly_wait(time_to_wait=3)
        driver.switch_to.frame("searchIframe")
        
        for num in range(1, 51):
            print("present num: ", num)
            try:
                element = driver.find_element_by_xpath(f'//*[@id="_pcmap_list_scroll_container"]/ul/li[{num}]/div[1]/a/div[1]/div/span')
                print("restaurant: ", element.text)
            except:
                driver.execute_script('arguments[0].scrollIntoView({block: "center"})', element)
                time.sleep(3)
        driver.close()
    return HttpResponse(status=200)