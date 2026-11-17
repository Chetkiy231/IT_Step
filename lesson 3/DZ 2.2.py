# clay = float(input("Введіть масу глини(кг): ")) Количство килограмм
# clay *= 1000 Это значит что Clay умножается на 1000
# clay_per_figure = 130 Количество на одну фигурку
# figures = clay // clay_per_figure Деление с округлением
# print(f"Можна зробити: {figures} фігурок")
#2
# fischer_1 = int(input("Сколько словил первый рыбак?"))
# fischer_2 = int(input("Сколько словил второй рыбак?"))
# fischer_3 = int(input("Сколько словил третий рыбак?"))
# average = (fischer_1 + fischer_2 + fischer_3)//3
# max_fish = max(fischer_1, fischer_2, fischer_3)
# print(f"Срений улов на рыбака:{average:.0f}")
# print("Самый большой улов", max_fish)
#3
# budget = int(input("Введите ваш бюджет:"))
# default = 150
# vip = 350
# vip_peoples = budget // vip
# default_peoples = budget // default
# print(f"Количество людей что могут пойти по обычному билету:{default_peoples:.0f}")
# print(f"Количество людей что могут пойти по vip билету:{vip_peoples:.0f}")
#4
amount=int(input("Введите бюджет"))
bills_500 = amount // 500
amount %= 500
bills_200 = amount // 200
amount %= 200
bills_100 = amount // 100
remainder = amount % 100
print(f" Купюри по 500: {bills_500} шт.")
print(f"Купюри по 200: {bills_200} шт.")
print(f"Купюри по 100: {bills_100} шт.")
print(f"Решта: {remainder} грн")


