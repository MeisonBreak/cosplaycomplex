# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: WarehouseMini
def show_menu():
    print("\n--- Меню управления складом ---")
    print("1. Показать товары")
    print("2. Добавить товар")
    print("3. Отчет по остаткам")
    print("4. Выход")
    choice = input("Выберите действие: ")
    if choice == "1":
        for item in inventory.values():
            print(f"{item['id']}: {item['name']} (Остаток: {item['qty']})")
    elif choice == "2":
        name = input("Название товара: ")
        qty = int(input("Количество: "))
        inventory[name] = {'id': len(inventory) + 1, 'name': name, 'qty': qty}
        print(f"Товар '{name}' добавлен.")
    elif choice == "3":
        total_value = sum(item['qty'] * item.get('price', 0) for item in inventory.values())
        low_stock = [item for item in inventory.values() if item['qty'] < 10]
        print(f"Общая стоимость: {total_value} руб.")
        if low_stock:
            print("Предупреждение! Низкий остаток у товаров:")
            for item in low_stock:
                print(f"- {item['name']} ({item['qty']})")
    elif choice == "4":
        print("Выход из системы.")
