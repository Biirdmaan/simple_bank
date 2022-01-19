import itertools
#import account


class Customer():
    customer_id = itertools.count()

    def __init__(self, first_name, last_name, ssn):
        self.first_name = first_name
        self.last_name = last_name
        self.ssn = ssn
        self.customer_id = next(self.customer_id)
        print(self.customer_id)
        self.customer_id = 11110 + self.customer_id
        print(self.customer_id)


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

    # Show customer information, social security number, first & last name,
    def show_customer(self):
        return self.ssn, self.first_name, self.last_name


a = Customer("Erik", "Eriksson", 197503033341)
b = Customer("Anna", "Svensson", 198706301212)

print(a.first_name)
a.change_first_name("David")
print(a.first_name)
