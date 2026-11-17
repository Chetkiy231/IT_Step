
# while True:
#     number = int(input("Введіть число від 1 до 9: "))
#     if 1 <= number <= 9:
#         break
#     print("Неправильне число. Спробуйте ще раз.")
#
# for i in range(1, 11):
#     print(i, "x", number, "=", i * number)
#
#2

# total = 0
# # count = 0
# # while True:
# #     grade = int(input("Введіть оцінку: "))
# #
# #     if grade == 0:
# #         break
# #
# #     count += 1
# #     total += grade
# #
# # average_grade = total / count
# # print(f"середня оцінка: {average_grade}")

#3

# while True:
#     operation = int(input("Выберите операцию: \n 1. сумма \n 2. разница \n 3. произведение \n 4. доля \n 5. выход \n"))
#     a = int(input("Введите первое число:"))
#     b = int(input("Введите второе число:"))
#     if operation == 1:
#         print("Результат: " , (a + b))
#     elif operation == 2:
#         print("Результат: " , (a - b))
#     elif operation == 3:
#         print("Результат: " , (a * b))
#     elif operation == 4:
#         if b == 0:
#             break
#         else:
#             print("Результат: " , (a / b))
#     elif operation == 5:
#         break
#     else:
#         print(" 🍏 ")


#4
# for i in range(3):
#  name = input("Введіть ім'я: ")
#  if name == "admin":
#     print("Це ім'я недоступне")
#  print(f"Учасник №{i+1}: {name}")