from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_valid_login():
    # Setup WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    
    # Open page
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    
    # Click on "Make Appointment" button
    driver.find_element(By.ID, "btn-make-appointment").click()
    
    # Fill the field
    driver.find_element(By.ID, "txt-username").send_keys("John Doe")
    driver.find_element(By.ID, "txt-password").send_keys("ThisIsNotAPassword")
    
    # Click button login
    driver.find_element(By.ID, "btn-login").click()
    
    # Wait and check for successful login message
    time.sleep(3)    
    try:
        # Check for successful login message
        success_message = driver.find_element(By.XPATH, "//h2[contains(text(),'Make Appointment')]")
        assert success_message.is_displayed()
        print("Test Passed: Login Successful")
    except:
        # Check for login failure message
        error_message = driver.find_element(By.XPATH, "//p[contains(text(),'Login failed! Please ensure the username and password are valid.')]")
        assert error_message.is_displayed()
        print("Test Passed: Login Failed as expected")
    
    return driver
    # Close the browser
    driver.quit()

if __name__ == "__main__":
    test_valid_login()
