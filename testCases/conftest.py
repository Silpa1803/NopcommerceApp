import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome(r'C:\Users\silpa\PycharmProjects\chromedriver_win32\chromedriver')
        print("Launching Chrome browser.......")
    elif browser=='firefox':
        driver=webdriver.firefox()
        print("Launching Firefox browser.......")
    else:
        driver = webdriver.Ie()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")  #this will get the value from CLI/hooks

@pytest.fixture()
def browser(request):              #this will return the browser value to setup method
    return request.config.getoption("--browser")

############  Pytest HTML Report ############

#It is the hoop for adding Environment info to HTML Report

def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Silpa'

@pytest.mark.optionalhook

def pytest_metadata(metadata):
    metadata.pop("Python_Home",None)
    metadata.pop("Plugins",None)
