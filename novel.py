import time
import random
import sys
def clear_screen():
    print("\033[H\033[J")
def out_white(text):
    print("\033[37m{}".format(text), end='')
def out_red(text):
    print("\033[31m{}".format(text))
    out_white("")
def display_text(text, speed=0.04):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(speed)
    print()
def display_print(text):
    clear_screen()
    display_text(text)
    time.sleep(1)

def main():
    money = 0
    points = 0
    name = str(input("Перед началом игры введите свое имя:"))
    display_print("Добро пожаловать на борт «Muerte del mar», последнего пиратского корабля в мире.\n"
                  "Совсем скоро мы отправимся в очередное путешествие в поисках сокровищ.\n"
                  "Ветер несёт корабль к порту города Силард.")
    display_print("Силард – город, славящийся мудростью старейшин и пьянством молодежи.\n"
                  "Попасть сюда не так уж просто. ")
    display_print("Для начала ответьте на несколько вопросов, и может быть тогда Вам удастся пройти внутрь города.")

    display_print("Весит груша, нельзя скушать.\n")
    answer = str.capitalize(input("Ответ: "))
    while answer != 'Лампочка':
         out_red("Попробуйте ещё раз")
         answer = str.capitalize(input("Ответ: "))
         continue
    
    display_print("Зимой и летом одним цветом")
    answer = str.capitalize(input("Ответ: "))
    while answer != 'Елка':
         out_red("Попробуйте ещё раз")
         answer = str.capitalize(input("Ответ: "))
         continue
    
    display_print("Степень окисления кислорода.")
    answer = str.capitalize(input("Ответ(введите цифру): "))
    while answer != '2':
         out_red("Попробуйте ещё раз")
         answer = str.capitalize(input("Ответ: "))
         continue
    points = 15
    display_print(f"Количество очков жизни: {points}\n"
                  "Береги их, иначе тебе крышка")
    display_print("Вам удалось доказать свои умения. Город с радостью принимает Вас.")
    display_print("Кажется, в таверне «Gusta la cerveza» опять завязался спор на деньги.\n"
                  "Настоящий пират никогда не упустит прибыль. Вы решаете ввязаться в спор.")
    i = 0
    
    display_print("И так, Вам нужно выпить две из предложенных настоек. Какую выберете?")
    drinks = {"Видение": {"description": "Выглядит неплохо... Подождите, это что человеческий глаз.", 
                            "result": "Ваш желудок явно не скажет вам спасибо. Человеческие лаза не особо полезны для организма", "point_change": -4},
                    "Удача": {"description": "Бармен странно улыбался, когда наливал эту жижу.", 
                            "result": "Это обычный лимонад, видимо бармен вспоминал свое детство, когда наливал его ", "point_change": 5},
                    "Томатный сок":{ "description": "Кто знает, что это за красное недоразумение в стакане?", 
                                "result": "Похоже это и правда томатный сок. Иногда стоит доверять людям", "point_change":3},
                    "Бомба":{ "description": "Одно лишь название говорит само за себя", 
                            "result": "Стоило уточнить, многие ли выживали после этого напитка, до того, как его пить.", "point_change": -5},
                    "Бабушка":{ "description": "Звучит…необычно", 
                            "result": "Чай? В любом случае лучше уж так, чем отравление крайней тяжести.", "point_change": 1},
                    "Святая вода":{ "description": "Будем надеяться, что название совпадает с действительностью", 
                                "result": "Не совпадает…", "point_change": -7}   
        }
    
    while i<2:
        j = 0    
        for num, drink in enumerate(drinks):
            print(f"{num + 1}. {drink} - {drinks[drink]['description']}")
        print("Введите название напитка: ")
        choice =str.capitalize(input())
        for drink in drinks:
            if choice == drink:
                j+=1
        if j == 1:
            points = points + drinks[choice]['point_change']
            display_print(f"{drinks[choice]['result']}\n" "Количество очков жизни:"f"{points}") 
            del drinks[choice]
            i+=1
            money+=15
        else: 
             clear_screen()
             out_red("Попробуйте ещё раз")
             continue
    display_print("Теперь деньги Ваши.\n""Гроши: "f"{money}")
    
    display_print("Хотите продолжить путешествие?\n1.Да\n2.Нет")
    out = int(input())
    if out == 2:
         display_print("Прощайте. Надеюсь мы ещё встретимся")
         sys.exit(0)
    
    display_print("Следующий пункт назначения – Анкрид. Жители здесь славятся нескончаемой удачей и возможностью видеть будущее.\n"
                  "Проверим и ваши экстрасенсорные навыки.")
    a = random.randint(0,100)
    b = 0
    print("Угадайте число от 0 до 100")
    while b!=a:
        b = int(input())
        if b<a:
              print("Нужно больше")
        elif b>a:
             print("Нужно меньше")
    display_print("Вы угадали!")
    money+=50
    points+=20
    display_print("Гроши: "f"{money}\n""Количество очков жизни:"f"{points}")
    display_print("Возможно, быть гадалкой Ваше призвание. Подумайте о смене профессии на досуге.\n"
                  "Ну, а пока решайте продолжим ли мы путь?\n1.Да\n2.Нет") 
    out = int(input())
    if out == 2:
         display_print("Прощайте. Надеюсь мы ещё встретимся")
         sys.exit(0)
    display_print("До Вас дошли вести о сокровищах, находящихся в далеком восточном городе Лонфорд.\n"
                  "Мало, что известно об этом месте, кроме слухов об ужасных монстрах, что водятся там.\n"
                  "Но когда настоящих пиратов пугали сражения?")
    display_print("Стоило вашей ноге ступить за борт корабля, как на горизонте появились первые признаки жизни.\n"
                  "Очень недовольной вашим присутствием жизни.")
    monsters = ["Лагрима", "Миедо", "Голпир", "Муер"]
    i = 0
    while i<3:
        monst_name = random.choice(monsters)
        monst_health = 4
        display_print("На вас надвигается противник "f"{monst_name}")
        display_text("Что будете делать?\n1.Атаковать\n2.Защищаться")
        while monst_health>0:
            action = int(input())
            if action == 1:
                monst_health -=3
                if monst_health>0:
                    display_print("Монстр атакует")
                    points-=1
                    display_text("Количество очков жизни:"f"{points}")
                    display_text("Что будете делать?\n1.Атаковать\n2.Защищаться")
                    continue
                else: 
                    display_text("Монстр побежден")
                    i+=1
            elif action == 2:
                    display_print("Вам удалось уклониться от атаки монстра")
                    display_text("Что будете делать?\n1.Атаковать\n2.Защищаться")
                    continue
    display_print("Избавившись от преград на пути, Вы уверено входите в пещеру. Ваш взгляд встречается в двумя красными глазами дракона.\n"
                  "“Мы что в книжке?” проносится у Вас в голове")
    display_print("Вы без малейших раздумий достаете саблю. Сокровища важнее пары конечностей.")
    dragon_health = 25
    display_print("Что будете делать?\n1.Атаковать\n2.Защищаться")
    while dragon_health>0:
        action = int(input())
        if action == 1:
            dragon_health-=4
            if dragon_health>0:
                display_print("Дракон атакует")
                points-= random.randint(1,4)
                if points>0:
                    display_text("Количество очков жизни:"f"{points}")
                    display_text("Что будете делать?\n1.Атаковать\n2.Защищаться")
                    continue
                else:
                     display_print("Оу… Кажется, вы умерли… Видимо придется начать всё занаво…")
                     break
            else: 
                display_print("Дракон побежден")
        elif action == 2:
                display_print("Вам удалось уклониться от атаки монстра")
                display_text("Что будете делать?\n1.Атаковать\n2.Защищаться")
                continue
    money+=500
    display_print("Дракон падает без дыхания. Путь к огромному сундуку, стоящему в центре залы, открыт")
    display_text("Гроши: "f"{money}")
    display_text("На этом нам придется попрощаться.")

if __name__ == "__main__":
        main()