from selenium import webdriver
from django.http import HttpRequest, JsonResponse
import os
import time


# scraping restaurants
def get_restaurant_name(request: HttpRequest):
    driver = webdriver.Chrome(os.environ.get('CHROMEDRIVER_PATH'))
    near_stations = ['선정릉', '삼성중앙', '선릉']
    content = {}
    
    for near_station in near_stations:
        driver.get(f'https://map.naver.com/v5/search/{near_station}%20음식점')
        driver.implicitly_wait(time_to_wait=3)
        driver.switch_to.frame("searchIframe")
        searches = []
        
        for num in range(1, 101):
            try:
                element = driver.find_element_by_xpath(f'//*[@id="_pcmap_list_scroll_container"]/ul/li[{num}]/div[1]/a/div[1]/div/span')
                name = element.text
                searches.append(name)
                is_exist = True
            except:
                driver.execute_script('arguments[0].scrollIntoView({block: "center"})', element)
                time.sleep(3)
                if not is_exist:
                    break
                is_exist = False
        
        content[near_station] = searches
    
    driver.close()
    return JsonResponse(content, status=200)
