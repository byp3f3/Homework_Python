from user import User

class Employee(User):
    def __init__(self):
        User.__init__(self)

    def update_employee_info(self, data):
        id_applicant = self.__is_applicant_account(data[-1])
        if id_applicant:
            self.cursor.execute(
                """
            UPDATE Employee
            SET FirstName = ?, SecondName = ?, Middle_name = ?
            WHERE Account_ID = ?
            """, (data))
        else:
            self.cursor.execute(
                """
                INSERT INTO Employee
                (FirstName, SecondName, Middle_name, Account_ID)
                VALUES (?,?,?,?)
                """, (data))
        print("Данные сотрудника были обновлены.")
        self.conn.commit()

    def __is_applicant_account(self, id_account):
        self.cursor.execute(
            """
            Select ID_Employee
            FROM Employee
            WHERE Account_ID = ?
            """, (id_account,))
        return [id for id in self.cursor]
    
    def __is_application(self, id_application):

        self.cursor.execute(
            """
            Select ID_Application
            FROM Application
            WHERE ID_Application = ?
            """, (id_application,))
        return self.cursor

    def change_application(self, data):
        id_application = self.__is_application(data[-1])
        if id_application:
            self.cursor.execute(
                """
                UPDATE Application
                SET Applicant_ID = ?, Specialty = ?, Average_score = ?, Status = ? 
                WHERE ID_Application = ?
                """, (data))
            self.conn.commit()
            print("Заявление изменено.")
        else:
            print("Заявление не существует.")
    
    def change_application_status(self, data):
            self.cursor.execute(
                """
                UPDATE Application
                SET Status = ?
                WHERE ID_Application = ?
                """, (data))
            self.conn.commit()
            print("Статус заявления изменен.")
        

    def _del_application(self, id_application):
        self.cursor.execute(
            """
            DELETE FROM Application
            WHERE ID_Application = ?
            """, (id_application,))
        self.conn.commit()
        print("Заявление удалено.")
    
    def _del_account(self, id_account):
        self.cursor.execute(
            """
            DELETE FROM Accounts
            WHERE ID_Account = ?
            """, (id_account,))
        self.conn.commit()
        print("Пользователь удалён.")
