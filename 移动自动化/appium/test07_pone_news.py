from appium import webdriver
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = '192.168.208.101:5555'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)


print(driver.device_time)
print(driver.battery_info)
print(driver.get_window_size())
print(driver.get_window_size()["width"])
print(driver.get_window_size()["height"])

driver.start_activity('com.android.settings','.Settings')
driver.find_element_by_xpath("//*[contains(@text,'应用')]").click()
while True:
    try:
        driver.find_element_by_xpath("//*[contains(@text,'Launcher3')]").click()
        break
    except Exception:
        window_width = driver.get_window_size()["width"]
        window_height = driver.get_window_size()["height"]
        start_x = window_width * 0.5
        end_x = start_x
        end_y = window_height * 0.25
        start_y = end_y * 3
        driver.swipe(start_x,start_y,end_x,end_y,5000)

# driver.close_app()
# driver.quit()
















