
from selenium import webdriver
import time

def test_scores_service(url_test):
    
    my_driver_for_facebook = webdriver.Chrome(
        executable_path="C:\\Users\\admin\Desktop\\chromedriver_win32\\chromedriver")

    my_driver_for_facebook.get(url_test)
    string = my_driver_for_facebook.find_element_by_xpath('//*[@id="score"]').text
    splited_str = string.split(' ')
    time.sleep(10)
    if(int(splited_str[-1]) in range(1, 1000)):
        return True
    else:
        return False


def main_function():
    flag = False
    if(test_scores_service('http://10.0.0.13:5001/') == flag):
        return -1
    else:
        return 0

print(main_function())