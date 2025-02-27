from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from TC12 import test_valid_login  # Import login function from login.py

def test_make_appointment():
    driver = test_valid_login()  # Call the login function from login.py
    
    try:
        # Check for successful login message
        success_message = driver.find_element(By.XPATH, "//h2[contains(text(),'Make Appointment')]")
        assert success_message.is_displayed()
        print("Test Passed: Login Successful")
        
        # Select "Facility"
        facility_dropdown = driver.find_element(By.ID, "combo_facility")
        facility_dropdown.send_keys(Keys.ARROW_DOWN)
        facility_dropdown.send_keys(Keys.RETURN)
        
        # Check "Apply for hospital readmission"
        driver.find_element(By.ID, "chk_hospotal_readmission").click()
        
        # Select "Medicare"
        driver.find_element(By.ID, "radio_program_medicare").click()
        
        # Input "Visit Date"
        driver.find_element(By.ID, "txt_visit_date").send_keys("27/02/2025")
        
        # Input "Comment"
        driver.find_element(By.ID, "txt_comment").send_keys("Test QA")
        
        # Click "Book Appointment"
        driver.find_element(By.ID, "btn-book-appointment").click()
        
        time.sleep(2)
        
        # Verify successful booking
        assert "Appointment Confirmation" in driver.page_source
        print("Test Passed: Appointment Successfully Booked")
        
        time.sleep(5)
        
    except Exception as e:
        print(f"Test Failed: {str(e)}")
    
    driver.quit()

if __name__ == "__main__":
    test_make_appointment()
