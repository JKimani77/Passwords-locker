import unittest
from credentials import Credentials


class TestCredentials(unittest.TestCase):

    '''
    test class that defines test cases for  the credentials class
    '''

    def setUp(self):
        '''
        set up method  that runs before each test case
        '''

        self.new_credentials = Credentials("Snapchat", "9876")

    def tearDown(self):
        '''
         tear down method that does clean up after each test case has run.
        '''
        Credentials.cred_list = []

    def test_credentials_instance(self):
        '''
        method to test if new credentials have been instanciated properly
        '''

        self.assertEqual(self.new_credentials.account_name, "Snapchat")
        self.assertEqual(self.new_credentials.account_password, "9876")

    def test_save_credentials(self):
        '''
        test case to test if credentials objects have been saved
        '''

        self.new_credentials.save_credentials()  # save new user
        self.assertEqual(len(Credentials.cred_list), 1)

    def test_delete_credentials(self):
        '''
        test delete credentials to test if we can remove a account from our list
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("Snapchat", "9876")
        test_credentials.save_credentials()
        self.new_credentials.delete_credentials()  # to delete a credentials   object
        self.assertEqual(len(Credentials.cred_list), 1)

    def test_getcredentials_by_name(self):
        '''
        test to check if credentials by the account name and can display information
        '''   

        self.new_credentials.save_credentials()
        test_credentials = Credentials("Snapchat", "9876")
        test_credentials.save_credentials()
        # found_credentials = Credentials.find_by_number("0711491808")
        # self.assertEqual(found_credentials.credentials_name,
        #                  test_credentials.password)

    def test_display_all_credentials(self):
        '''
        Test to check if all contacts can be viewed
        '''

        self.assertEqual(Credentials.show_credentials(),
                         Credentials.cred_list)


if __name__ == '__main__':
    unittest.main()

