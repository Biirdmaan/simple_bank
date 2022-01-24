import itertools
import account


class Customer:
    customer_id = itertools.count()

    def __init__(self, first_name, last_name, ssn, customer_id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.ssn = str(ssn)
        self.accounts = []
        if customer_id:
            self.customer_id = customer_id
        else:
            self.customer_id = next(self.customer_id)
            self.customer_id = 11110 + self.customer_id



    """Three methods of changing customer name:
    1. Change first name
    2. Change last name
    3. Change first & last name 
    """
    def change_first_name(self, first_name):
        self.first_name = first_name

    def change_last_name(self, last_name):
        self.last_name = last_name

    def change_customer_name(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    # Show customer information: social security number, first & last name & account: number, balance, type
    def show_customer(self):
        account_detail = []
        for account in self.accounts:
            details = account.account_number, account.balance, account.account_type
            account_detail.append(details)
        return self.ssn, self.first_name, self.last_name, account_detail

    # Add new account
    def add_account(self):
        acc = account.Account()
        self.accounts.append(acc)
        print(f"Account created! \n"
              f"Account number: {acc.account_number},\n"
              f"Account type: {acc.account_type}, \n"
              f"Account balance: {acc.balance}")
