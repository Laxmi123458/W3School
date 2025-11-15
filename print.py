from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

opts = Options()
opts.add_argument("--start-maximized")
# use a chromedriver in PATH
driver = webdriver.Chrome(options=opts)
driver.get("https://online.fliphtml5.com/mkzfx/phnn/#p=1")

time.sleep(5)  # allow viewer to initialize

# example: try to find a download button (class/id varies)
try:
    btn = driver.find_element(By.XPATH, "//button[contains(., 'Download') or @title='Download']")
    btn.click()
    print("Clicked download button — check browser download folder.")
except Exception as e:
    print("No obvious download button found:", e)

# optionally take a screenshot for manual inspection
driver.save_screenshot("viewer_screenshot.png")
driver.quit()
