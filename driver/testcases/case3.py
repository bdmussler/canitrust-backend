# ------------------------------------------------------------------------------------------------
#  Copyright (c) mgm security partners GmbH. All rights reserved.
#  Licensed under the AGPLv3 License. See LICENSE.md in the project root for license information.
#-------------------------------------------------------------------------------------------------

from testcases.testCase import TestCase
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from helper import Logger
logger = Logger(__name__).logger

class Case3(TestCase):

    def __init__(self):
        TestCase.__init__(self)
        self.testCaseNum = 3

    def executeTest(self, webDriver):
        """ Definition of a testcase
            Test result MUST be set to self.data
        """
        webDriver.get("https://invalidcert.test-canitrust.com")
        WebDriverWait(webDriver, 30).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        HSTS = webDriver.current_url
        if "https" in HSTS:
            textGetFromBrowser = webDriver.find_element_by_tag_name('body')
            dataText = textGetFromBrowser.text 
        self.data = {'first_HSTS':HSTS, "respone data" : dataText}
        return 1

    def evaluate(self):
        # Todo
        pass
