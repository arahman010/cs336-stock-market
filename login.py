import os

class User:
    def __init__(self):
        self.username = None
        self.password = None

    # Private variables
    __login_file = "login_credentials.txt"

    @classmethod
    def get_username(self):
        """
        Returns the username to login to the DB
        """
        try:
            login_credentials = open(self.__login_file, "r")
            username = login_credentials.readline()
            login_credentials.close()
            return username.rstrip()
        except IOError:
            with open(self.__login_file, "wb") as login_credentials:
                login_credentials.write("#### Replace this with your username ####\n#### Replace this with your password ####")
            raise IOError("login_credentials.txt was not found, write your username and password on lines 1 and 2 on the created file")
            return None

    @classmethod
    def get_password(self):
        """
        Returns the password to login to the DB
        """
        try:
            login_credentials = open(self.__login_file, "r")
            password = login_credentials.readlines()[1]
            login_credentials.close()
            return password.rstrip()
        except IOError:
            with open(self.__login_file, "wb") as login_credentials:
                login_credentials.write("#### Replace this with your username ####\n#### Replace this with your password ####")
            raise IOError("login_credentials.txt was not found, write your username and password on lines 1 and 2 on the created file")
