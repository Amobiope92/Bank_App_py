import sys
import time
import random
class Bank:
    def __init__(self):
        self.bankname = 'APEX BANK'
        self.name = ""
        self.pin = ""
        self.acc_no = 0
        self.login = []
        self.acc_bal = 0
        self.acc_detail = []
class operation(Bank):
    def __init__(self):
        super().__init__()
        print(f"WELCOME TO {c1.bankname}!!!")
        print("""
              ........................................
              Please select an operation function below
              1. Account Registration
              2. Account Login
              3. Exit
              """)
        ops = input('Select an option\n>')
        if ops == '1':
            c3 = registration()
        elif ops == '2':
            c4 = login()
        elif ops == '3':
            sys.exit()
        else:
           print('Invalid selection! Please try again')
           c2 = operation()

class registration(Bank):
    def __init__(self):
        super().__init__()
        c1.name = input('Enter your name?\n>')
        c1.acc_no = random.randint(1000000000, 10000000000)
        c1.pin = input('Kindly enter a 4digits account pin of your choice\n>')
        while len(str(c1.pin)) == 4:
                c1.acc_detail.append({"Name": c1.name, "Account number": c1.acc_no, "Password": c1.pin})
                print(c1.acc_detail)
                c4 = login()
        else:
            print('PIN input invalid! Enter a 4digits pin\n>')
            c3 = registration()

class login(Bank):
    def __init__(self):
        super().__init__()
        acc_validation = input('Enter your account number\n>')
        password = input('Enter your pin\n>')
        while acc_validation == c1.acc_no or password == c1.pin:
            c5 = bank_app()
        else:
            print('Invalid account number\password! Enter valid details')
            c4 = login()
class bank_app(Bank):
    def __init__(self):
        super().__init__()
        print("""
            Welcome to APEX BANK what would you like to do today?
            1. Check Account Balance
            2. DEPOSIT
            3. WITHDRAW
            4. LOG-OUT
              """)
        option_choice = input('Kindly select an option of what you will like to do\n>')
        if option_choice == '1':
            print(f'Your account balance is: ${c1.acc_bal}')
            c5 = bank_app()
        elif option_choice == '2':
            depo = int(input('How much would you like to deposit?\n>'))
            c1.acc_bal += depo
            print(f'Your account balance is: ${c1.acc_bal}')
            c1.acc_detail.append({"Balance": c1.acc_bal})
        elif option_choice == '3':
            withdrawal = int(input('How much would you like to withdraw?\n>'))
            if withdrawal < c1.acc_bal:
                c1.acc_bal -= withdrawal
                print(f'Your account balance is: ${c1.acc_bal}')
                c1.acc_detail.append({"Balance": c1.acc_bal})
            else:
                print('Insufficient funds!')
                c5 = bank_app()
        elif option_choice == '4':
            c2 = operation()
        else:
            print('Invalid option! Kindly choose within the options provided\n>')
            c5 = bank_app()
        # myquery = "INSERT INTO CUSTOMER_DETAILS VALUES(%s, %s, %s, %s)"
        # myquery = "INSERT CUSTOMER_DETAILS VALUES(%s, %s, %s, %s)"
        # myvalues = (c1.name, c1.acc_no, c1.pin, c1.acc_bal)
        # mycursor.execute(myquery, myvalues)
        # mycon.commit()

    
c1 = Bank()
c2 = operation()
c3 = registration()
c4 = login()
c5 = bank_app()
