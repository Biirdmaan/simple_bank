import customer
import re
from account import Account


class Bank:

    def __init__(self):
        self.customers = []
        self.name = "NBI"
        self._load()

    def _load(self):
        """
        Load and strip customer information from a textfile.
        Customer information initialize to a customer object and append to customers[], if ssn does not exist.
        if customer_id already exist, customer gets a new customer_id
        :return: self.customers
        """

        for line in open("Customer_bank.txt", "rt").readlines():
            cust = line.strip()
            cust = re.split(pattern=r"[:#]", string=cust)


            if self.customers == []:
                client = customer.Customer(cust[1], cust[2], cust[3], cust[0])
                self.customers.append(client)

                # Adding accounts and append to list
                acc1 = Account(cust[4], cust[6], cust[5])
                acc2 = Account(cust[7], cust[9], cust[8])
                client.accounts.append(acc1)
                client.accounts.append(acc2)

            else:
                for x in self.customers:
                    if int(cust[0]) != int(x.customer_id):
                        client = customer.Customer(cust[1], cust[2], cust[3], cust[0])
                        self.customers.append(client)

                        # Adding accounts and append to list
                        acc1 = Account(cust[4], cust[6], cust[5])
                        acc2 = Account(cust[7], cust[9], cust[8])
                        client.accounts.append(acc1)
                        client.accounts.append(acc2)
                        break
                    else:
                        client = customer.Customer(cust[1], cust[2], cust[3])
                        self.customers.append(client)

                        # Adding accounts and append to list
                        acc1 = Account(cust[4], cust[6], cust[5])
                        acc2 = Account(cust[7], cust[9], cust[8])
                        client.accounts.append(acc1)
                        client.accounts.append(acc2)
                        break
        return self.customers

    def get_all_customers(self):
        """
        Get all customers
        :return: list of all customers, showing customer information: ssn, first_name and last_name
        """
        all_customers = []

        for customer in self.customers:
            details = customer.customer_id, customer.ssn, customer.first_name, customer.last_name
            all_customers.append(details)
        return all_customers

    def add_customer(self, first_name, last_name, ssn):
        """
        Add new customer to customers [list] if ssn not used.
        :param first_name:
        :param last_name:
        :param ssn:
        :return: True if customer created, False if not
        """

        check = True

        if self.customers == []:
            check
        else:
            for x in self.customers:
                if int(ssn) == int(x.ssn):
                    print("SSN already exist!")
                    check = False
                    break

        if check == True:
            client = customer.Customer(first_name, last_name, ssn)
            self.customers.append(client)
            print(f"Customer {client.customer_id}: {client.first_name} {client.last_name} has been added!")

        return check

    def get_customer_by_ssn(self, pnr):
        """
        Get customer by ssn.
        :param pnr:
        :return: information about customer + accounts.
        """
        if self.customers == []:
            print(f"Error, no customer found with ssn: {pnr}")
        else:
            for x in self.customers:
                if pnr == x.ssn:
                    return x.show_customer()
                #else:
            print("Customer not found!")

    def change_customer_name(self, ssn, first_name, last_name):
        """
        Change customer name.
        :param ssn:
        :param name: Enter first and last name.
        :return: True if customer name change, False if not
        """
        if self.customers == []:
            print("Bank has no customers!")
            print(f"Customer with ssn: {ssn} not found!")
            return False
        else:
            for x in self.customers:
                if ssn == x.ssn:
                    x.first_name = first_name
                    x.last_name = last_name
                    print(f"Customer {x.first_name} {x.last_name} has been updated!")
                    return True

            print(f"Person with pnr: {ssn} is not a customer!")
            return False

    def remove_customer(self, ssn):
        """
        Remove customer, accounts closes and customer will receive total amount from accounts
        :param ssn:
        :return:Customer details + received balance or ssn not found
        """
        return_balance = 0

        for x in self.customers:
            if x.ssn == ssn:
                customer = self.customers.index(x)
                self.customers.pop(customer)

                for y in x.accounts:
                    return_balance += y.balance
                return f"Customer {x.first_name} {x.last_name} is deleted\n" \
                       f"Return balance: {return_balance}"
            else:
                f"Customer with personal number: {ssn} not found!"

    def add_account(self, ssn):
        """
        Adds a new account by ssn
        :param ssn:
        :return: String "Account created, with information about the account"
        """
        if self.customers == []:
            print(f"Bank has no customer, no customer with ssn: {ssn} found")
        else:
            for x in self.customers:
                if ssn == x.ssn:
                    print(x.add_account())
                    break

    def get_account(self, ssn, account_id):
        """
        Get account by ssn & account_number
        :param ssn:
        :param account_id:
        :return: Account details or Error if ssn/account_number is not correct
        """

        for x in self.customers:
            if x.ssn == ssn:
                for y in x.accounts:
                    if y.account_number == account_id:
                        return f"Account number: {y.account_number}\nBalance: {y.balance}\nAccount type: {y.account_type}"

        return "Error, something went wrong"
        # Returnerar en string: kontonummer, saldo, kontotyp

    def deposit(self, ssn, account_number, amount):
        """
        Account deposit
        :param ssn:
        :param account_number:
        :param amount:
        :return: True if deposit, False if not
        """
        for x in self.customers:
            if x.ssn == ssn:
                for y in x.accounts:
                    if y.account_number == account_number:
                        y.deposit(amount)
                        return True
                print(f"Account {account_number} not found")
                return False

    def withdraw(self, ssn, account_number, amount):
        """
        withdraw amount from account
        :param ssn:
        :param account_number:
        :param amount:
        :return: True if withdrawn, False if not.
        """

        for x in self.customers:
            if x.ssn == ssn:
                for y in x.accounts:
                    if account_number == y.account_number:
                        y.withdraw(amount)
                        return True

                print(f"Account {account_number} not found!")
                return False

    def close_account(self, ssn, account_number):
        """
        Close account by ssn & account_number
        :param ssn:
        :param account_number:
        :return: account_number & which amount customer will receive
        """
        for x in self.customers:
            if x.ssn == ssn:
                for y in x.accounts:
                    if y.account_number == account_number:
                        x.close_account(account_number)
                        return f"Account {account_number} closed, you will receive {y.balance}"

                return f"Account: {account_number} not found!"

        return f"Customer with ssn {ssn} not found!"
