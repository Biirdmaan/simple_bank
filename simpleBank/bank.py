
class Bank:

    def _load(self):
        # Läser in en textfil och befolkar listan som ska innehålla kunderna
        pass

    def get_customers(self):
        # returner bankens alla kunder (personnummer & namn)
        pass

    def add_customer(self, first_name, last_name, ssn):
        # Skapar en ny kund om inte personnumret redan angetts.
        # Returner True om kunden har skapat & False om personnumret redan är upptaget.
        pass

    def get_customer(self, ssn):
        # Returnerar information om kunden inklusive dess konton.
        # Ordningen på returen är: Kundens förnamn, efternamn, ssn, dess konto (sort by account id?)
        pass

    def change_customer_name(self, first_name, last_name, ssn):
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