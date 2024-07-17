def menu():  # for displaying menu
    print("-" * 24, "Address Book", "-" * 24)
    print("1. Add Contact\n2. Edit Contact\n3. Delete Contact\n4. View Contacts\n5. Search Address Book\n6. Exit\n")

def add():  # adding contacts
    if length <= 99:
        fn = input("\nEnter First Name: ")
        ln = input("Enter Last Name: ")
        ad = input("Enter Address: ")
        cn = input("Enter Contact Number: ")
        if fn == "" or ln == "" or ad == "" or cn == "":
            print("Please enter a character.")
            add()
        elif (fn in first_name) and (ln in last_name) and (ad in address) and (cn in contact_number):
            print("You've already entered that contact. Try again.")
            add()
        else:
            first_name.append(fn)
            last_name.append(ln)
            address.append(ad)
            contact_number.append(cn)
            print("\nAdded successfully!\n")
    else:
        print("\nThe Address Book has 100 entries already. Sorry.\n")

def edit():  # editing contacts
    print("\nCONTACTS")
    view()  # users can see their contacts to edit
    entry = int(input("\nWhat entry number to edit? "))
    if entry < 1 or entry > length:
        print("Invalid entry number. Please try again.")
        edit()
    else:
        fne = input("Enter First Name: ")
        lne = input("Enter Last Name: ")
        ade = input("Enter Address: ")
        cne = input("Enter Contact Number: ")
        first_name[entry - 1], last_name[entry - 1], address[entry - 1], contact_number[entry - 1] = fne, lne, ade, cne
        print("\nEdited successfully!\n")

def delete():  # deleting contacts
    print("\nCONTACTS")
    view()  # users can see their contacts to delete
    entryDel = int(input("\nWhat entry number to delete? "))
    if entryDel < 1 or entryDel > length:
        print("Invalid entry number. Please try again.")
        delete()
    else:
        first_name.pop(entryDel - 1)
        last_name.pop(entryDel - 1)
        address.pop(entryDel - 1)
        contact_number.pop(entryDel - 1)
        print("\nDeleted successfully!\n")

def view():  # viewing contacts
    if length > 0:
        print("\nCONTACTS")
        for i in range(length):
            print(str(i + 1) + ". Name:", first_name[i], last_name[i], "\n   Address: ", address[i], "\n   Contact Number: ", contact_number[i])
    else:
        print("\nYou have no contacts.")

def search(): #search contacts
    def searchContacts():
        print("\nSEARCH RESULTS")
        x = 0
        for i in range(length):
            if searchfor.lower() in searchby[i].lower():  # check if search term is in the current item
                x = 1
                print(str(i + 1) + ". Name:", first_name[i], last_name[i], "\n   Address: ", address[i],
                      "\n   Contact Number: ", contact_number[i])
        return x

    while True:
        search = input("\nSearch by:\n    a. first name?\n    b. last name?\n    c. address?\n    d. contact number?\n\nAnswer (a-d): ")
        search = search.lower()
        if search == "a":
            searchfor = input("Search for (first name): ")
            searchby = first_name
        elif search == "b":
            searchfor = input("Search for (last name): ")
            searchby = last_name
        elif search == "c":
            searchfor = input("Search for (address): ")
            searchby = address
        elif search == "d":
            searchfor = input("Search for (contact number): ")
            searchby = contact_number
        else:
            print("a, b, c, or d only. Try again.")
            continue

        x = searchContacts()
        if x == 0:
            print("No results found for '" + searchfor + "'\n")
        break


first_name = []
last_name = []
address = []
contact_number = []

while True:
    menu()
    opt = input("Choose an option: ")
    if opt == "1" or opt == "2" or opt == "3" or opt == "4" or opt == "5" or opt == "6":
        opt = int(opt)
        if opt == 1:
            length = len(first_name)  # to determine how many entries are currently in the program
            add()
        elif opt == 2:
            length = len(first_name)  # to determine how many entries are currently in the program
            edit()
        elif opt == 3:
            length = len(first_name)  # to determine how many entries are currently in the program
            delete()
        elif opt == 4:
            length = len(first_name)  # to determine how many entries are currently in the program
            view()
        elif opt == 5:
            length = len(first_name)  # to determine how many entries are currently in the program
            search()
        elif opt == 6:
            break
    else:
        print("Options 1-6 only. Try again.")
        continue