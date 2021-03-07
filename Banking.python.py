class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Welcome to the deposite and withdrawal machine")
    def deposit(self):
        amount=float(input("Enter amount to be deposite:"))
        self.balance += amount
        print("Amount Deposited:",amount)
    def withdraw(self):
        amount=float(input("Enter amount to withdrawn:"))
        if self.balance>=amount:
            self.balance-= amount
            print("You Withdrew:",amount)
        else:
            print("Insufficient balance.")
    def display(self):
        print("Net available balance:",self.balance)
s =Bank_Account()
s.deposit()
s.withdraw()
s.display()
