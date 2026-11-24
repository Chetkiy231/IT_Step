# text = input("Введите текст")
# i = int(input("Введите индекс"))

# if i >= len(text):
#     print("Ошибка")
# else:
#     print(text[i])

#2
# text = input("Введіть рядок: ")
#
# start = int(input("Введіть початковий індекс: "))
# end = int(input("Введіть кінцевий індекс: "))
#
# segment = text[start:end]
#
# print(segment)

#3
# text = input("Введите текст")
# i = int(input("Введите индекс"))

# if i >= len(text):
#     print("Ошибка")
# else:
#     print(text[i])

#2
# text = input("Введіть рядок: ")
#
# start = int(input("Введіть початковий індекс: "))
# end = int(input("Введіть кінцевий індекс: "))
#
# segment = text[start:end]
#
# print(segment)

#3
s = input("Введите строку: ")
n = int(input("Введите число n: "))

if n < 0:
    print("Ошибка: число n не может быть отрицательным.")
elif n == 0:
    print("Первые n символов: ")
    print("Последние n символов: ")
elif n >= len(s):
    print("Первые n символов:", s)
    print("Последние n символов:", s)
else:
    first_n = s[:n]
    last_n = s[len(s) - n:]
    print("Первые n символов:", first_n)
    print("Последние n символов:", last_n)
