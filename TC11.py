from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def testgagal():
    # Setup WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    
    # Open page
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    
    driver.find_element(By.ID, "btn-make-appointment").click()
    # Fill the field
    driver.find_element(By.XPATH, "//input[@id='txt-username']").send_keys("Test") 
    driver.find_element(By.XPATH, "//input[@id='txt-password']").send_keys("Test123")
    
    
    # Click Button Login
    driver.find_element(By.ID, "btn-login").click()
    
    # Wait and check for failed login error message
    time.sleep(3)
    success_message = driver.find_element(By.XPATH, "//p[contains(text(),'Login failed! Please ensure the username and password are valid.')]" ) 
    assert success_message.is_displayed(), "Login Gagal!"
    
    print("Test Passed: Login Gagal")
    
    # Close the browser
    driver.quit()

if __name__ == "__main__":
    testgagal()
