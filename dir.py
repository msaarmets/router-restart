from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import sys, credentials
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By
from time import sleep

class DirRestart():
    def __init__(self):
        pass

    result = ""

    def restart(self, app):
        self.app = app
        user = credentials.dirUser
        password = credentials.password
        url = credentials.dirUrl

        # Hide Chrome browser window while running the code
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('disable-gpu')

        try:
            # Start Chrome browser
            driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
            driver.get(url)
            assert "DIR-620" in driver.title

            # Enter username
            form_username = driver.find_element_by_id("A1")
            form_username.clear()
            form_username.send_keys(user)

            # Enter password
            form_pw = driver.find_element_by_id("A2")
            form_pw.clear()
            form_pw.send_keys(password)

            # Submit form
            submit = driver.find_element_by_id("enter")
            submit.click()

            # Open system configuration menu
            driver.get(url+'/#system/sysconf')

            # Click "Reboot" button and confirm reboot
            try:
                element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Reboot')]")))
                element.click()
                driver.switch_to_alert().accept()
                DirRestart.result = "DIR-620 successfully restarted"
            finally:
                sleep(2)
                driver.quit()
                self.sendError(self)

        except WebDriverException:
            self.result = "Error: ", WebDriverException
            self.sendError(self)
            raise
        except:
            print("Unexpected error:", sys.exc_info()[0])
            self.result = "Unexpected error:", sys.exc_info()[0]
            self.sendError(self)
            raise

    def sendError(self):
        self.app.updateInformationField(self.result)