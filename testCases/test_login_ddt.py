import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen
from utilities import ExcelUtils
import time

class Test_002_DDT_Login:
    baseURL = Readconfig.getApplicationURL()
    path=".//testData/Data.xlsx"
    logger= LogGen.loggen()

    def test_login_ddt(self,setup):
        self.logger.info("******* Test_002_DDT_Login *******")
        self.logger.info("******* Verifying Login DDT Test *******")
        self.driver=setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.rows=ExcelUtils.getRowCount(self.path,'Sheet1')
        print("Number of Rows in an Excel = ",self.rows)

        list_status=[]     #Empty list variable

        for r in range(2,self.rows+1):
            self.user=ExcelUtils.readData(self.path,'Sheet1',r,1)
            self.password = ExcelUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = ExcelUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.exp=="pass":
                    self.logger.info(" ********** PASSED **********")
                    self.lp.clickLogout();
                    list_status.append("pass")
                elif self.exp=="fail":
                    self.logger.info(" ********** FAILED **********")
                    self.lp.clickLogout();
                    list_status.append("fail")

            elif act_title != exp_title:
                if self.exp == "pass":
                    self.logger.info(" ********** FAILED **********")
                    list_status.append("pass")
                elif self.exp == "fail":
                    self.logger.info(" ********** PASSED **********")
                    list_status.append("pass")

        if "fail" not in list_status:
            self.logger.info("********** Login DDT test Passed **********")
            self.driver.close()
            assert True
        else:
            self.logger.info("********** Login DDT test Failed **********")
            self.driver.close()
            assert False

        self.logger.info("********** End of Login DDT Test **********")
        self.logger.info("********** Completed TC_loginDDT_002 **********")
