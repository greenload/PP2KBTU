#Create a bank account class that has attributes owner, balance and two methods deposit and withdraw.
#Withdrawals may not exceed the available balance.
#Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account():

    def __init__(self, owner="mr. Blanc", balance=0):
        self.owner = owner
        self.balance = balance

    def changeOwner(self):
        self.owner = input("Enter a name of the account owner, please: ")
        print(f"Account owner name is set to {self.owner}\n")

    def deposit(self):
        self.toDeposit = float(input("Enter a sum to deposit: "))
        self.balance += self.toDeposit
        print(f"You have successfully deposit {self.toDeposit}.\nYour current balance is {self.balance}.\n")

    def withdraw(self):
        self.toWithdraw = float(input("Enter a sum to withdraw: "))
        if self.toWithdraw > self.balance:
            print(f"Your balance is {self.balance}, it is insufficient to withdraw {self.toWithdraw}.\n")
        else:
            self.balance -= self.toWithdraw
            print(f"You have successfully withdrawn {self.toWithdraw}.\nYour current balance is {self.balance}.\n")
    
    def show(self):
        print(f"Your current balance is {self.balance}.\n") 

account = Account()

account.changeOwner()

account.show()

account.withdraw()

account.deposit()

account.withdraw()


