from bank import Bank
import bank

b = Bank()
bank.Bank()

def menu():
    print("""\nChoose your option:
    1. Add customer
    2. Get customer by ssn
    3. Get all customers
    4. Change customer name
    5. Remove customer
    6. Add account
    7. Close account
    8. Get account by ssn & account id
    9. Deposit/Withdraw 
    0. Exit
    """)
    answer = int(input("Enter your selection:\n"))

    if answer == 1:
        ssn = input("Input your personal number 10 digits: ")
        if len(ssn) != 10:
            print("I told you 10 digits!\n")
            ssn = input("Enter your social security number with 10 digits:\n")
            if len(ssn) != 10:
                print("Personal number invalid!")
                menu()
            else:
                first_name = input("Enter your first name: ").capitalize()
                last_name = input("Enter your last name: ").capitalize()
                b.add_customer(first_name, last_name, ssn)
                menu()
        else:
            first_name = input("Enter your first name: ").capitalize()
            last_name = input("Enter your last name: ").capitalize()
            b.add_customer(first_name, last_name, ssn)
            menu()

    elif answer == 2:
        ssn = input("Find customer by social security number (10 digits): ")
        if len(ssn) != 10:
            print("Wrong!\nI told you 10 digits..")
            ssn = input("Enter social security number with 10 digits:\n")
            if len(ssn) != 10:
                print("Social security number invalid!\n")
                menu()
            else:
                customer = b.get_customer_by_ssn(ssn)
                print(customer)
                menu()
        else:
            customer = b.get_customer_by_ssn(ssn)
            print(customer)
            menu()

    elif answer == 3:
        print("Customer list: ")
        print(b.get_all_customers())
        menu()

    elif answer == 4:
        ssn = input("Input customer ssn 10 digits: ")
        if len(ssn) != 10:
            print("Wrong input, pls enter ssn 10 digits")
            ssn = input("Last try, input customer ssn 10 digits: ")
            if len(ssn) != 10:
                menu()
            else:
                first_name = input("Enter customer first name: ").capitalize()
                last_name = input("Enter customer last name: ").capitalize()
                b.change_customer_name(ssn, first_name, last_name)
                menu()
        else:
            first_name = input("Enter customer first name: ").capitalize()
            last_name = input("Enter customer last name: ").capitalize()
            b.change_customer_name(ssn, first_name, last_name)
            menu()

    elif answer == 5:
        ssn = input("Input customer ssn (10 digits) you want to remove: ")
        if len(ssn) != 10:
            print("Wrong input, pls enter ssn 10 digits")
            ssn = input("Last try to remove customer, input ssn 10 digits: ")
            if len(ssn) != 10:
                menu()
            else:
                remove = b.remove_customer(ssn)
                print(remove)
                menu()
        else:
            remove = b.remove_customer(ssn)
            print(remove)
            menu()

    elif answer == 6:
        ssn = input("Enter customer ssn 10 digits: ")
        if len(ssn) != 10:
            print("Wrong input!\nLast try, pls enter ssn with 10 digits")
            ssn = input("Input ssn 10 digits: ")
            if len(ssn) != 10:
                menu()
            else:
                b.add_account(ssn)
                menu()

        else:
            b.add_account(ssn)
            menu()

    elif answer == 7:
        ssn = input("Enter customer ssn - 10 digits: ")
        if len(ssn) != 10:
            print("Wrong input!\nLast try, pls enter ssn with 10 digits")
            ssn = input("Input ssn 10 digits: ")
            if len(ssn) != 10:
                menu()
            else:
                account_number = input("Which account do you want to close: ")
                b.close_account(ssn, account_number)
                menu()
        else:
            account_number = input("Which account do you want to close: ")
            b.close_account(ssn, account_number)
            menu()

    elif answer == 8:
        ssn = input("Enter customer ssn - 10 digits: ")
        if len(ssn) != 10:
            print("Wrong input!\nLast try, pls enter ssn with 10 digits")
            ssn = input("Input ssn 10 digits: ")
            if len(ssn) != 10:
                menu()
            else:
                account_number = input("Which account do you want to find: ")
                b.get_account(ssn, account_number)
                menu()
        else:
            account_number = input("Which account do you want to find: ")
            b.get_account(ssn, account_number)
            menu()

    elif answer == 9:
        print("What would you like to do:\n1. Deposit\n2. Withdraw\n3. Back to main menu")
        try:
            option = int(input("Enter your option: "))
        except:
            print("Error, wrong input!")
            menu()

        while option == 1 or 2 or 3:
            if option == 1:
                ssn = input("Enter customer ssn - 10 digits: ")
                if len(ssn) != 10:
                    print("Wrong input!\nLast try, pls enter ssn with 10 digits")
                    ssn = input("Input ssn 10 digits: ")
                    if len(ssn) != 10:
                        menu()
                else:
                    try:
                        account_number = int(input("Which account number (4 digits) do you want deposit: "))
                        amount = float(input("Whats the amount you want to deposit: "))
                        b.deposit(ssn, account_number, amount)
                        break
                    except:
                        print("Wrong input!")
                        break

            elif option == 2:
                ssn = input("Enter customer ssn - 10 digits: ")
                if len(ssn) != 10:
                    print("Wrong input!\nLast try, pls enter ssn with 10 digits")
                    ssn = input("Input ssn 10 digits: ")
                    if len(ssn) != 10:
                        menu()
                else:
                    try:
                        account_number = int(input("Which account number (4 digits) do you want withdraw: "))
                        amount = float(input("Whats the amount you want to withdraw: "))
                        b.withdraw(ssn, account_number, amount)
                        break
                    except:
                        print("Wrong input!")
                        break

            elif option == 3:
                menu()
        menu()

    elif answer == 0:
        print("You have now left the building!")
    else:
        menu()


b.add_customer("Dejan", "Spasovic", "1234567890")
b.add_account("1234567890")
menu()