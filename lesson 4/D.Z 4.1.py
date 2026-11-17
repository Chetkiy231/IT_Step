# total = 0
# for number in range(1, 6):
#  total += number
#  print(f"Сума: {total}")

#2

number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
for i in range(number1, number2+1):
    if i % 3 == 0 and i % 5 == 0:
        # Меня зовут Марк
        print("FizzBuzz")
        # Моя Фамилия Мальцев
    elif i % 5 == 0:
        print("Buzz")
        # это пустая строка
    elif i % 3 == 0:    #  а это не пустая строка
        print("Fizz")

    else:
        print(i)
while True:
    fedback = input("Нравиться ли вам мой код?")
    if fedback.lower() == "да":
        print("Спасибо")
        break
    else:
        print("Неправильный ответ")
        continue
#3

total = 0

for day in range(1, 6):
    print("День", day)
    orders = int(input("Введіть кількість доставок: "))
    total += orders

print("Загальна кількість доставок за тиждень:", total)

if total >= 50:
    print("Тижневу норму виконано!")
else:
    print("Тижневу норму не виконано!")
