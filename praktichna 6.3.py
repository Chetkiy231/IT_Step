# numbers =  [1, 8, -5, 9]
# print(numbers)

# for i in range(len(numbers)):
#     numbers[i] = numbers[i] * 3
# print(numbers)
# for i in range(len(numbers)):
#     if numbers[i] > 10:
#         numbers[i] = 0
# print(numbers)

#2
# numbers = []
#
# while True:
#     num = int(input("Введите число (-1 для завершения): "))
#     if num == -1:
#         break
#     numbers.append(num)
#
# if len(numbers) > 0:
#     print("Список:", numbers)
#     print("Количество:", len(numbers))
#     print("Сума:", sum(numbers))
#     print("Минимальное:", min(numbers))
#     print("Максимальное:", max(numbers))
# else:
#     print("Ошибка")

#3
# negative = []
# positive = []
# while True:
#     number = int(input("Введіть число (0 для завершення):" ))
#
#     if number > 0:
#         positive.append(number)
#     elif number == 0:
#         break
#     else:
#         negative.append(number)
#
# print("Додатні числа:", positive)
# print("Від'ємні числа:", negative)

#4
salaries = []
while True:
    salary = int(input("Введите зарплату сотрудника(-1 для завершения):"))

    if salary == -1:
        break
    else:
        salaries.append(salary)

prozent = int(input("На сколько % вы хотите повысить зарплату сотрудникам"))

if prozent <= 0:
        print("Жмотяра")
else:
    for i in range(len(salaries)):
        salaries[i] = salaries[i] / 100 * (100 + prozent)

print("Новые зарплаты",salaries)
