while True:
    print("\nМеню:")
    print("1. Вибрати піцу")
    print("2. Вихід")

    choice = input("Оберіть опцію: ")

    if choice == "1":
        pizza_name = input("Введіть назву піци: ")
        quantity = int(input("Введіть кількість: "))
        print(f"Замовлено {pizza_name}, {quantity} шт")
    elif choice == "2":
        print("До побачення!")
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")
MENU = {
    "Маргарита": 150,
    "Пепероні": 180,
    "Чотири сири": 200
}

while True:
    print("\nМеню:")
    print("1. Вибрати піцу")
    print("2. Вихід")

    choice = input("Оберіть опцію: ")

    if choice == "1":
        print("\nДоступні піци:")
        for name, price in MENU.items():
            print(f"{name} – {price} грн")

        pizza_name = input("\nВведіть назву піци: ").strip().capitalize()

        if pizza_name not in MENU:
            print("Помилка: такої піци немає в меню.")
            continue

        quantity = int(input("Введіть кількість: "))
        print(f"Замовлено {pizza_name}, {quantity} шт")

    elif choice == "2":
        print("До побачення!")
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")
