#Member

import psycopg2
from psycopg2 import errorcodes
from datetime import datetime,date,timedelta
import os

def clearscreen():
    print('\n' * 5)
    
def Insert_member():
    try:
        conn=conn=psycopg2.connect(user='postgres',password='pranav@123',host='localhost',database='postgres')
        conn.autocommit=True
        
        cur=conn.cursor()
        
        mno = input("Enter Member Code : ")
        mname = input("Enter Member Name : ")
        print("Enter Date of Membership (Date/Month and Year) seperately) : ")
        DD = int(input("Enter Date : "))
        MM = int(input("Enter Month : "))
        YYYY = int(input("Enter Year : "))
        addr = input("Enter Member Address : ")
        mob = int(input("Enter Member Mobile No. : "))
        Qry = ("INSERT INTO Member VALUES(%s, %s, %s, %s, %s)")
        data = (mno,mname,date(YYYY,MM,DD),addr,mob)
        cur.execute(Qry, data)
        cur.close()
        conn.close()
        print("Record Inserted.")
        
    except psycopg2.Error as err:
        if(err.pgcode == errorcodes.SYNTAX_ERROR_OR_ACCESS_RULE_VIOLATION):
            print("Something is wrong with your user name or password")
        elif(err.pgcode == errorcodes.BAD_COPY_FILE_FORMAT):
            print("Database does not exist")
        else:
            print(err)
            
def delete_member():
    try:
        conn=psycopg2.connect(user='postgres',password='pranav@123',host='localhost',database='postgres')
    
        conn.autocommit=True
    
        cur=conn.cursor()
        del_mem=input('write the member code to be delete : ')
        query='''delete from member where mno = %s'''
        tbd=(del_mem)
        cur.execute(query,tbd)
        print(cur.rowcount ,'records deleted successful')
        
    except psycopg2.Error as err:
        if(err.pgcode == errorcodes.SYNTAX_ERROR_OR_ACCESS_RULE_VIOLATION):
            print("Something is wrong with your user name or password")
        elif(err.pgcode == errorcodes.BAD_COPY_FILE_FORMAT):
            print("Database does not exist")
        else:
            print(err)

def update_member():
    try:
        conn=psycopg2.connect(user='postgres',password='pranav@123',host='localhost',database='postgres')
    
        conn.autocommit= True
        cur=conn.cursor()
    
        upd_mem=input('writr memeber code to be update : ')
    
        print('new details')
        mname=input('member name')
        print("Enter Date of Membership (Date/Month and Year) seperately) : ")
        DD = int(input("Enter Date : "))
        MM = int(input("Enter Month : "))
        YYYY = int(input("Enter Year : "))
        date_of_membership=date(YYYY,MM,DD)
        addr = input("Enter Member Address : ")
        mob = int(input("Enter Member Mobile No. : "))
    
        query='''update member set mname=%s ,date_of_membership=%s,addr=%s,mob=%s where mno=%s '''
        data=(mname,date_of_membership,addr,mob,upd_mem)
        cur.execute(query,data)
    
        print(cur.rowcount,'records updated successfully')
    
    except psycopg2.Error as err:
        if(err.pgcode == errorcodes.SYNTAX_ERROR_OR_ACCESS_RULE_VIOLATION):
            print("Something is wrong with your user name or password")
        elif(err.pgcode == errorcodes.BAD_COPY_FILE_FORMAT):
            print("Database does not exist")
        else:
            print(err)
            
def Search_member():
    try:
        conn=psycopg2.connect(user='postgres',password='pranav@123',host='localhost',database='postgres')
        conn.autocommit=True
        
        cur=conn.cursor()
        
        srch_mem=input('write member code to be search : ')
        qry='''select * from member where mno=%s'''
        search_code=srch_mem
        cur.execute(qry,search_code)
        
        Rec_count=0
        for (mno, mname, date_of_membership, addr, mob) in cur:
            Rec_count += 1
            print("=============================================================")
            print("member Code : ", mno)
            print("member Name : ", mname)
            print("data of membership : ", date_of_membership)
            print("address : ", addr)
            print("mob : ", mob)
            print("=============================================================")
        print(Rec_count, 'Record(s) found')
        if Rec_count == 0: 
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
        
        