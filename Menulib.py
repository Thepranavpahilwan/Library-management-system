


import Book
import Issue
import Member

def Menubook():
    while True:
        # Book.clearscreen()
        print("\t\t\t Book Record Management\n")
        print("==========================================================")
        print("1. Add Book Record")
        print("2. Search Book Record")
        print("3. Delete Book Record")
        print("4. Update Book Record")
        print("5. Return to Main Menu")
        print("==========================================================")
        choice = int(input("Enter Choice between 1 to 5 -------> : "))
        if choice == 1:
            Book.Insert_Data()
        elif choice == 2:
            Book.Search_Book()
        elif choice == 3:
            Book.Delete_Book()
        elif choice == 4:
            Book.Update_Book()
        elif choice == 5:
            return
        else:
            print("Wrong Choice.....Enter Your Choice again")
            x = input("Enter any key to continue")
            
def MenuIssue():
    while True:
        print("\t\t\t Member Record Management\n")
        print("==========================================================")
        print("1. Issue Book")
        print("2. Search Issue Book Record")
        print("3. Return Issued Book")
        print("4. Return to Main Menu")
        print("==========================================================")
        choice = int(input("Enter Choice between 1 to 4 ------> : "))
        if choice == 1:
            Issue.issue_books()
        elif choice == 2:
            Issue.SearchIssuedBooks()
        elif choice == 3:
            Issue.return_books()
        elif choice == 4:
            return
        else:
            print("Wrong Choice.....Enter Your Choice again")
            x = input("Enter any key to continue")


def MenuMember():
    while True:
        
        print("\t\t\t Member Record Management\n")
        print("==========================================================")
        print("1. Add Member Record")
        print("2. Search Member Record")
        print("3. Delete Member Record")
        print("4. Update Member Record")
        print("5. Return to Main Menu")
        print("==========================================================")
        choice = int(input("Enter Choice between 1 to 5 ------> : "))
        if choice == 1:
            Member.Insert_member()
        elif choice == 2:
            Member.Search_member()
        elif choice == 3:
            Member.delete_member()
        elif choice == 4:
            Member.update_member()
        elif choice == 5:
            return
        else:
            print("Wrong Choice.....Enter Your Choice again")
            x = input("Enter any key to continue")