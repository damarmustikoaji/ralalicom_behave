from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

class Browser(object):

    BROWSER = "Chrome"

    if BROWSER == "Firefox" :
        options = Options()#firefox
        options.set_preference('dom.webnotifications.enabled', False)
        options.set_preference('geo.enabled', False)
        driver = webdriver.Firefox(options=options, executable_path="../driver/mac/geckodriver")
        driver.maximize_window()
    else:
        options = webdriver.ChromeOptions()
        #block permission webnotif
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        options.add_experimental_option("prefs",prefs)
        driver = webdriver.Chrome(chrome_options=options, executable_path="../driver/mac/chromedriver")
        driver.set_window_size(1280, 800)
    driver.implicitly_wait(15)
    driver.set_page_load_timeout(15)
    #driver.set_window_size(1280, 800)

    def close(context):
        context.driver.close()

    def quit(context):
        context.driver.quit()
