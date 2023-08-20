# Database and Tables creation

import psycopg2


def CreateDatabase():
    conn=psycopg2.connect(user='postgres',host='localhost',password='pranav@123')
    conn.autocommit = True

    cur=conn.cursor()
    query1=''' Drop database if exists LibraryM'''
    query2=''' Create Database LibraryM''';
    cur.execute(query1)
    cur.execute(query2)
    print('Database created...')
    
    cur.close()
    conn.close()
    
def CreateTable():
    conn=psycopg2.connect(user='postgres',host='localhost',password='pranav@123',database='postgres')
    conn.autocommit=True
    
    cur=conn.cursor()
    cur.execute("DROP TABLE IF EXISTS Bookrecord")
    cur.execute("CREATE TABLE IF NOT EXISTS Bookrecord(Bcode integer primary key, Bname varchar(20), Auth varchar(20), Price integer, Publisher varchar(20), Qty integer, Date_of_Purchase Date)")
    cur.execute("DROP TABLE IF EXISTS Member")
    cur.execute("CREATE TABLE IF NOT EXISTS Member(Mno integer primary key, Mname varchar(20), Date_of_Membership Date, Addr varchar(24), Mob varchar(10))")
    cur.execute("DROP TABLE IF EXISTS Issue")
    cur.execute("CREATE TABLE IF NOT EXISTS Issue(Bno integer, Mno integer, d_o_issue Date, d_o_ret Date)")
    print('''Tables Created.....''')
    cur.close()
    conn.close() 

