import sqlite3 as sq
from database import create_data

class Registration:
    def __init__(self):
        create_data()
        self.conn = sq.connect('.\database.db')
        self.cursor = self.conn.cursor()

    def __if_login(self, login):
            self.cursor.execute(
                """
                Select Login
                FROM Accounts
                WHERE Login = ?
                """, (login,))
            return self.cursor
    
    def loggin(self, login, password):
        self.cursor.execute(
            """
            Select ID_Account, Employee_password
            FROM Accounts
            WHERE Login = ? AND Password = ?
            """, (login, password))
        user = [user for user in self.cursor]
        return user

    def create_account(self, login, password, emp_password):
        if not [user for user in self.__if_login(login)]:
            self.cursor.execute(
                """
                INSERT INTO Accounts
                (Login, Password, Employee_password)
                VALUES (?,?,?)
                """, (login, password, emp_password))
            print("Вы зарегестрировались.")
            self.conn.commit()
        else:
            print("Вы уже зарегестрированы!")