from registration import Registration

class User(Registration):
    def __init__(self):
        Registration.__init__(self)

    def update_user_info(self, data):
        id_applicant = self.__if_applicant(data[-1])
        if id_applicant:
            self.cursor.execute(
                """
            UPDATE Applicant
            SET FirstName = ?, SecondName = ?, Middle_name = ?, Birth_date = ?
            WHERE Account_ID = ?
            """, (data))
        else:
            self.cursor.execute(
                """
                INSERT INTO Applicant
                (FirstName, SecondName, Middle_name, Birth_date, Account_ID)
                VALUES (?,?,?,?,?)
                """, (data))
        print("Ваши данные обновлены.")
        self.conn.commit()

    def __if_applicant(self, id_account):
        self.cursor.execute(
            """
            Select ID_Applicant
            FROM Applicant
            WHERE Account_ID = ?
            """, (id_account,))
        return [id for id in self.cursor]
    
    def __is_applicant(self, id_applicant):
        self.cursor.execute(
            """
            Select ID_Applicant
            FROM Applicant
            WHERE ID_Applicant = ?
            """, (id_applicant,))
        return self.cursor

    def create_application(self, data):
        if [applicant for applicant in self.__is_applicant(data[0])]:
            self.cursor.execute(
                """
                INSERT INTO Application
                (Applicant_ID, Specialty, Average_score, Status)
                VALUES (?,?,?,?)
                """, (data))
            self.conn.commit()
            print("Заявление было создано")
        else:
            print("Абитуриент не найден. Попробуйте снова.")

    def check_application(self, id_account):
        id_applicant = self.__if_applicant(id_account)
        if id_applicant:
            id_applicant = id_applicant[0][0]
        else:
            id_applicant = -1
        self.cursor.execute(
            f"Select ID_Application, Specialty, Status FROM Application WHERE Applicant_ID = {id_applicant}")
        return [application for application in self.cursor]