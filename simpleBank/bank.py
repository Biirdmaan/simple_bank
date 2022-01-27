import customer

class Bank:

    def __init__(self):
        self.customers = []
        self.name = "SEB"

    # needs update, does not work with ssn yet!
    def _load(self):
        """
        Load and strip customer information from a textfile.
        Customer information initialize to a customer object and append to customers[], if ssn does not exist.
        if customer_id already exist, customer gets a new customer_id
        :return:
        """
        for line in open("Customer_bank.txt").readlines():
            cust = line.strip().split(':')
            for x in self.customers:
                if cust[3] != x.ssn:
                    if int(cust[0]) != int(x.customer_id):
                        client = customer.Customer(cust[1], cust[2], cust[3], cust[0])
                        self.customers.append(client)
                        break
                    else:
                        client = customer.Customer(cust[1], cust[2], cust[3])
                        self.customers.append(client)
                        break
                else:
                    print("Customer already exist!")
        return self.customers

    def get_all_customers(self):
        """
        Get all customers
        :return: list of all customers, showing customer information: ssn, first_name and last_name
        """
        all_customers = []
        for customer in self.customers:
            details = customer.ssn, customer.first_name, customer.last_name
            all_customers.append(details)
        return all_customers
        # returner bankens alla kunder (personnummer & namn)

    def add_customer(self, first_name, last_name, ssn):
        """
        Create customer if ssn not used.
        :param first_name:
        :param last_name:
        :param ssn:
        :return:
        """
        client = customer.Customer(first_name, last_name, ssn)
        check = True
        if self.customers == []:
            self.customers.append(client)
            print(f"Customer {client.customer_id}: {client.first_name} {client.last_name} has been added!")
        else:
            for x in self.customers:
                if x.ssn != client.ssn:
                    self.customers.append(client)
                    print(f"Customer {client.customer_id}: {client.first_name} {client.last_name} has been added!")
                    break
                else:
                    check = False
                    print("SSN already exist!")
                    break
        return check

        # Skapar en ny kund om inte personnumret redan angetts.
        # Returner True om kunden har skapat & False om personnumret redan är upptaget.

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
                else:
                    print("Customer not found!")
                    break

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
                else:
                    print(f"Person with {ssn} is not a customer!")
                    return False


        # while ssn in self.customers:

        # Byter namn på kunden, returnerar True om namnet ändrats, False om kunde inte finns.
        pass

    def remove_customer(self, ssn):
        """
        Ta bort kund --> Alla konton tas bort
        Returneras: resultatet, en lista med alla information om alla konton som tagits bort & saldo som kunden ska
        få tillbaka
        :param ssn:
        :return:
        """
        return_balance = 0
        customer = []
        account_list = []
        for x in self.customers:
            if x.ssn == ssn:
                customer = self.customers.index(x)
                self.customers.pop(customer)

                for y in x.accounts:
                    return_balance = y.balance
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
        # Skapa ett konto, returnerar: kontonummer eller -1 om personnumret inte hittades

    def get_account(self, ssn, account_id):
        for customer in self.customers:
            if customer.ssn == ssn:
                print(customer.accounts[0])
                for x in customer.accounts[0]:
                    if x.account_id == account_id:
                        return x.show_account()
                    break
            else:
                return "Error, something went wrong"
        # Returnerar en string: kontonummer, saldo, kontotyp

    def deposit(self, ssn, account_number, amount):

        for x in self.customers:
            if x.ssn == ssn:
                for y in x.accounts:
                    if y.account_number == account_number:
                        y.deposit(amount)
                        return True
                    else:
                        print(f"Account {account_number} not found")
                        return False

        # Gör en insättning på kontot, returnerar: True om det gick igenom, False om ssn eller account_id inte hittades.

    def withdraw(self, ssn, account_number, amount):

        for x in self.customers:
            if x.ssn == ssn:
                for y in x.accounts:
                    if account_number == y.account_number:
                        y.withdraw(amount)
                        return True
                    else:
                        print(f"Account {account_number} not found!")
                        return False
        # Gör ett uttag från kontot, returnerar True --> ok, False --> gick åt helvete
        pass

    def close_account(self, ssn, account_number):
        for x in self.customers:
            if x.ssn == ssn:
                for y in x.accounts:
                    if y.account_number == account_number:
                        x.close_account(account_number)
                        return f"Account {account_number} closed, you will receive {y.balance}"
                    else:
                        return f"Account: {account_number} not found!"
            else:
                return f"Customer with ssn {ssn} not found!"

        # Avslutar ett konto
        # Returnerar en string: presentation av saldo som kunden ska ha.
