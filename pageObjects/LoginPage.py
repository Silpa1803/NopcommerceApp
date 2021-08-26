from selenium import webdriver

class LoginPage:
    textbox_username_ID="Email"
    textbox_password_ID="Password"
    button_login_Class="button-1 login-button"
    link_logout_xpath="/a[@href='/logout']"

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        self.driver.find_element_by_id(self.textbox_username_ID).clear()
        self.driver.find_element_by_id(self.textbox_username_ID).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_ID).clear()
        self.driver.find_element_by_id(self.textbox_password_ID).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_class(self.button_login_Class).click()

    def clickLogout(self):
        self.driver.find_element_by_xpath(self.link_logout_xpath).click()

