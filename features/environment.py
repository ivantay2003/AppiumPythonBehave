from behave import fixture, use_fixture
# from behave4my_project.fixtures import wsgi_server
from appium import webdriver

@fixture
def capabilities (context):

    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['deviceName'] = 'a8dbf256'
    desired_caps['appPackage'] = 'com.google.android.youtube'
    desired_caps['appActivity'] = 'com.google.android.apps.youtube.app.application.Shell$HomeActivity'
    desired_caps['noReset'] = 'true'
    desired_caps['forceMjsonwp'] = 'true'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    context.driver = driver;
    return driver

@fixture
def before_all(context):
    use_fixture(capabilities, context)



