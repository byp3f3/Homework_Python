from math import *

print("Инженерный калькулятор")
print("1.Сложение")
print("2.Вычитание")
print("3.Умножение")
print("4.Деление")
print("5.Возведение в степень")
print("6.Квадратный корень")
print("7.Факториал")
print("8.Синус")
print("9.Косинус")
print("10.Тангенс")

while True:
    try:
        symbol = int(input("Выберите команду: "))
        break
    except ValueError:
        print("Что-то пошло не так, попробуйте снова")

if symbol >= 1 and symbol <= 4:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
elif symbol == 5:
    a = float(input("Введите число: "))
    b = float(input("Введите степень: "))
elif symbol >=5 and symbol <= 10:
    a = float(input("Введите число: "))
else:
    print("Что-то пошло не так, попробуйте снова")

match symbol:
    case 1:
        print("Сумма равна: ", a + b )
    case 2:
        print("Разность равна: ", a - b)
    case 3:
        print("Произведение равно: ", a * b)
    case 4:
        if b==0:
            print("На ноль делить нельзя!")
        else:
            print("Частное равно: ", a/b)
    case 5:
        print(a, "в степени ", b, "равно", a**b)
    case 6:
        print("Корень равен: ", sqrt(a))
    case 7:
        print("Факториал равен: ", factorial(a))
    case 8:
        print("Синус равен: ", sin(a))
    case 9:
        print("Косинус равен: ", cos(a))
    case 10:
        print("Тангенс равен: ", tan(a))


