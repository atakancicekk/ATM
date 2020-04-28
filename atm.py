import time


customer_db = {
    "atakan cicek": {
        "username": "atakancicek",
        "password": "1234",
        "balance": 4000
    },
    "harry potter": {
        "username": "harrypotter",
        "password": "7890",
        "balance": 5000
    },
    "miley cyrus": {
        "username": "mileycyrus",
        "password": "1111",
        "balance": 4400
    }
}


def welcome():
    print "Welcome to Bank Atakan !"
    print "*****************************"
    user_selection = input("press 0 to log in, press 1 to sign up: ")
    if user_selection == 0:
        login()
    elif user_selection == 1:
        signup()


def login():
    print " "
    print " "
    print "Login"
    print "*****************************"
    input_username = raw_input("username: ")
    for user in customer_db:
        if input_username == customer_db[user]["username"]:
            input_password = raw_input("password: ")
            if input_password == customer_db[user]["password"]:
                account(customer_db[user])
            else:
                print "Wrong password, please try again..."
                login()


def signup():
    print "Sign Up"
    print "*****************************"
    input_fullname = raw_input("Enter your full name: ")
    input_username = raw_input("Enter a username: ")
    input_password = raw_input("Enter a password: ")
    customer_db[input_fullname] = {"username": input_username, "password": input_password, "balance": 0}
    login()


def account(user):
    print " "
    print " "
    print "Account Page"
    print "*****************************"
    print "Have a nice day", user["username"], ". Your current balance is:", user["balance"]
    print "What you would like to do ?"
    user_selection = input(
        "1. Withdraw money\n"
        "2. Transfer money\n"
        "3. Deposit money\n"
        "4. Logout\n"
        "5. Exit from ATM\n"
    )
    if user_selection == 1:
        withdraw(user)
    elif user_selection == 2:
        transfer_money(user)
    elif user_selection == 3:
        deposit(user)
    elif user_selection == 4:
        welcome()
    elif user_selection == 5:
        exit()
    else:
        print "Sorry, wrong key pressed. Please select 1 or 2"
        account(user)


def withdraw(user):
    print " "
    print " "
    print "Withdraw Money"
    print "*****************************"

    withdraw_amount = input("Please enter the amount: ")

    if user["balance"] > withdraw_amount:
        print "Making the transaction, please wait."
        time.sleep(3)
        user["balance"] -= withdraw_amount
        print "Money withdrawed. Your new balance is: ", user["balance"]
        time.sleep(1.5)
        print "Please wait while you are being redirected..."
        time.sleep(4)
        account(user)
    else:
        print "Insufficent Funds !"
        withdraw(user)


def deposit(user):
    print " "
    print " "
    print "Deposit Money"
    print "*****************************"

    deposit_amount = input("Please enter the deposit amount: ")

    print "Making the transaction, please wait."
    time.sleep(3)
    user["balance"] += deposit_amount
    print "Money deposited. Your new balance is: ", user["balance"]
    time.sleep(1.5)
    print "Please wait while you are being redirected..."
    time.sleep(4)
    account(user)


def transfer_money(user):
    for customer in customer_db:
        if user["username"] == customer_db[customer]["username"]:
            pass
        else:
            print customer_db[customer]["username"]

    transfer_selection = raw_input("Please type the recipient: ")
    transfer_amount = input("Please enter the amount: ")

    if user["balance"] >= transfer_amount:
        for person in customer_db:
            if transfer_selection in customer_db[person]["username"]:
                customer_db[person]["balance"] += transfer_amount
                user["balance"] -= transfer_amount
                print "Making the transfer, please be patient."
                time.sleep(3)
                print "Money sent. Your new balance is: ", user["balance"]
                time.sleep(1.5)
                print "Please wait while you are being redirected..."
                time.sleep(4)
                account(user)
    else:
        print "Insufficent Funds !"
        transfer_money(user)


'''
    if user["balance"] <= deposit_amount:
        print "money sent"
    else:
        print "Insufficent funds. Please try again."
        deposit(user)

'''

welcome()
