from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.options import Options
import sys,credentials

class ThomsonRestart():
    result = ""
    def restart(self, app):
        self.app = app
        user = credentials.thomsonUser
        password = credentials.password
        url = credentials.thomsonUrl

        # Hide Firefox browser window while running the code
        options = Options()
        options.set_headless(headless=True)

        try:
            # Start Firefox browser
            driver = webdriver.Firefox(executable_path=r'c:\py_ruuter\geckodriver.exe', firefox_options=options)
            driver.get(url)
            assert "Thomson Gateway" in driver.title

            # Enter username
            form_username = driver.find_element_by_name("user")
            form_username.clear()
            form_username.send_keys(user)

            # Enter password
            form_pw = driver.find_element_by_id("password")
            form_pw.clear()
            form_pw.send_keys(password)

            # Submit form
            submit = driver.find_element_by_name("ok")
            submit.click()

            # Open "Information" menu
            information = driver.find_element_by_link_text("Information")
            information.click()

            # Click "Restart" link
            restart = driver.find_element_by_link_text("Restart my Thomson Gateway")
            restart.click()

            # Confirm restart
            confirm = driver.find_element_by_xpath("//input[@value='Yes, restart my Thomson Gateway']")
            confirm.click()
            assert "No results found." not in driver.page_source
            driver.close()

            self.result = "Thomson router restarted"
            self.sendError(self)
        except WebDriverException:
            ThomsonRestart.result = "Error: ", WebDriverException
            self.sendError(self)
            raise
        except:
            print("Unexpected error:", sys.exc_info()[0])
            ThomsonRestart.result = "Unexpected error:", sys.exc_info()[0]
            self.sendError(self)
            raise


    def sendError(self):
        self.app.updateInformationField(self.result)