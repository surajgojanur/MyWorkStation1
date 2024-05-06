from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

# Initialize Chrome WebDriver (ensure you have chromedriver installed)
driver = webdriver.Chrome()

# Open the webpage
driver.get('https://www.google.com/maps/place/Coffeeshop+Leipzig.+Bar+italiano/@51.3371422,12.3814044,575m/data=!3m1!1e3!4m10!1m2!2m1!1sCoffee+Shop!3m6!1s0x47a6f83bbd257795:0xf867106e9524d8ec!8m2!3d51.3371422!4d12.3859105!15sCgtDb2ZmZWUgU2hvcFoIIgZjb2ZmZWWSAQRjYWZlmgEkQ2hkRFNVaE5NRzluUzBWSlEwRm5TVU5sY1c4dGVYSkJSUkFC4AEA!16s%2Fg%2F11bwf7mtsd?entry=ttu')

# Wait for the page to fully load (you may need to adjust this timing)
time.sleep(5)  # Adjust as needed

# Iterate through 10 times
for i in range(10):
    # Find all elements with class "hfpxzc"
    elements = driver.find_elements_by_class_name('hfpxzc')
    
    # Iterate through each element and click it
    for element in elements:
        element.click()
        time.sleep(1)  # Wait for the page to update
    
        # Find and collect text from elements with class "Io6YTe fontBodyMedium kR99db"
        try:
            text_elements = driver.find_elements_by_class_name('Io6YTe.fontBodyMedium.kR99db')
            for text_element in text_elements:
                print(text_element.text)
        except NoSuchElementException:
            pass
    
    print(f"Iteration {i+1} completed.")
