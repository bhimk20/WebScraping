import pandas as pd
import mysql.connector
from mysql.connector import Error

#creating database
def create_database():
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='5684')

    mycursor = mydb.cursor()

    mycursor.execute("Create database NSEIndia")

    mycursor.execute("show databases")

    for db in mycursor:
        print(db)
    mycursor.close()
    mydb.close()

#connecting database
def connect_database():
    try:
        conn = mysql.connector.connect(host='localhost', database='NSEIndia', user='root', passwd='5684')

        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database", record)
            cursor.close()
        return conn
    except Error as e:
        print("Error while connecting to MySQL", e)

#create tables for csv
def create_tables(conn):
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS EquitySegment;')
    print("Creating tables...")
    cursor.execute('''
        CREATE TABLE EquitySegment(
            Symbol varchar(255), 
            CompanyName varchar(255),
            Series varchar(255), 
            ListingDate varchar(255), 
            PaidupValue int, 
            MarketLot int, 
            ISINNumber varchar(255), 
            FaceValue int
        )
    ''')


    cursor.execute('DROP TABLE IF EXISTS BhavCopy;')
    cursor.execute('''
        CREATE TABLE BhavCopy(
            Symbol varchar(255), 
            Series varchar(255), 
            Open float(20),
            High float(20),
            Low float(20),
            Close float(20),
            Last float(20),
            PrevClose float(20),
            TOTTRDQTY float(20),
            TOTTRDVAL double,
            TimeStamp varchar(255),
            TotalTrades int,
            ISIN varchar(255)
        )
    ''')
    cursor.execute("SHOW TABLES")
    print("Following tables created!!!")
    for tb in cursor:
        print(tb)
    cursor.close()

#inserting values to db
def insert_values(conn):
    cursor = conn.cursor()

    df = pd.read_csv("file1.csv", index_col=0 ,delimiter=',')
    print("Inserting equity segment values into database...")
    for index, row in df.iterrows():
        query = "INSERT INTO EquitySegment VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(query, tuple(row))
        conn.commit()
    print("Values inserted!!!")

    df = pd.read_csv("file2.csv", index_col=0, delimiter=',')
    print("Inserting BhavCopy values into database...")
    for index, row in df.iterrows():
        query = "INSERT INTO BhavCopy VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(query, tuple(row))
        conn.commit()
    print("Values inserted!!!")
    cursor.close()


#For creating a data base.
#create_database()

conn = connect_database()
create_tables(conn)
insert_values(conn)
conn.close()