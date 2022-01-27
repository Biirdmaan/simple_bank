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
        """
        The main function behind deposit. Changing balance when user insert amount.
        :param amount:
        :return: account balance
        """
        self.balance += amount
        print(f"Your debit account have been filled. Your current balance is: {self.balance}")
        return self.balance

    def withdraw(self, amount):
        """
        The main function behind withdraw. if customer withdraw,
        account balance will be subtracted with the amount. If customer wish to withdraw more amount than user has,
        customer will get an error message.
        :param amount:
        :return: balance
        """
        if amount <= self.balance:
            self.balance -= amount
            print(f"Successful withdraw, your remain balance is: {self.balance}")
        else:
            print(f"Insufficient funds\nYour current balance is: {self.balance}")
            return self.balance

    def show_account(self):
        """
        Show account information
        :return:  account_number, balance, type
        """
        return self.account_number, self.balance, self.account_type


