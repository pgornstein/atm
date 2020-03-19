import view
from account import Account

from random import randint

def atm():

    #Main menu loop
    while True:
        view.show_main_menu()
        selection = view.get_input("Your choice: ")

        #Account creation
        if selection == "1":
            view.display_text("Account creation")
            first_name = view.get_input("    First name: ")
            last_name = view.get_input("    Last name: ")
            pin = view.get_input("    PIN: ")
            confirm_pin = view.get_input("    Confirm PIN: ")
            if pin != confirm_pin:
                view.display_text("PINs do not match, please try again")
            else:
                #account_number = model.new_account(first_name, last_name, pin)
                while True:
                    account_number = randint(100000, 999999)
                    if Account.account_in_data(account_number) == False:
                        new_account = Account(account_number, pin, 0, first_name, last_name)
                        new_account.save()
                        view.display_text(f"account created, your account number is {new_account.account_num}.")
                        break

        #Login
        elif selection == "2":
            account_number = view.get_input("    Account number: ")
            pin = view.get_input("    PIN: ")
            #valid, name = model.login(account_number, pin)
            user_account = Account(account_number, pin)
            if user_account.validate() == False:
                raise AuthenticationError
                view.display_text("No account exists with such a PIN, please try again")
            else:
                user_account.load()
                #Loop for user display after login
                while True:
                    view.show_login_menu(f"Hello, {user_account.first_name.title()} {user_account.last_name.title()} ({user_account.account_num})")
                    new_selection = view.get_input("Your choice: ")

                    #Check balance
                    if new_selection == "1":
                        balance = user_account.balance
                        balance = '${:,.2f}'.format(balance)
                        view.display_text(f"    Your balance is {balance}")

                    #Withdrawal
                    elif new_selection == "2":
                        amount_to_withdraw = view.get_input(    "How much to withdraw: ")
                        #insufficient = model.withdraw(account_number, amount_to_withdraw)
                        if user_account.withdraw(amount_to_withdraw) == False:
                            view.display_text("!! INSUFFICIENT FUNDS !!")
                    
                    #Deposit
                    elif new_selection == "3":
                        amount_to_deposit = view.get_input(    "How much to deposit: ")
                        #model.deposit(account_number, amount_to_deposit)
                        user_account.deposit(amount_to_deposit)

                    #Sign out
                    elif new_selection == "4":
                        user_account.save()
                        break
        #Quit
        elif selection == "3":
            break

if __name__ == "__main__":
    atm()