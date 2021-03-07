class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Welcome to the deposite and withdrawal machine")
    def Deposit(self):
        amount=float(input("Enter amount to be Deposite:"))
        self.balance += amount
        print("Amount Deposited:",amount)
    def Withdraw(self):
        amount=float(input("Enter amount to Withdrawn:"))
        if self.balance>=amount:
            self.balance-= amount
            print("You Withdrew:",amount)
        else:
            print("Insufficient balance.")
    def Display(self):
        print("Net available Balance:",self.balance)
s =Bank_Account()
s.Deposit()
s.Withdraw()
s.Display()
