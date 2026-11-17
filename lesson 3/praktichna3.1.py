# age = int(input("Введите свой возраст"))
# # if age >= 18 and age <= 65:
# #     print("Работо способный")
# # else:
# #     print("Не работо способный")
#2
# secret_login = input("Введите логин")
# secret_password =input("Введите пароль:")
# if secret_password == "OpenSesame123" and secret_login=="AliBaba":
#     print("Пароль и логин правильный")
# else:
#     print("Неверный логин или пароль")
#3
# price = int(input("Введите цену товара"))
# amount = int(input("Введите количество товаров"))
# age = int(input("Введите ваш возраст"))
# full_price = price * amount
# percentage = (full_price / 100 * 15)
# percentage_price = full_price - percentage
# if age < 18 or age > 65:
#     print("Цена за товар со скидкой по возрасту:" , percentage_price)
# else:
#     print("Цена за товар без скидки по возрасту:" , full_price)
#4
# age = 23
# has_license = "так"
# accidents = 0
# if age >= 18 and has_license == "так" and accidents == 0:
#    print("Оренда дозволена")
# else:
#    print("Оренда заборонена")
#5
# price = int(input("Введите суму покупки"))
# delivery_price = 120
# if price > 500:
#    delivery_price = 120
# elif price>= 500 and price <= 1000:
#      delivery_price = 114
# elif price > 1000 and price < 2000:
#      delivery_price = 96
# else:
#     delivery_price = 0
# total_price = price + delivery_price
# print(f"Общая сумма:{total_price:.0f}")
#6
amount = float(input("Введите сумму кредита: "))
years = float(input("Введите на сколько лет вы его берете: "))

if amount <= 10000:
  if years <= 3:
    rate = 8.0
  else:
    rate = 10.0
elif amount <= 50000:
  if years <= 3:
    rate = 12.0
  else:
    rate = 14.0
else:
  rate = 20.0

monthly_rate = rate / 100 / 12
months = int(years * 12)

if monthly_rate > 0:
  monthly_payment = amount * (monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
else:
  monthly_payment = amount / months

total_payment = monthly_payment * months

print("Расчёт по кредиту")
print(f"Сума кредиту: {amount:,.2f}")
print(f"Время по кредиту: {years} лет ({months} мес.)")
print(f"Процентная ставка: {rate}%")
print(f"Ежемесячный платеж: {monthly_payment:.2f}")
print(f"Сумма выплат: {total_payment:.2f}")

