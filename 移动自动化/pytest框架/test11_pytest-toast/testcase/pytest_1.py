# coding=utf-8
import sys
import time
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = ({'platformName': 'Android',
                 'platformVersion': '6.0',
                 'deviceName': '192.168.208.101:5555',
                'unicodeKeyboard': True,
                 'resetKeyboard': True,
                 'automationName': 'uiautomator2'})

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


# def find_toast(massage):
#     # print(driver.current_package)
#     # print(driver.current_activity)
#     driver.start_activity('com.amaze.filemanager','.activities.MainActivity')
#
#     driver.press_keycode(4)
#     toast = WebDriverWait(driver,10,0.1).until(lambda x:x.find_element(By.XPATH,"//*[contains(@text,'" + massage + "')]"))
#
#     return toast.text
# print(find_toast("退出"))


# def find_toast(message):
#     driver.start_activity('com.amaze.filemanager', '.activities.MainActivity')
#     # driver.press_keycode(4)
#     try:
#         element = WebDriverWait(driver, 5,1).until(lambda x:x.find_element(By.XPATH,"//*[contains(@text,'" + message + "')]"))
#         if len(element.text) != 0:
#             return "toast存在-->%s" % element.text
#
#     except Exception:
#         now_time = time.strftime('%Y_%m_%d %H-%M-%S')
#         news = sys.exc_info()[1]
#         driver.get_screenshot_as_file("./%s-%s.png" % (now_time,news))
#         print("toast不存在")
#         raise

def find_toast(message,timeout=5.0,poll=0.1):
    message = "//*[contains(@text,'" + message + "')]"
    toast = WebDriverWait(driver, timeout,poll).until(lambda x:x.find_element(By.XPATH,message))
    return toast.text

def is_toast_exist(message,timeout=5.0,poll=0.1):
    try:
        find_toast(message,timeout,poll)
        return True
    except Exception:
        return False



print(find_toast("退出"))
# driver.keyevent(3)
driver.press_keycode(3)