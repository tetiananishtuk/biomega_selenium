import pytest
from selenium import webdriver
driver = None

# from selenium.webdriver import ActionChains
# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.support import expected_conditions as EC


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope='class')
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path='../drivers/chromedriver')
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path='../drivers/geckodriver')
    driver.get('https://biomega.net/')
    request.cls.driver = driver
    yield
    driver.close()

#@pytest.mark.hookwrapper
#def pytest_runtest_makereport(item): #inserts screenshot into html report when test fails

   # pytest_html = item.config.pluginmanager.getplugin('html')
   # outcome = yield
   # report = outcome.get_report()
   # extra = getattr(report, 'extra', [])


    #if report.when == 'call' or report.when == 'setup':
       # xfail = hasattr(report, 'wasxfail')
        #if (report.skipped and xfail) or (report.failed and not xfail):
           # file_name = report.nodeid.replace('::', '_') + '.png'
           # _capture_screenshot(file_name)
          #  if file_name:
              #  html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                  #     'onclick="window.open(this.src)" align="right"/></div>' % file_name

              #  extra.append(pytest_html.extras.html(html))

              #  report.extra = extra

#def _capture_screenshot(name):
    #driver.get_screenshot_as_file(name)
