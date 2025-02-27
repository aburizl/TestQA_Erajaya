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

# Appium Configuration Using Real Device
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
    
    # Input correct email & password
    find_and_send_keys(driver, "//android.widget.EditText[@resource-id='com.eraspace.app.membership:id/edtPhoneOrEmail']", "afipes6551@gmail.com")
    find_and_send_keys(driver, "//android.widget.EditText[@resource-id='com.eraspace.app.membership:id/edtPassword']", "@123Qwer")
    
    # Click the Login button
    find_and_click(driver, "//android.widget.Button[@resource-id='com.eraspace.app.membership:id/btnLogin']")
    
    find_and_click(driver, "//android.widget.ImageView[@resource-id='com.eraspace.app:id/btnClose']")
    time.sleep(2)
    find_and_click(driver, "//android.widget.FrameLayout[@content-desc='Akun']")
    time.sleep(2)
    # Check some elements after login
    success_messages = []

    # Check if the user name appears
    try:
        username_xpath = "//android.widget.TextView[@resource-id='com.eraspace.app:id/tvName']"
        username_text = driver.find_element(AppiumBy.XPATH, username_xpath).text
        success_messages.append(f"Nama pengguna terdeteksi: {username_text}")
    except:
        print("Nama pengguna tidak ditemukan.")

    # Check if the logout button is available
    try:
        point_xpath = "//android.widget.TextView[@resource-id='com.eraspace.app:id/tvMyPoint']"
        point_text = driver.find_element(AppiumBy.XPATH, point_xpath).text
        success_messages.append(f"Poin Berhasil Ditampilkan : {point_text}")
    except:
        print("Point tidak ditemukan.")

    # Show results
    if success_messages:
        print("LOGIN SUCCESS")
        for msg in success_messages:
            print(msg)
    else:
        print("Login gagal, tidak ada elemen sukses yang ditemukan.")

finally:
    driver.quit()
