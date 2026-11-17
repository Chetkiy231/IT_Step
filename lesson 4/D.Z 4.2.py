# while True:
#         grade = int(input("Введіть оцінку за іспит (від 1 до 5): "))
#
#         if grade == 1:
#             print("Дуже погано")
#             break
#         elif grade == 2:
#             print("Погано")
#             break
#         elif grade == 3:
#             print("Задовільно")
#             break
#         elif grade == 4:
#             print("Добре")
#             break
#         elif grade == 5:
#             print("Чудово")
#             break
#         else:
#             print("Помилка! Число має бути від 1 до 5.")

#2
# yes_count = 0
# no_count = 0
#
# print("Опитування: «Чи потрібно будувати більше дитячих садків у вашому місті?»")
# print("Вводьте 'так', 'ні' (або 'стоп' для завершення):")
#
# while True:
#     answer = input("Ваша відповідь: ")
#
#     if answer == "стоп":
#         break
#     elif answer == "так":
#         yes_count += 1
#     elif answer == "ні":
#         no_count += 1
#     else:
#         print("Помилка! Невідоме слово. Будь ласка, введіть 'так', 'ні' або 'стоп'.")
#
# print("Кількість 'так':", yes_count)
# print("Кількість 'ні':", no_count)
#
# if yes_count > no_count:
#     print("Висновок: голосів 'так' більше.")
# elif no_count > yes_count:
#     print("Висновок: голосів 'ні' більше.")
# else:
#     print("Висновок: кількість голосів 'так' і 'ні' однакова.")

#3
print("Введіть число (0 для виходу):")

while True:
    num = int(input("Ваше число: "))

    if num == 0:
        print("Вихід з програми.")
        break
    else:
       print(f"Ви ввели: {num}")
