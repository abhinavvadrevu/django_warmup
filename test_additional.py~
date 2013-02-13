"""
Each file that starts with test... in this directory is scanned for subclasses of unittest.TestCase or testLib.RestTestCase
"""

import unittest
import os
import testLib

class TestUnit(testLib.RestTestCase):
    """Issue a REST API request to run the unit tests, and analyze the result"""
    def testUnit(self):
        respData = self.makeRequest("/TESTAPI/unitTests", method="POST")
        self.assertTrue('output' in respData)
        print ("Unit tests output:\n"+
               "\n***** ".join(respData['output'].split("\n")))
        self.assertTrue('totalTests' in respData)
        print "***** Reported "+str(respData['totalTests'])+" unit tests"
        # When we test the actual project, we require at least 10 unit tests
        minimumTests = 10
        if "SAMPLE_APP" in os.environ:
            minimumTests = 4
        self.assertTrue(respData['totalTests'] >= minimumTests,
                        "at least "+str(minimumTests)+" unit tests. Found only "+str(respData['totalTests'])+". use SAMPLE_APP=1 if this is the sample app")
        self.assertEquals(0, respData['nrFailed'])


        
class TestAddUser(testLib.RestTestCase):
    """Test adding users"""
    def assertResponse(self, respData, count = 1, errCode = testLib.RestTestCase.SUCCESS):
        """
        Check that the response data dictionary matches the expected values
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)
    
    def testAdd1(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        self.assertResponse(respData, count = 1)
    def testAdd2(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'a'*129, 'password' : 'pass'} )
        self.assertResponse(respData, errCode = -3, count=None)
    def testAdd3(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : '', 'password' : 'pass'} )
        self.assertResponse(respData, errCode = -3, count=None)
    def testAdd4(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'abs', 'password' : 'p'*129} )
        self.assertResponse(respData, errCode = -4, count=None)
    def testAdd5(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'abs1', 'password' : ''} )
        self.assertResponse(respData, errCode = 1, count=1)
    def testAdd6(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'abs2', 'password' : 'p'*128} )
        self.assertResponse(respData, errCode = 1, count=1)
    def testLogin1(self):
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'abs', 'password' : 'pass'} )
        self.assertResponse(respData, errCode = -1, count=None)
    def testLogin2(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'abs1', 'password' : ''} )
        self.assertResponse(respData, errCode = 1, count=1)
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'abs1', 'password' : ''} )
        self.assertResponse(respData, errCode = 1, count=2)
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'abs1', 'password' : ''} )
        self.assertResponse(respData, errCode = 1, count=3)
    def testLogin3(self):
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'abs1', 'password' : 'p'} )
        self.assertResponse(respData, errCode = -1, count=None)
