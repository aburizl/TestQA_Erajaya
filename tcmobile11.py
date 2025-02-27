from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

# Functions to find an element and click on it
def find_and_click(driver, xpath, wait_time=3):
    element = driver.find_element(AppiumBy.XPATH, xpath)
    element.click()
    time.sleep(wait_time)

# Function to fill text in the input field
def find_and_send_keys(driver, xpath, text, wait_time=1):
    field = driver.find_element(AppiumBy.XPATH, xpath)
    field.send_keys(text)
    time.sleep(wait_time)

# Appium Configuration using Real Device
options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "VO6S5DQWSCHALF5D"
options.app_package = "com.eraspace.app"
options.app_activity = "com.eraspace.home.presentation.HomeActivity"
options.no_reset = True

# Connect to Appium Server
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

try:
    driver.implicitly_wait(10)
    
    # Click the Login button
    find_and_click(driver, "//android.widget.Button[@resource-id='com.eraspace.app.home:id/btnLogin']")
    
    # Incorrect email & password input
    find_and_send_keys(driver, "//android.widget.EditText[@resource-id='com.eraspace.app.membership:id/edtPhoneOrEmail']", "afipes6551@gmail.com")
    find_and_send_keys(driver, "//android.widget.EditText[@resource-id='com.eraspace.app.membership:id/edtPassword']", "@123Qwzr")
    
    # Click the Login button
    find_and_click(driver, "//android.widget.Button[@resource-id='com.eraspace.app.membership:id/btnLogin']")
    
    # Capture error message
    error_xpath = "//android.widget.TextView[@resource-id='com.eraspace.app.membership:id/tvError']"
    error_message = driver.find_element(AppiumBy.XPATH, error_xpath).text
    
    print(f"Pesan error yang muncul: {error_message}")
    print("Test case negatif PASSED: Pesan error berhasil ditampilkan.")
    
except Exception as e:
    print(f"Test case gagal dengan error: {e}")

finally:
    driver.quit()
