import pytest
from selenium import webdriver

from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.edge.options import Options as edge_options
from selenium.webdriver.edge.service import Service


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')
    options.add_argument('--headless')
    #options.add_argument('--start-maximized')
    #options.add_argument('--window-size=1920,1080')
    options.add_argument('--ignore-certificate-errors-spki-list')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    return options


@pytest.fixture
def get_edge_options():
    options = edge_options()
    options.add_argument('edge')
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--ignore-certificate-errors-spki-list')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    return options


@pytest.fixture
def get_webdriver(get_chrome_options, get_edge_options, browser):
    browser = browser
    if browser == 'chrome':
        options = get_chrome_options
        #s = Service("E:\\current\\selenium\\pythonProject\\chromedriver.exe")
        #driver = webdriver.Chrome(service=s, options=options)
        driver = webdriver.Remote('http://127.0.0.1:4444/wd/hub', options=options)
    elif browser == 'edge':
        options = get_edge_options
        s = Service("E:\\current\\selenium\\pythonProject\\msedgedriver.exe")
        driver = webdriver.Edge(service=s, options=options)
    else:
        options = get_chrome_options
        s = Service("E:\\current\\selenium\\pythonProject\\chromedriver.exe")
        driver = webdriver.Chrome(service=s, options=options)
    return driver


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://www.yandex.ru/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.quit()


def get_test_case_docstring(item):
    """ This function gets doc string from test case and format it
        to show this docstring instead of the test case name in reports.
    """

    full_name = ''

    if item._obj.__doc__:
        # Remove extra whitespaces from the doc string:
        name = str(item._obj.__doc__.split('.')[0]).strip()
        full_name = ' '.join(name.split())

        # Generate the list of parameters for parametrized test cases:
        if hasattr(item, 'callspec'):
            params = item.callspec.params

            res_keys = sorted([k for k in params])
            # Create List based on Dict:
            res = ['{0}_"{1}"'.format(k, params[k]) for k in res_keys]
            # Add dict with all parameters to the name of test case:
            full_name += ' Parameters ' + str(', '.join(res))
            full_name = full_name.replace(':', '')

    return full_name


def pytest_itemcollected(item):
    """ This function modifies names of test cases "on the fly"
        during the execution of test cases.
    """

    if item._obj.__doc__:
        item._nodeid = get_test_case_docstring(item)


def pytest_collection_finish(session):
    """ This function modified names of test cases "on the fly"
        when we are using --collect-only parameter for pytest
        (to get the full list of all existing test cases).
    """

    if session.config.option.collectonly is True:
        for item in session.items:
            # If test case has a doc string we need to modify it's name to
            # it's doc string to show human-readable reports and to
            # automatically import test cases to test management system.
            if item._obj.__doc__:
                full_name = get_test_case_docstring(item)
                print(full_name)

        pytest.exit('Done!')