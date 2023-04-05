import csv
import os
os.system("cls")

# Define the name of the file
filename = "Products.csv"
totalsum = 0

def searchProduct():
    product = input("Which Product are you searching?\n")
    csv_file = csv.reader(open(filename), delimiter=';')
    found_product = False
    global totalsum

    for row in csv_file:
        if len(row) >= 2 and product == row[1]:
            print("Preis per kilogramm: ", row[2],  "\nPreis: ", row[3])
            preiskg = row[2]
            preis = row[3]
            relevance= input("Is the price per kilogramm relevant for this product? Y/N: ")
            if relevance == "Y":
                gewicht = input("Please input the amount you wish: ")
                summe = round(float(gewicht) * float(preiskg), 3)
                print(summe)
                totalsum = totalsum + summe
            found_product = True
    if not found_product:
        print("\033[31mProduct was not found in the database!\033[0m")
            

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
            
while True:
    print("######################\nWelcome to our Shopping Simulator!\n######################\n")
    print("\033[32mEnter 1 to search for Product Name:\033[0m")
#    print("\033[32mEnter 2 to search for a category:\033[0m")
    print("\033[32mEnter 0 to quit.\033[0m")
    print("\033[33mCurrent price of all products:\033[0m ", totalsum)

    src=int(input("Enter here: "))

    if src==1:
        searchProduct()
#    elif src==2:
#        searchCategory()
    elif src == 0:
        print("Thank you for shopping with us <3")
        break
    else:
        print("\033[31mWrong Input!\033[0m")
