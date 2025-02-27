from selenium.webdriver.common.by import By
import time
from TC12 import test_valid_login  # Import login function from login.py

def test_negative_appointment():
    driver = test_valid_login()  # Call the login function from login.py
    
    try:
        # Check for successful login message
        success_message = driver.find_element(By.XPATH, "//h2[contains(text(),'Make Appointment')]")
        assert success_message.is_displayed()
        print("Test Passed: Login Successful")
        
        # Clear the date input field
        date_input = driver.find_element(By.ID, "txt_visit_date")
        date_input.clear()
        
        # Negative Test Case: Try submitting an appointment without selecting a date
        driver.find_element(By.ID, "btn-book-appointment").click()
        
        time.sleep(2)
        
        # Check if error message appears in page source
        if "Please fill the fields." in driver.page_source:
            print("Test Passed: Negative Case - Appointment Failed Without Date Selection")
        else:
            print("Test Failed: Error message not found for missing date selection")
        
    except:
        print("Test Failed: Unable to reach appointment page")
    
    # Close the browser
    driver.quit()

if __name__ == "__main__":
    test_negative_appointment()
