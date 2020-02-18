class Credentials:

    '''
    class that generates new instance of credentials
    '''

    def __init__(self, account_name, account_password):
        self.account_name = account_name
        self.account_password = account_password

    cred_list = []

    def save_credentials(self):
        '''
        function to save credential objects into list
        '''

        self.cred_list.append(self)

    def delete_credentials(self):
        '''
        deleting credentials
        '''

        Credentials.cred_list.remove(self)


    @classmethod
    def exists(cls, account_name):
        '''
        func to check if credential exists
        Args:
            name: account_name to be searched
        boolean:
                true or false
        '''

        for credentials in cls.cred_list:
            if credentials.account_name == account_name:
                return True
        return False


    @classmethod
    def getcredentials_by_name(cls, account_name):
        '''
        function that takes in a name and returns a credential that matches that name

        Args:
            name: account_name that has a password
        return:
            the account that matches that name

        '''

        for credentials in cls.cred_list:
            if credentials.account_name == account_name:
                return credentials

    @classmethod
    def show_credentials(cls):
        '''
        function that displays credentials
        '''
        return cls.cred_list
