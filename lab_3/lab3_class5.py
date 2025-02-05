class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount},New Balance:{self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("jetpeydi")
        else:
            self.balance -= amount
            print(f"Withdrawn:{amount},New Balance:{self.balance}")

acc = Account("John", 100)
acc.deposit(70)
acc.withdraw(300)
acc.withdraw(500)
