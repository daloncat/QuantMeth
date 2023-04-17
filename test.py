import csv
import time
from os import system, name

# Define the name of the file
FILENAME = "Products.csv"
TOTALSUM = 0
PASSWORD_FILE = "password.csv"

class Login:
    def __init__(self, filename):
        self.filename = filename

    def login_user(self):
        with open(self.filename, "r") as f:
            reader = csv.reader(f)
            username = input("Username: ")
            password = input("Password: ")
            for row in reader:
                if len(row) >= 2 and row[0] == username and row[1] == password:
                    print("Login successful!")
                    return True
            print("Incorrect username or password. Please try again.")
            return False

#This function is used to clear the console from previous interactions
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

clear()

# Create a login object
login = Login(PASSWORD_FILE)

# Call the login method
if not login.login_user():
    exit()
    
while True:
    print("\033[37m######################\nWelcome to our Shopping Simulator!\n######################\n\033[37m")
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
#    elif src==2:
#        searchCategory()
    elif src==3:
        listproducts()
    elif src == 0:
        print("Thank you for shopping with us <3")
        break
    else:
        print("\033[31mWrong Input!\033[0m")
