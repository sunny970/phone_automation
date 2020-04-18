import base64
from time import sleep
from appium import webdriver

# 初始化连接手机应用
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
# desired_caps['platformVersion'] = '8.1'
desired_caps['deviceName'] = '192.168.208.101:5555'
# desired_caps['deviceName'] = '10.4.226.163:5555'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
# 创建手机对象
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
# # 打印当前包名
# print(driver.current_package)
# # 打印当前
# print(driver.current_activity)
# sleep(3)
# driver.close_app()
# print(driver.current_package)
# driver.start_activity('com.android.messaging','.ui.conversationlist.ConversationListActivity')
# driver.close_app()
# # 安装应用
# driver.install_app('C:\\Users\\15154\\Desktop\\CloudMusic_official_7.1.10.1585132106.apk')
# # 卸载应用
# driver.remove_app("com.netease.cloudmusic")
# print(driver.is_app_installed('com.netease.cloudmusic'))
# driver.install_app('C:\\Users\\15154\\Desktop\\CloudMusic_official_7.1.10.1585132106.apk')
# # 判断应用是否安装
# Is = driver.is_app_installed('com.netease.cloudmusic')
# print(Is)
# 发送编辑文件文件保存到手机
# data = str(base64.b64encode('123abc'.encode('utf-8')),'utf-8')
# driver.push_file('/sdcard/13.txt',data)
# 读取手机文件的内容
# data = driver.pull_file('/sdcard/13.txt')
# print(str(base64.b64decode(data)),'utf-8')
# 获取屏幕所有元素
# print(driver.page_source)
# 设置程序进入后台时间
# driver.background_app(10)

driver.quit()
