# age=int(input("Введите ваш возраст"))
# age2=int(input("Введите возраст второго человека"))
# age3=int(input("Введите возраст 3 человека"))
# if age<12:
#    ticket_price=80
# elif age>=12 and age<=65:
#     ticket_price=200
# else:
#     ticket_price=120
# if age2<12:
#    ticket_price2=80
# elif age2>=12 and age2<=65:
#     ticket_price2=200
# else:
#     ticket_price2=120
# if age3<12:
#    ticket_price3=80
# elif age3>=12 and age3<=65:
#     ticket_price3=200
# else:
#     ticket_price3=120
# total = ticket_price + ticket_price2 + ticket_price3
# print(f"Цена за билеты:{total}\nХорошего Дня!")
#3
# month = input("Введите месяц")
# day = input("Введите сегодняшнее число")
# if month == "Январь" and day == "1":
#     print("Новый год")
# elif month == "Февраль" and day == "14":
#     print("День святого Валентина")
# elif month == "Декабрь" and day == "25":
#     print("Рождество")
# elif month == "Апрель" and day == "1":
#     print("День смеха")
# else:
#     print("Обычный день")
#5
product = input("Введіть назву товару: ")
if product == "алкоголь" or product == "тютюн":
    age = int(input("Введіть ваш вік: "))

    if age >= 18:
        print("Дозволено до продажу")
    else:
        print("Заборонено до продажу")

elif product == "ліки":

    prescription = input("У вас є рецепт від лікаря? ")

    if prescription == "так":
        print("Дозволено до продажу")
    else:
        print("Заборонено до продажу")

else:
    print("Дозволено до продажу")


