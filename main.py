import os
from user import User
from employee import Employee

def main():
    (lambda: os.system('cls'))()
    print("=============Мечты=============\n1. Войти\n2. Зарегестрироваться\n3. Выйти")
    while True:
        choice = input("Выбирете номер команды: ")
        match choice:
            case "1": 
                print("Введите логин и пароль:")
                login = input("Логин: ")
                password = input("Пароль: ")
                object = User()
                user_id = object.loggin(login, password)
                if user_id:
                    if user_id[0][1]:
                        employee_interface(Employee(), user_id[0][0])
                    else:
                        user_interface(object, user_id[0][0])
                else:
                    print("Логин или пароль не верный. Попробуйте ещё раз")
            case "2":
                print("Введите логин и пароль:")
                login = input("Логин: ")
                password = input("Пароль: ")
                unique_key = input("Введите код доступа сотрудника, либо оставте поле пустым: ")
                if unique_key == "123":
                    object = Employee()
                    object.create_account(login, password, 1)
                else:
                    object = User()
                    object.create_account(login, password, 0)
            case "3":
                break
            case _:
                print("Кажется Вы ошиблись. Попробуйте снова.")

def user_interface(object, user_id):
    (lambda: os.system('cls'))()
    print("КАБИНЕТ ПОЛЬЗОВАТЕЛЯ")
    print("1. Изменить свои данные‌\n2. Создать заявление‌\n3. Посмотреть статус заявления‌\n4. Выйти")
    while True:
        choice = input("Выбирете номер команды: ")
        match choice:
            case "1":
                object.update_user_info([
                    input("Введите Ваше имя: "),
                    input("Введите Вашу фамилию: "),
                    input("Введите Ваше отчество(можно оставить пустым): "),
                    input("Введите Вашу дату рождения: "),
                    user_id
                    ])
            case "2":
                try:
                    application = object.create_application(
                        [int(input("Введите свой ID: ")),
                         input("Введите название выбранной специальности: "),
                         float(input("Введите свой средний балл: ")),
                         "Создано"])
                except (ValueError):
                    print ("Вы ввели неправильное значение. Попробуйте еще раз.")
            case "3":
                applications = object.check_application(user_id)
                if applications:
                    for application in applications:
                        print(f"Заявление № {application[0]}\nСпециальность: {application[1]}\nСтатус: {application[2]}")
                else:
                    print("У Вас нет активных заявлений.")
            case "4":
                main()
            case _:
                print("Кажется Вы ошиблись. Попробуйте снова.")


def employee_interface(object, user_id):
    (lambda: os.system('cls'))()
    print("КАБИНЕТ СОТРУДНИКА")
    print("1. Изменить свои данные\n2. Создать заявление\n3. Изменить заявление\n4. Изменить статус заявления\n5. Удалить заявление\n6. Войти в кабинет администратора\n7. Выйти")
    while True:
        choice = input("Выбирете номер команды: ")
        match choice:
            case "1":
                object.update_employee_info([
                    input("Введите Ваше имя: "),
                    input("Введите Вашу фамилию: "),
                    input("Введите Ваше отчество(можно оставить пустым): "),
                    user_id
                ])
            case "2":
                try:
                    object.create_application(
                            [int(input("Введите ID абитуриента: ")),
                            input("Введите название выбранной специальности: "),
                            float(input("Введите средний балл: ")),
                            input("Введите статус заявления: ")
                            ])
                except (ValueError):
                    print ("Вы ввели неправильное значение. Попробуйте еще раз.")
            case "3":
                try:
                    object.change_application(
                        [int(input("Введите ID абитуриента: ")),
                            input("Введите название выбранной специальности: "),
                            float(input("Введите средний балл: ")),
                            input("Введите статус заявления: "),
                            int(input("Введите ID заявления: "))]
                    )
                except (ValueError):
                    print ("Вы ввели неправильное значение. Попробуйте еще раз.")
            case "4":
                try:
                    object.change_application_status(
                        [input("Введите новый статус заявления: "), 
                         int(input("Введите ID заявления: "))
                         ])
                except (ValueError):
                    print("Вы ввели неправильное значение. Попробуйте еще раз.")
            case "5":
                try:
                    object._del_application(int(input("Введите ID заявления, которое хотите удалить: ")))
                except (ValueError):
                    print("Вы ввели неправильное значение.")
            case "6":
                admin_password = input("Введите ключ доступа администратора: ")
                if admin_password == "124":
                    admin_interface(Employee(), [0][0])
            case "7":
                main()
            case _:
                print("Кажется Вы ошиблись. Попробуйте снова.")

def admin_interface(object, user_id):
    (lambda: os.system('cls'))()
    print("КАБИНЕТ АДМИНИСТРАТОРА")
    print("1. Изменить свои данные\n2. Изменить данные пользователя\n3. Удалить пользователя\n4. Выйти")
    choice = input("Выбирете номер команды: ")
    while True:
        match choice:
            case "1":
                object.update_employee_info([
                    input("Введите Ваше имя: "),
                    input("Введите Вашу фамилию: "),
                    input("Введите Ваше отчество(можно оставить пустым): "),
                    user_id
                ])
            case "2":
                print("Чьи данные Вы хотите изменить?\n1.Абитуриента\n2.Сотрудника\n3.Выйти")
                change = int(input())
                match change:
                    case 1:
                        try:
                            object.update_user_info([
                            input("Введите имя: "),
                            input("Введите фамилию: "),
                            input("Введите отчество(можно оставить пустым): "),
                            input("Введите дату рождения: "),
                            int(input("Введите ID абитуриента: "))
                            ])
                        except (ValueError):
                            print ("Вы ввели неправильное значение. Попробуйте еще раз.")
                    case 2:
                        try:
                            object.update_employee_info([
                            input("Введите имя: "),
                            input("Введите фамилию: "),
                            input("Введите отчество(можно оставить пустым): "),
                            int(input("Введите ID сотрудника: "))
                            ])
                        except (ValueError):
                            print ("Вы ввели неправильное значение. Попробуйте еще раз.")
                    case 3:
                        admin_interface(Employee(), [0][0])
                    case _:
                        print("Вы ввели неправильное значение.")
            case "3":
                try:
                    object._del_account(int(input("Введите ID пользователя, которого хотите удалить: ")))
                except (ValueError):
                    print("Вы ввели неправильное значение.")
            case "4":
                main()
if __name__ == '__main__':
    main()
