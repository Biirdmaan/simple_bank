
class Bank():
    name = "SEB"

    def _load(self):
        f = open("customer_bank.txt", "r")
        print(f)


seb = Bank()

seb._load()
