import customer


class Bank:

    def __init__(self):
        self.customers = []
        self.name = "SEB"

    """ 
    _load metoden:
    Reads textfile and add customer from textfile to customer list - customers[] 
    if customer_id (textfile) != customer_id (in customers[]), customer adds to customer[] with same id as textfile
    else customer gets a new id. 
    """
    def _load(self):
        for line in open("Customer_bank.txt").readlines():
            cust = line.strip().split(':')
            for x in self.customers:
                if int(cust[0]) != int(x.customer_id):
                    client = customer.Customer(cust[1], cust[2], cust[3], cust[0])
                    self.customers.append(client)
                    break
                else:
                    client = customer.Customer(cust[1], cust[2], cust[3])
                    self.customers.append(client)
                    break
        return self.customers

    # get all customers, return [] of all customers with ssn, first_name, last_name
    def get_customers(self):
        all_customers = []
        for customer in self.customers:
            details = customer.ssn, customer.last_name, customer.last_name
            all_customers.append(details)
        return all_customers
        # returner bankens alla kunder (personnummer & namn)

    """
    Behövs justeras, skapar samma customer 2 ggr, varför? 
    """
    def add_customer(self, first_name, last_name, ssn):
        client = customer.Customer(first_name, last_name, ssn)
        print(client)
        check = True
        if self.customers == []:
            self.customers.append(client)
            print(f"Customer {client.customer_id}: {client.first_name} {client.last_name} has been added!")
        else:
            for x in self.customers:
                if x.ssn != ssn:
                    self.customers.append(client)
                    print(f"Customer {client.customer_id}: {client.first_name} {client.last_name} has been added!")
                    break
                else:
                    check = False
                    break
        return check

        # Skapar en ny kund om inte personnumret redan angetts.
        # Returner True om kunden har skapat & False om personnumret redan är upptaget.

    def get_customer(self, ssn):

        for x in self.customers:
            try:
                if ssn == x.ssn:
                    return x.show_customer()
                else:
                    print("Customer not found!")
            except:
                print("Error, no customer found in customer list")

        # Returnerar information om kunden inklusive dess konton.
        # Ordningen på returen är: Kundens förnamn, efternamn, ssn, dess konto (sort by account id?)
        pass

    def change_customer_name(self, ssn, first_name=None, last_name=None):
        # while ssn in self.customers:

        # Byter namn på kunden, returnerar True om namnet ändrats, False om kunde inte finns.
        pass

    def remove_customer(self, ssn):
        # Ta bort kund --> Alla konton tas bort
        # Returneras: resultatet, en lista med alla information om alla konton som tagits bort & saldo som kunden ska
        # få tillbaka
        pass

    def add_account(self, ssn):
        # Skapa ett konto, returnerar: kontonummer eller -1 om personnumret inte hittades
        pass

    def get_account(self, ssn, account_id):
        # Returnerar en string: kontonummer, saldo, kontotyp
        pass

    def deposit(self, ssn, account_id, amount):
        # Gör en insättning på kontot, returnerar: True om det gick igenom, False om ssn eller account_id inte hittades.
        pass

    def withdraw(self, ssn, account_id, amount):
        # Gör ett uttag från kontot, returnerar True --> ok, False --> gick åt helvete
        pass

    def close_account(self, ssn, account_id):
        # Avslutar ett konto
        # Returnerar en string: presentation av saldo som kunden ska ha.
        pass

    def get_all_transactions_by_pnr_acc_nr(self, ssn, account_number):
        # --------------------VG---------------------
        # Returnerar: alla transaktioner som en kund har gjort med ett specifikt konto
        # returnerar -1 ifall kontot inte finns.
        pass


a = Bank()
a.add_customer("Dejan", "Spasovic", 198805293311)
print(a.customers)

print(a.get_customers(198805293311))