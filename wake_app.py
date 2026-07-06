import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 🔗 REPLACE WITH YOUR ACTUAL STREAMLIT APP URL
URL = "https://your-app-subdomain.streamlit.app" 

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

try:
    print(f"Pinging app at {URL}...")
    driver.get(URL)
    
    # Wait up to 15 seconds to see if the "Wake up" button appears
    wait = WebDriverWait(driver, 15)
    wake_button = wait.until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Yes, get this app back up')]"))
    )
    
    print("🌙 App was found sleeping! Clicking wake up button...")
    wake_button.click()
    print("🚀 Clicked successfully. The app is waking up!")
except Exception:
    print("☀️ App is already awake and operational. Nothing to do!")
finally:
    driver.quit()
