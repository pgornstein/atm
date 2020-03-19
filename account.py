import json
import os

DIR = os.path.dirname(__file__)
DATAFILENAME = "data.json"  # use your teller filename
DATAPATH = os.path.join(DIR, DATAFILENAME)


class AuthenticationError(Exception):
    pass


class Account:
    data_path = DATAPATH

    def __init__(self, account_num="", pin="", balance=0, first_name="", last_name = ""):
        self.account_num = account_num
        self.pin = int(pin)
        self.balance = balance
        self.first_name = first_name.lower()
        self.last_name = last_name.lower()

    @classmethod
    def account_in_data(cls, num):
        with open("data.json", 'r') as json_file:
            data = json.load(json_file)
            if num in data:
                return True
            else: 
                return False
                
    def validate(self):
        # return True or False if the account_num and pin is in the datafile
        with open("data.json", 'r') as json_file:
            data = json.load(json_file)
        if self.account_num in data and self.pin == data[self.account_num]["pin"][0]:
            return True
        else:
            return False

    def load(self):
        # load the account with this object's self.account number from the
        # datafile and set its attributes accordingly
        # user = Account(account_num="0000000001", pin="1234")
        # if user.validate():
        #    user.load()
        # else:
        #    raise AuthenticationError
        #
        # this would set the user's balance (and any other information you
        # chose to represent, like first name, last name, etc. from the
        # json file
        with open("data.json", 'r') as json_file:
            data = json.load(json_file)
        self.first_name = data[self.account_num]["first name"][0]
        self.last_name = data[self.account_num]["last name"][0]
        self.balance = data[self.account_num]["balance"][0]

    def save(self):
        # update the json data with this account's data, either creating a new
        # account record or updating an existing one
        with open("data.json", 'r') as json_file:
            data = json.load(json_file)
        if self.account_num not in data.keys():
            user_dict = {self.account_num: {}}
            data.update(user_dict)
            first_name_dict = {"first name": [self.first_name]}
            last_name_dict = {"last name": [self.last_name]}
            pin_dict = {"pin": [self.pin]}
            balance_dict = {"balance": [self.balance]}
            data[self.account_num].update(first_name_dict)
            data[self.account_num].update(last_name_dict)
            data[self.account_num].update(pin_dict)
            data[self.account_num].update(balance_dict)
        else:
            data[self.account_num]["first name"][0] = self.first_name
            data[self.account_num]["last name"][0] = self.last_name
            data[self.account_num]["pin"][0] = self.pin
            data[self.account_num]["balance"][0] = self.balance
        with open("data.json", 'w') as json_file:
            json.dump(data, json_file, indent=2)

    def deposit(self, amount):
        amount = float(amount)
        # increase the balance of this account
        self.balance += amount

    def withdraw(self, amount):
        amount = float(amount)
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False
        # decrease the balance of this account
        # raise ValueError if there is insufficient funds or create an
        # InsufficientFunds exception type
