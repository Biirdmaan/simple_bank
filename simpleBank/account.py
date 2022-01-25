import itertools


class Account:
    account_number = itertools.count()

    def __init__(self):
        self.account_type = "Debit account"
        self.balance = 0
        self.account_number = next(self.account_number)  #
        self.account_number = 1001 + self.account_number

    def __str__(self):
        return f":{self.account_number}:{self.account_type}:{self.balance}"

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


