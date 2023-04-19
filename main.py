import hashlib
import csv
import time
from os import system, name

# Define the name of the file
FILENAME = "Products.csv"
TOTALSUM = 0

class User:
    def __init__(self, username, password_hash):
        self.username = username
        self.password_hash = password_hash
        
    def check_password(self, password):
        return self.password_hash == hashlib.sha256(password.encode('utf-8')).hexdigest()

class LoginSystem:
    def __init__(self, filename):
        self.users = []
        self.filename = filename
        self.load_users()
    
    def register(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
        self.users.append(User(username, password_hash))
        self.save_users()
        print("Registration successful!")
    
    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        for user in self.users:
            if user.username == username and user.check_password(password):
                print("Login successful!")
                return True
        print("Incorrect username or password.")
        return False
    
    def load_users(self):
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    username, password_hash = line.strip().split(',')
                    self.users.append(User(username, password_hash))
        except FileNotFoundError:
            pass
    
    def save_users(self):
        with open(self.filename, 'w') as file:
            for user in self.users:
                file.write(f"{user.username},{user.password_hash}\n")

def clear():
	# for windows
	if name == 'nt':
		_ = system('cls')
	# for mac and linux(here, os.name is 'posix')
	else:
		_ = system('clear')

def searchProduct():
    product = input("Which Product are you searching?\n")
    csv_file = csv.reader(open(FILENAME), delimiter=';')
    found_product = False
    global TOTALSUM

    for row in csv_file:
        if len(row) >= 2 and product == row[1]:
            print("Preis per kilogramm: ", row[2],  "\nPreis: ", row[3])
            preiskg = row[2]
            preis = row[3]
            if preis == "0":
                gewicht = input("How many kilogramms do you want to buy? ")
                summe = round(float(gewicht) * float(preiskg), 3)
                print(summe)
                TOTALSUM = TOTALSUM + summe
            else:
                summe = round(float(preis), 3)
                print("Total price for your product: ", summe)
                TOTALSUM = TOTALSUM + summe
            found_product = True
    if not found_product:
        print("\033[31mProduct was not found in the database!\033[0m")

def listproducts():
    print("We have following products in stock:")

    csv_file = csv.reader(open(FILENAME), delimiter=';')
    for row in csv_file:
        print("\033[35m", row[1], "\033[35m")
    time.sleep(2.5)

#def searchCategory():
#    product = input("Nach welcher Kategorie möchtest du ausschau halten?\n")
#    csv_file = csv.reader(open(filename))
#    found_category = False
#
#    for row in csv_file:
#        if product==row[0]:
#            print(row)
#            found_category = True
#
#    if not found_category:
#        print("\033[31mFehler\033[0m")

login_system = LoginSystem("password.txt")
clear()
while True:
    action = input("Do you want to register or login? ")
    if action == "register":
        login_system.register()
    elif action == "login":
        if login_system.login():
            # do something after login
            clear()
            print("Login Succesful!")
            while True:
                print("\033[37m############################################\033[0m")
                print("Welcome to our shopping simulator!")
                print("\033[37m############################################\033[0m")
                print("\033[32mEnter 1 to search for Product Name:\033[0m")
#    print("\033[32mEnter 2 to search for a category:\033[0m")
                print("\033[32mEnter 3 to get a list of all items.\033[0m")
                print("\033[32mEnter 0 to quit.\033[0m")
                print("\033[33mCurrent price of all products:\033[0m ", TOTALSUM)

                src_str = input("Enter here: ")
                try:
                    src = int(src_str)
                except ValueError:
                    print("\033[31mInvalid input! Please enter a number.\033[0m")
                    continue
                if src==1:
                    searchProduct()
#               elif src==2:
#                   searchCategory()
                elif src==3:
                    listproducts()
                elif src == 0:
                    print("Thank you for shopping with us <3")
                    break
                else:
                    print("\033[31mWrong Input!\033[0m")
            break
    else:
        print("Invalid action. Please enter 'register' or 'login'.")
