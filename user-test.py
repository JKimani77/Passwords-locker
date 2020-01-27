import unittest
from user import User


class TestUser(unittest.TestCase):

    '''
    test class for behaviours


    Args:
        unittest.TestCase :Test case that helps in creating test cases

    '''

    def setUp(self):
        '''
        method run before each test case
        '''

        self.new_user = User("ramza", "password")
