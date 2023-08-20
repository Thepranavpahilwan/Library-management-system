
import psycopg2
from psycopg2 import errorcodes
from datetime import datetime,date,timedelta
import os
import platform

def clearscreen():
    if platform.system()=='Windows':
        print(os.system('cls'))
        
def Insert_Data():
    try:
        conn=psycopg2.connect(user='postgres',password='pranav@123',host='localhost',database='postgres')
        conn.autocommit=True
        
        cur=conn.cursor()
        
        bcode=input('Enter Book Code : ')
        bname=input('Enter Book Name : ')
        auth=input('Enter Book Author Name : ')
        price=input('Enter Book Price : ')
        publisher=input('Enter Publisher Name : ')
        qty=input('Enter Quantity purchased : ')
        print("Enter Date of Purchase (Date/Month and Year seperately) : ")

        DD = int(input("Enter Date : "))
        MM = int(input("Enter Month : "))
        YYYY = int(input("Enter Year : "))
        query=''' Insert Into Bookrecord values (%s,%s,%s,%s,%s,%s,%s)'''
        data=(bcode,bname,auth,price,publisher,qty,date(YYYY,MM,DD))
        cur.execute(query,data)
        print('Insert successful')
        cur.close()
        conn.close()
    except psycopg2.Error as err:
        if(err.pgcode == errorcodes.SYNTAX_ERROR_OR_ACCESS_RULE_VIOLATION):
            print("Something is wrong with your user name or password")
        elif(err.pgcode == errorcodes.BAD_COPY_FILE_FORMAT):
            print("Database does not exist")
        else:
            print(err)
        
        

            
def Delete_Book():
    try:
        conn=psycopg2.connect(user='postgres',password='pranav@123',host='localhost',database='postgres')
        conn.autocommit=True
    
        cur=conn.cursor()
    
        bcodes = input("Enter Book Code of Book to be deleted from the Library : ")
        query = '''DELETE FROM Bookrecord WHERE Bcode = %s'''
        del_rec = (bcodes,)
        cur.execute(query, del_rec)
        cur.close()
        conn.close()
        print(cur.rowcount, "Record(s) Deleted Successfully.")
    except psycopg2.Error as err:
        if(err.pgcode == errorcodes.SYNTAX_ERROR_OR_ACCESS_RULE_VIOLATION):
            print("Something is wrong with your user name or password")
        elif(err.pgcode == errorcodes.BAD_COPY_FILE_FORMAT):
            print("Database does not exist")
        else:
            print(err)
    
     
def Search_Book():
    try:
        conn=psycopg2.connect(user='postgres',password='pranav@123',host='localhost',database='postgres')
        conn.autocommit = True
        
        cur=conn.cursor()
        
        bno=input('Enter Book Code to be Searched from the Library : ')
        query = '''SELECT * FROM Bookrecord where bcode = %s'''
        rec_srch = (bno,)
        cur.execute(query,rec_srch)
        
        print('done')
        Rec_count=0
        for (Bcode, Bname, Auth, price, publisher, qty, Date_of_Purchase) in cur:
            Rec_count += 1
            print("=============================================================")
            print("Book Code : ", Bcode)
            print("Book Name : ", Bname)
            print("Author of Book : ", Auth)
            print("Price of Book : ", price)
            print("Publisher : ", publisher)
            print("Total Quantity in Hand : ", qty)
            print("Purchased On : ", Date_of_Purchase)
            print("=============================================================")
            if Rec_count%2 == 0:
                input("Press any key continue")
                clearscreen()
                print(Rec_count, "Record(s) found")
        cur.close()
        conn.close()
    except psycopg2.Error as err:
        if(err.pgcode == errorcodes.SYNTAX_ERROR_OR_ACCESS_RULE_VIOLATION):
            print("Something is wrong with your user name or password")
        elif(err.pgcode == errorcodes.BAD_COPY_FILE_FORMAT):
            print("Database does not exist")
        else:
            print(err)
    
    

def Update_Book():
    try:
        conn=psycopg2.connect(user='postgres',password='pranav@123',host='localhost',database='postgres')
        conn.autocommit = True
        
        cur=conn.cursor()
        
        bno=input('Enter Book Code of Book to be Updated from the Library : ')
        query = ("SELECT * FROM BookRecord WHERE Bcode = %s ")
        rec_srch = (bno,)
        cur.execute(query,rec_srch)
       
        print('#done---------------------------------------------#')
        print("Enter new data")
        bname = input("Enter Book Name : ")
        Auth = input("Enter Book Author's Name : ")
        price = int(input("Enter Book Price : "))
        publisher = input("Enter Publisher of Book : ")
        qty = int(input("Enter Quantity purchased : "))
        print("Enter Date of Purchase (Date/Month and Year seperately) : ")
        DD = int(input("Enter Date : "))
        MM = int(input("Enter Month : "))
        YY = int(input("Enter Year : "))
        Date_of_Purchase = date(YY,MM,DD)
        Qry = ("UPDATE Bookrecord SET bname=%s, Auth=%s, price=%s, publisher=%s, qty=%s, Date_of_Purchase=%s WHERE bcode=%s")
        data = (bname, Auth, price, publisher, qty, Date_of_Purchase, bno)
        cur.execute(Qry,data)
        cur.close()
        conn.close()
        print(cur.rowcount, "Record(s) Updated Successfully.")
    except psycopg2.Error as err:
        if(err.pgcode == errorcodes.SYNTAX_ERROR_OR_ACCESS_RULE_VIOLATION):
            print("Something is wrong with your user name or password")
        elif(err.pgcode == errorcodes.BAD_COPY_FILE_FORMAT):
            print("Database does not exist")
        else:
            print(err)
    
        
    
           

