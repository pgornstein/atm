def show_main_menu():
    print("Welcome to Terminal Teller!\n")
    print("1) create account")
    print("2) log in")
    print("3) quit\n")

def show_login_menu(hello):
    print(hello + '\n')
    print("    1) Check balance")
    print("    2) Withdraw funds")
    print("    3) Deposit funds")
    print("    4) sign out\n")

def display_text(text):
    print('\n' + text + '\n')

def get_input(prompt):
    return input(prompt)