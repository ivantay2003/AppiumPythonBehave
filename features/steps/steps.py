from behave import *
from LOCELEMENT import LOCELEMENT
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

LOCELEMENT = LOCELEMENT()



@given('I am in Youtube home page')
def step_impl(context):

    #Check if navigation bar exist
    if isPresent (context, MobileBy.ACCESSIBILITY_ID, LOCELEMENT.LOC_NAV_LIBRARY_ACC) is not None:
        pass
    elif False:
        assert False



@when ('I want to search for "{text}"')
def step_impl(context, text):

    context.driver.find_element_by_accessibility_id(LOCELEMENT.LOC_NAV_SEARCH_ACC).click()

    if isPresent(context, By.ID, LOCELEMENT.LOC_SEARCH_INPUT_ID) is not None:
        context.driver.find_element_by_id(LOCELEMENT.LOC_SEARCH_INPUT_ID).send_keys(text + "\n")
        context.driver.press_keycode(66)
    elif False:
        assert False


@when ("Select the second search video")
def step_impl(context):
    #click on 2nd video
    xpath1 = "//android.support.v7.widget.RecyclerView[@resource-id='com.google.android.youtube:id/results']/android.view.ViewGroup"

    if isPresent (context, By.XPATH, xpath1) is not None:
        elements = context.driver.find_elements_by_xpath(xpath1)
        elements[3].click()
    elif False:
        assert False



@then ("The selected video will play on")
def step_impl(context):


    if isPresent (context, MobileBy.ACCESSIBILITY_ID, LOCELEMENT.LOC_VIDEO_PLAYER_ACC) is not None:
        context.driver.save_screenshot("result/screenshot.png")
    elif False:
        assert False


def isPresent (context, by, elementid):

    try:
        elements = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((by, elementid))
        )

        return elements

    except TimeoutException:
        print("Time out. Cannot find element ")
        context.driver.quit()
        return False


