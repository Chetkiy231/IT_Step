from random import choice

# name = input("Введите ваше имя")
# age = int(input("Введите ваш возраст"))
# while age <= 0:
#     age = input("Введите натуральное число")
#     if age > 0:
#        break
# print("Привіт Джон. Тобі 36 років”")

#2
# days = 0
# total = 0
# goal = float(input("Цільова сума? "))
# while True:
#     daily_amount = float(input("Сьогоднішній вклад? "))
#     total += daily_amount
#     days += 1
#     if total >= goal:
#         break
# print(f"Мету досягнуто! У скарбничці {total} грн.\nПрошло дней:{days}")

#3
# metr = int(input("Введите длину в метрах"))
# yard = metr * 0.9144
# foot = metr * 0.3048
# print(f"Ваша длина в ярдах {yard:.2f}")
# print(f"Ваша длина в футах {foot:.2f}")
#
# while True:
#    choice = input("Хотите ли вы продолжить? да/нет")
#    if choice == "да":
#        metr = int(input("Введите длину в метрах"))
#        yard = metr * 0.9144
#        foot = metr * 0.3048
#        print(f"Ваша длина в ярдах {yard:.2f}")
#        print(f"Ваша длина в футах {foot:.2f}")
#    elif choice == "нет":
#        break
#    else:
#        print("Напищите да/нет")
#
# print("Досвидания")
 #5
total_items = 0
print("Додайте товари. Для завершення введіть'stop'.")
while True:
    item = input("Введіть товар: ")
    if item == "stop":
        break
    else:
        total_items += 1
print("Підрахунок завершений")

print(f"Всього товарів додано: {total_items}")
