import itertools
import account


class Customer:
    customer_id = itertools.count()

    def __init__(self, first_name=None, last_name=None, ssn=None, customer_id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.ssn = str(ssn)
        self.accounts = []

        if customer_id:
            self.customer_id = next(self.customer_id)
            self.customer_id = int(customer_id) + self.customer_id
        else:
            self.customer_id = next(self.customer_id)
            self.customer_id = 11110 + self.customer_id

    def __str__(self):
        """
        Show customer information instead of an object. Similar as show_customer().
        :return: returns a string instead of an object
        """
        acc_lst = []
        for x in self.accounts:
            acc_lst.append(x.account_number)
            acc_lst.append(x.account_type)
            acc_lst.append(x.balance)
        return f"Customer ID: {self.customer_id},\nFull name: {self.first_name} {self.last_name},\nSSN: " \
               f"{self.ssn},\nAccounts: {acc_lst}"

    def show_customer(self):
        """
        Show customer information.
        :return: social security number, first & last name & account: number, balance, type
        """
        account_detail = []
        for account in self.accounts:
            details = account.account_number, account.balance, account.account_type
            account_detail.append(details)
        return self.customer_id, self.ssn, self.first_name, self.last_name, account_detail

    def add_account(self):
        """
        Add new account
        :return: account number, account type, balance
        """
        acc = account.Account()
        self.accounts.append(acc)
        print("Account has been created")
        return f"Account number: {acc.account_number},\nAccount type: {acc.account_type},\n Account balance: {acc.balance}"

    def close_account(self, account_number):
        """
        Close account by account number
        :param account_number:
        :return:
        """
        for x in self.accounts:
            if account_number == x.account_number:
                account = self.accounts.index(x)
                self.accounts.pop(account)

