from selenium import webdriver
import os
import time


# scraping restaurants
def get_restaurant_main_info():
    driver = webdriver.Chrome(os.environ.get('CHROMEDRIVER_PATH'))
    near_stations = ['선정릉역', '삼성중앙역', '선릉역']
    main_categories = ['한식', '일식', '중식', '양식']
    
    content = []
    for near_station in near_stations:
        for main_category in main_categories:
            driver.get(f'https://map.naver.com/v5/search/{near_station}%20{main_category}')
            driver.implicitly_wait(time_to_wait=5)
            driver.switch_to.frame("searchIframe")
            
            for num in range(3, 103):
                print(near_station, main_category, num)
                context = {
                    'near_station': None,
                    'main_category': None,
                    'name': None
                }
                try:
                    if near_station == '선릉역' and main_category != '양식':
                        element = driver.find_element_by_xpath(f'//*[@id="_pcmap_list_scroll_container"]/ul/li[{num}]/div[1]/a/div[1]/div/span')
                    else:
                        element = driver.find_element_by_xpath(f'//*[@id="_pcmap_list_scroll_container"]/ul/li[{num}]/div[2]/a[1]/div/div/span[1]')
                    name = element.text
                    context['near_station'] = near_station
                    context['main_category'] = main_category
                    context['name'] = name
                    is_exist = True
                except:
                    driver.execute_script('arguments[0].scrollIntoView({block: "center"})', element)
                    time.sleep(5)
                    if not is_exist:
                        break
                    is_exist = False
                content.append(context)
            time.sleep(3)
        time.sleep(3)
    driver.close()
    return content
