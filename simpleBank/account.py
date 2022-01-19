import itertools


class Account:
    account_number = itertools.count()
    account_type = "Debit account"
    balance = 0.0

    def __init__(self, balance):
        self.balance = float(balance)
        self.account_number = next(self.account_number)
        self.account_number = 1000 + self.account_number


    def deposit(self, amount):
        self.balance += amount
        print(f"Your debit account have been filled. Your current balance is: {self.balance}")
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Successful withdraw, your remain balance is: {self.balance}")
        else:
            print(f"Insufficient funds\nYour current balance is: {self.balance}")
            return self.balance

    def show_account(self):
        return self.account_number, self.balance, self.account_type


abc = Account(1000.49344)
bcd = Account(2000)
dfg = Account(3000)


print(abc.show_account())