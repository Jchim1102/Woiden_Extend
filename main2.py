options = uc.ChromeOptions()
# 浏览器不提供可视化界面
# options.add_argument('--headless')
# 隐私模式启动
options.add_argument('--incognito')
# options.add_argument('--disable-infobars')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-gpu')
# options.add_argument('--disable-dev-shm-usage')

# driver = webdriver.Chrome(executable_path=diffPlatformDriverPath(), options=Options)
driver_chrome = uc.Chrome(version_main=105,options=options)
# driver = uc.Chrome()
delay()
# go to website which have recaptcha protection
driver_chrome.get(urlLogin)
