#num1 = input("перше число: ")
#num2 = input("друге число: ")
#num1 = float(num1)
#num2 = float(num2)
#sum = num1 * num2
#average = sum / 2
#print("Сума:", sum)
#print("Середнє:", average)
#2
# uah = float(input("Гривны:"))
# usd = round((uah / 45),2)
# print("Доллар:", usd)
#3
# price = input('Цена:')
# percent = float(input("Процент скидки")) / 100
# price = float(price)
# total = price-(price*percent)
# print("К оплате", total)
#4
minutes_slow = int(input("Количество минут медленно:"))
minutes_fast = int(input("Количество минут быстро:"))
minutes_sprint = int(input("Количество минут бег:"))
slow = 3
fast = 4.5
sprint = 9
calories_slow = slow * minutes_slow
calories_fast = fast * minutes_fast
calories_sprint = sprint * minutes_sprint
calories_sum =(calories_fast+calories_slow+calories_sprint)
print("Соженные калории:", calories_sum)
print("Соженные калории медленно:", calories_slow)
print("Соженные калории быстро:", calories_fast)
print("Соженные калории бег:", calories_sprint)