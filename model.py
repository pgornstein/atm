import json
from random import randint

def new_account(first_name, last_name, pin):
    first_name = first_name.lower()
    last_name = last_name.lower()
    pin = int(pin)
    data = read_json()
    while True:
        account_number = str(randint(100000, 999999))
        if account_number in data:
            continue
        else:
            user_dict = {account_number: {}}
            data.update(user_dict)
            first_name_dict = {"first name": [first_name]}
            last_name_dict = {"last name": [last_name]}
            pin_dict = {"pin": [pin]}
            balance_dict = {"balance": [0]}
            data[account_number].update(first_name_dict)
            data[account_number].update(last_name_dict)
            data[account_number].update(pin_dict)
            data[account_number].update(balance_dict)
            write_json(data)
            break
    return account_number

def login(account_number, pin):
    pin = int(pin)
    data = read_json()
    if account_number in data and pin == data[account_number]["pin"][0]:
        name = data[account_number]["first name"][0] + " " + data[account_number]["last name"][0]
        return True, name
    else:
        return False, None

def check_balance(account_number):
    data = read_json()
    print(data[account_number]["balance"][0])
    return data[account_number]["balance"][0]

def withdraw(account_number, amount_to_withdraw):
    amount_to_withdraw = amount_to_withdraw.strip("$")
    amount_to_withdraw = float(amount_to_withdraw)
    data = read_json()
    balance = data[account_number]["balance"][0] - amount_to_withdraw
    if balance >= 0:
        data[account_number]["balance"][0] = balance
        write_json(data)
        return False #not insufficient
    else:
        return True #insufficient funds

def deposit(account_number, amount_to_deposit):
    amount_to_deposit = amount_to_deposit.strip("$")
    amount_to_deposit = float(amount_to_deposit)
    data = read_json()
    balance = data[account_number]["balance"][0] + amount_to_deposit
    data[account_number]["balance"][0] = balance
    write_json(data)

def read_json():
    with open("data.json", 'r') as json_file:
        data = json.load(json_file)
    return data

def write_json(data):
    with open("data.json", 'w') as json_file:
        json.dump(data, json_file, indent=2)