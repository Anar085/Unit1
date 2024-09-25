

banner = """⠀⠀⠀⠀⠀⠀
       ⣠⡤⢤⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣾⣿⠂⠀⣇⣀⠀⠀⠀
⠀⠀⠀⣠⠖⠉⠀⠀⠀⠀⠀⠉⠙⢢
⠀⠀⣴⠃⠀⢰⣮⠿⠿⢍⣻⡒⣶⠃
⠀⢀⡿⡄⠀⠈⠳⢤⣀⠀⠀⠉⠁⠀
⠀⠈⢗⠝⡢⣄⡀⠀⠀⠉⠓⠢⡀⠀
⠀⠀⠀⠙⠮⢔⣝⣗⠦⣄⠀⠀⠘⡆
⠀⠀⠀⡀⠀⠀⠀⠉⢳⠬⡇⠀⠀⡱
⢀⡶⡾⠉⠒⠢⠤⠤⠼⠟⠁⠀⢠⡇
⠺⣍⡣⣄⣀⣀⣀⠀⠀⣠⣤⣴⡟⠁
⠀⠈⠙⠲⠵⢽⡹⡇⠀⢹⠟⠉⠀⠀
⠀⠀⠀⠀⠀⢸⡦⣷⢖⣾⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠛⠓⠋⠁⠀⠀⠀⠀
Welcome to the Currency Converter!
These are the available currencies for converting: 
USD - Us dollars 
AZN - Azerbaijani manat
JPY - Japanese yen
EUR - European euro

Only typing options are: AZN, USD, EUR, JPY!
To exit the program, please type "stop".
"""
end_code = "\033[00m"
bk = "\33[0;102m"
black = "\33[1;30m"
blue = "\33[1;34m"
red = "\33[1;31m"
bkr = "\33[0;101m	"
bkb = "\33[0;104m"

print(f"{bk}{black}{banner}")

exchange_rates = {
    "USD": {"EUR": 0.9, "JPY": 140, "AZN": 1.7},
    "EUR": {"USD": 1.1, "JPY": 155, "AZN": 1.88},
    "JPY": {"USD": 0.007, "EUR": 0.0064, "AZN": 0.012},
    "AZN": {"USD": 0.59, "EUR": 0.53, "JPY": 82.85}
}
options = ["AZN", "EUR", "USD", "JPY"]
terminate = True
while terminate:
    from_currency_unsafe = input("Enter the currency to convert from: ")
    if from_currency_unsafe == "stop":
        exit("Thank you for using our services! ")
    elif from_currency_unsafe not in options:
        print("Invalid currency, please try again.")
        print("Only typing options are: AZN, USD, EUR, JPY ")
    else:
        terminate = False
terminate2 = True
while terminate2:
    to_currency_unsafe = input("Enter the currency to convert to: ")
    if to_currency_unsafe == "stop":
        exit("Thank you for using our services! ")
    elif to_currency_unsafe not in options:
        print("Invalid currency, please try again.")
        print("Only typing options are: AZN, USD, EUR, JPY ")
    else:
        terminate2 = False
terminate3 = True
while terminate3:
    amount_original = input("Enter the amount to convert: ")
    if amount_original == "uniqueschool2024":
        import csv

        banner1 = """

                     Secret  Password  Manager
                   __________                                 
                 .'----------`.                              
                 | .--------. |                             
                 | |########| |       __________              
                 | |########| |      /__________\             
        .--------| `--------' |------|    --=-- |-------------.
        |        `----,-.-----'      |o ======  |             | 
        |       ______|_|_______     |__________|             | 
        |      /  %%%%%%%%%%%%  \                             | 
        |     /  %%%%%%%%%%%%%%  \                            | 
        |     ^^^^^^^^^^^^^^^^^^^^                            | 
        +-----------------------------------------------------+
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

        WELCOME TO THE PASSWORD MANAGER !!!
        Available operations:
        1. View the passwords of applications (type "view")
        2. Add a new application and its password (type "add")
        3. Remove an existing application and its password (type "remove")
        4. Edit an existing application and its password (type "edit")
        5. Stop the application (type "stop")
Here is the list of software applications for only teachers:
        """

        print(f"{bkb}{black}{banner1}")
        with open('c:/Users/User/PycharmProjects/Unit 1/database.csv', 'r') as f:
            data = f.readlines()

        lst = []
        catalog = {}
        for item in data:
            remove_new_line = item.strip()
            app, password = remove_new_line.split(',')
            catalog[app] = password
            app = list(app)
            app.reverse()
            app = "".join(app)
            lst.append(app)

        for x in range(len(lst)):
            print(f"{x + 1}.{lst[x]}")


        def inputvalidation(num: str):
            s = 0
            for letter in num:
                if letter in '0123456789':
                    s += 1
                    if len(num) == s:
                        num = int(num)
                        if num <= len(lst) and num > 0:
                            return False
                        else:
                            print(f"{num} is not a valid number for this list, please try again.")
                            return True
                            break
                    else:
                        print(f"{num} is not a valid number for this list, please try again.")
                        return True
                        break

                else:
                    print(f"{num} is not a valid number for this list, please try again.")
                    return True
                    break

        terminate = True
        while terminate:
            app_unsafe = input(f"Which operation you want to perform: ")
            app_requested = app_unsafe

            if app_requested == "stop":
                terminate = False
            elif app_requested == "add":
                end_code = "\033[00m"
                red = "\33[0;31m"
                term = True
                while term:
                    app2 = input("What application do you want to add? ")
                    if app2 == "stop":
                        exit(f"{bkr}{black}Thank you for using our services!{end_code}")
                    app2 = list(app2)
                    app2.reverse()
                    app2 = "".join(app2)
                    if app2 in catalog:
                        print(f" Application is already in the password manager, please try a new one: ")
                    else:
                        term = False
                pass2 = input("Set a strong password: ")
                if pass2 == "stop":
                    exit(f"{bkr}{black}Thank you for using our services!{end_code}")
                pass2 = list(pass2)
                pass2.reverse()
                pass2 = "".join(pass2)
                print("Operation completed")
                with open('database.csv', 'a') as f:
                    f.writelines([f"\n{str(app2)} ,{str(pass2)}\n"])
            elif app_requested == "remove":
                for i, item in enumerate(data):
                    clean_item = item.strip('\n')
                    app, password = clean_item.split(',')
                tr3 = True
                while tr3:
                    delete = input("Enter the number of app: ")
                    if delete == "stop":
                        exit(f"{bkr}{black}Thank you for using our services!{end_code}")
                    num=delete
                    m1 = inputvalidation(num)
                    if m1 == False:
                        tr3 = False
                    else:
                        tr3 = True
                delete = int(num)
                new_data = []
                tr4 = True
                while tr4:
                    if delete <= len(data) and delete > 0:
                        for i, item in enumerate(data):
                            if i + 1 != delete:
                                new_data.append(item)
                        tr4 = False
                        print("Operation completed")
                    else:
                        print("Invalid number, please try again.")
                        break
                with open('c:/Users/User/PycharmProjects/Unit 1/database.csv', 'w') as f:
                    f.writelines(new_data)
                for item in new_data:
                    remove_new_line1 = item.strip()
                    app1, pass1 = remove_new_line1.split(',')
                    app1 = list(app1)
                    app1.reverse()
                    app1 = "".join(app1)
                    pass1 = list(pass1)
                    pass1.reverse()
                    pass1 = "".join(pass1)
                    catalog[app1] = pass1
            elif app_requested == "view":
                tr = True
                while tr:
                    num = input("Enter the number of the application: ")
                    if num == "stop":
                        exit(f"{bkr}{black}Thank you for using our services!{end_code}")
                    m=inputvalidation(num)
                    if m==False:
                        tr=False
                    else:
                        tr=True
                num=int(num)
                a1 = lst[num - 1]
                a = a1

                a = list(a)
                a.reverse()
                a = "".join(a)
                p = catalog[a]
                p = list(p)
                p.reverse()
                p = "".join(p)
                print(f"Password of the {a1} is {p}")
            elif app_requested == "edit":
                tr4 = True
                while tr4:
                    number = input("Enter the number of the application to edit: ")
                    if number == "stop":
                        exit(f"{bkr}{black}Thank you for using our services!{end_code}")
                    num=number
                    m3 = inputvalidation(num)
                    if m3 == False:
                        tr4 = False
                    else:
                        tr4 = True
                number = int(num)
                new_app = input("Enter the new application name: ")
                if new_app == "stop":
                    exit(f"{bkr}{black}Thank you for using our services!{end_code}")
                new_password = input("Enter the new password: ")
                if new_password == "stop":
                    exit(f"{bkr}{black}Thank you for using our services!{end_code}")
                a2 = list(new_app)
                a2.reverse()
                a2 = "".join(a2)
                p2 = list(new_password)
                p2.reverse()
                p2 = "".join(p2)
                data[number - 1] = f"{a2},{p2}\n"
                with open('database.csv', 'w') as f:
                    f.writelines(data)

                catalog[a2] = p2
                r = lst[number - 1]
                r = list(r)
                r.reverse()
                r = "".join(r)
                del catalog[r]

                print("Operation completed.")


            else:
                print("Incorrect operation, please try again.")
        exit(f"{bkr}{black}Thank you for using the services!{end_code}")
    elif amount_original == "stop":
        exit(f"{bkr}{black}Thank you for using our services!{end_code}")
    else:
        if "." in amount_original:
            number = amount_original.count(".")
            if number != 1:
                print("Invalid amount, please enter a number or a number with a single decimal point.")
            else:
                parts = amount_original.split(".")
                if not all(part.isdigit() for part in parts):
                    print("Invalid amount, please enter a number or a number with a single decimal point.")
                else:
                    terminate3 = False
        elif not amount_original.isdigit():
            print("Invalid amount, please enter a number or a number with a single decimal point.")
        else:
            terminate3 = False

amount_original = float(amount_original)
converted_amount = amount_original * exchange_rates[from_currency_unsafe][to_currency_unsafe]
print(f"{amount_original} {from_currency_unsafe} is equal to {converted_amount} {to_currency_unsafe}{end_code}")
print(f"{bkr}{black}Thank you for using our services! {end_code}")
