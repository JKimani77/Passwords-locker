import random
from user import User
from credentials import Credentials

# The functions defined below creates account names, save credentials, 
# find credentials created and deletes credentials respectively.


def create_new_credential(account_name, account_password):
    '''
    method that creates  new  account name
    '''
    new_credential = Credentials(account_name, account_password)

    return new_credential


def save_new_credential(credentials):
    '''
    method to save new credentials
    '''

    credentials.save_credentials()


def find_credential(account_name):
    '''
    method to find a credential that has been created
    '''

    return Credentials.find_by_name(account_name)


def display_credential():
    '''
    method to dispay a credential that has been created
    '''
    return Credentials.display_credentials()


def delete_credential(credentials):
    '''
    method to delete a credential that has been created
    '''

    return Credentials.delete_credentials(credentials)

def main():
    print('\n')
    while True:
        print(
            "********************  Welcome to password locker!!! ********************"
        )
        print('\n')
        print("""Use these short codes to navigate: \n "nu"- add new user \n "lg"-login to your created account \n "ex"-to exit the system""")
        short_code = input().lower()
        print('\n')

        if short_code == 'nu':
            print('-----------create username---------')
            created_user_name = input()

            print('-----------create password---------')
            created_user_password = input()

            print('-----------confirm password---------')
            confirm_password = input()
            print('\n')

            while confirm_password != created_user_password:
                print("-----------Invalid Password !-----------")
                print("-----------Enter user name-----------")
                created_user_password = input()
                print("-----------Confirm your password-----------")
                confirm_password = input()
                print('\n')
                
            else:
                print(
                    f"Hello {created_user_name}! You have successfully create your account! "
                )
                print('\n')
                print("****** Proceed to login *******")
                print('\n')
                print("-----------Username-----------")
                entered_username = input()
                print("-----------Your password-----------")
                entered_password = input()

            while entered_username != created_user_name or entered_password != created_user_password:
                print('\n')
                print("Invalid username or password")
                print("-----------Username-----------")
                entered_username = input()
                print("-----------Your password-----------")
                entered_password = input()
                print('\n')

            else:
                print('\n')
                print(
                    f"******* Welcome {entered_username} to your account *******")
                print('\n')

                print("Select an option to continue: \n Enter 1, 2, 3, 4 or 5")
                print('\n')
