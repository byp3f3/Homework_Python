import sqlite3 as sq

def create_data():
    with sq.connect('.\database.db') as con:
        cur = con.cursor()

        cur.execute( 
            """
            CREATE TABLE IF NOT EXISTS Accounts (
            ID_Account INTEGER PRIMARY KEY AUTOINCREMENT,
            Login VARCHAR(30) UNIQUE  NOT NULL,
            Password VARCHAR(30) NOT NULL,
            Employee_password INTEGER)
            """)

        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS Employee (
            ID_Employee INTEGER PRIMARY KEY AUTOINCREMENT,
            Account_ID INTEGER UNIQUE NOT NULL,
            FirstName VARCHAR(50) NOT NULL,
            SecondName VARCHAR(50) NOT NULL,
            Middle_name VARCHAR(50),
            FOREIGN KEY (Account_ID) REFERENCES Accounts(ID_Account))
            """)

        cur.execute(  
            """
            CREATE TABLE IF NOT EXISTS Applicant (
            ID_Applicant INTEGER PRIMARY KEY AUTOINCREMENT,
            Account_ID INTEGER UNIQUE NOT NULL,
            FirstName VARCHAR(50) NOT NULL,
            SecondName VARCHAR(50) NOT NULL,
            Middle_name VARCHAR(50),
            Birth_date date NOT NULL,
            FOREIGN KEY (Account_ID) REFERENCES Accounts(ID_Account))
            """)

        cur.execute(
            """
            CREATE TABLE  IF NOT EXISTS Application (
            ID_Application INTEGER PRIMARY KEY AUTOINCREMENT,
            Applicant_ID INTEGER NOT NULL,
            Specialty VARCHAR(100) NOT NULL, 
            Average_score REAL NOT NULL, 
            Status VARCHAR(50) NOT NULL DEFAULT "Создано",
            FOREIGN KEY (Applicant_ID) REFERENCES Clients(ID_Applicant))
            """)
    