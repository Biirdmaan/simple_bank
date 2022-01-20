import itertools
from customer import Customer

class Account:
    account_number = itertools.count()
    account_type = "Debit account"
    balance = 0.0

    def __init__(self, customer_id):
        self.balance = 0
        self.customer_id = customer_id
        print(self.customer_id)

        self.account_number = next(self.account_number)     #
        self.account_number = 1001 + self.account_number



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



account1 = Account()