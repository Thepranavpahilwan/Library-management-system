
import Database
import Book
import Menulib


# Database.CreateDatabase()
# Database.CreateTable()

while True:
    Book.clearscreen()
    print("\t\t\t Library Management\n")
    print("=====================================================================")
    print("1. Book Management")
    print("2. Members Management")
    print("3. Issue/Return Book")
    print("4. Exit")
    choice = int(input("Enter Choice between 1 to 4 -------> : "))
    
    if choice == 1:
        Menulib.Menubook()
    elif choice == 2:
        Menulib.MenuMember()
    elif choice == 3:
        Menulib.MenuIssue()
    elif choice == 4:
        break
    else:
        print("Wrong Choice.....Enter Your Choice again")
        x = input("Press any key to continue")



