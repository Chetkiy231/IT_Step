# minutes = int(input("Введите минуты"))
# # if minutes >= 0:
# #     print("Cекунды:",minutes*60)
# # else:
# #     print("Невозможно ввести отрицательное число")
#2
# secret_password =input("Введите пароль:")
# if secret_password == "OpenSesame123":
#     print("Пароль правильный")
# else:
#     print("Неверный пароль")
#3
# metr = int(input("Введите метры"))
# choose = input("Введите еденицу измерения")
# if choose == "Сантиметр":
#     print("Ответ в сантиметрах:",metr*100)
# elif choose== "Дециметр":
#      print("Ответ в Дециметре:", metr*10)
# else:
#     print("Невозможно обчислить в такой единице измерения")
#4
# answer = input("Відповідь на Велике Питання Життя, Всесвіту і Всього Іншого:")
# if answer == "42":
#  print("Правильно")
# elif answer == "сорок два":
#  print("Правильно")
# elif answer == "42":
#  print("Правильно")
# elif answer == "сорок-два":
#  print("Правильно")
# else:
#  print("Не правильно")
#5
# grade = int(input("Введіть оцінку: "))
# if grade == 2:
#    print("Незадовільно")
# elif grade == 3:
#    print("Задовільно")
# elif grade == 4:
#    print("Добре")
# elif grade == 5:
#    print("Відмінно")
# else:
#    print("Оцінка має бути від 2 до 5")
#6
price = float(input("Введите цену одной пиццы"))
amount = int(input("Введите количество пицц"))
budget = float(input("Введите ваш бюджет"))
total_cost = price * amount
reminder = budget - total_cost
if budget >= total_cost:
  print(f"Денег хватает\nОбщая стоимость:{total_cost:.2f}")
  print(f"Остаток денег:{reminder:.2f}")
else:
    print("Не хватает денег")


