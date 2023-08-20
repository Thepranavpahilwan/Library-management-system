##Book issue

import psycopg2
from psycopg2 import errorcodes
from datetime import datetime,date,timedelta
import os

def clearscreen():
    print('\n' *5)
    
def SearchIssuedBooks():
    try:
        os.system('cls')
        conn=psycopg2.connect(user='postgres',password='pranav@123',host='localhost',database='postgres')
        conn.autocommit=True
        
        cur=conn.cursor()
        mno = input("Enter Member No to search issued book : ")
        query = ("SELECT * FROM issue where mno = %s")
        rec_srch = (mno,)
        cur.execute(query, rec_srch)
        Rec_count = 0
        for (Bno,Mno,d_o_issue,d_o_ret) in cur:
            Rec_count += 1
            print("=============================================================")
            print("1.Book Code : ", Bno)
            print("2.Member Code : ", Mno)
            print("3.Date of Issue : ", d_o_issue)
            print("4.Date of Return : ", d_o_ret)
            print("=============================================================")
        print(Rec_count, 'Record(s) found')
        if Rec_count == 0:
            input("Press any key continue")
            clearscreen()
            print(Rec_count, "Record(s) found")
        cur.close()
        conn.close()
        print("You have done it!")
    except psycopg2.Error as err:
        if(err.pgcode == errorcodes.SYNTAX_ERROR_OR_ACCESS_RULE_VIOLATION):
            print("Something is wrong with your user name or password")
        elif(err.pgcode == errorcodes.BAD_COPY_FILE_FORMAT):
            print("Database does not exist")
        else:
            print(err)
    

def issue_books():
    try:
         conn=psycopg2.connect(user='postgres',password='pranav@123',host='localhost',database='postgres')
         conn.autocommit = True
         
         cur=conn.cursor()
         
         bno=input('Enter Book code to issue : ')
         mno=input('Enter Member code : ')
         print("Enter Date Issue (Date/Month and Year separately) : ")
         DD = int(input("Enter Date : "))
         MM = int(input("Enter Month : "))
         YYYY = int(input("Enter Year : "))
         Date=date(YYYY,MM,DD)
         query='''insert into issue (bno,mno,d_o_issue) values (%s,%s,%s)'''
         val=(bno,mno,Date)
         cur.execute(query,val)
         
         cur.close()
         conn.close()
    except psycopg2.Error as err:
        if(err.pgcode == errorcodes.SYNTAX_ERROR_OR_ACCESS_RULE_VIOLATION):
            print("Something is wrong with your user name or password")
        elif(err.pgcode == errorcodes.BAD_COPY_FILE_FORMAT):
            print("Database does not exist")
        else:
            print(err)
    

def return_books():
    try:
        conn=psycopg2.connect(user='postgres',password='pranav@123',host='localhost',database='postgres')
        conn.autocommit = True
        
        cur=conn.cursor()
        
        bno=input('Enter the book code to be return : ')
        mno=input('Enter member code : ')
        return_date=date.today()
        
        query='''update issue set d_o_ret=%s where bno=%s and mno=%s'''
        val=(return_date,bno,mno)
        cur.execute(query,val)
        
        print("Return Successful")
        
        cur.close()
        conn.close()
    except psycopg2.Error as err:
        if(err.pgcode == errorcodes.SYNTAX_ERROR_OR_ACCESS_RULE_VIOLATION):
            print("Something is wrong with your user name or password")
        elif(err.pgcode == errorcodes.BAD_COPY_FILE_FORMAT):
            print("Database does not exist")
        else:
            print(err)