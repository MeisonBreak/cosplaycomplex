# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: WarehouseMini
def demo():
    """Показывает основной пользовательский сценарий."""
    # 1. Создаём товары
    warehouse = WarehouseMini()
    warehouse.add("Электроника", "Ноутбук", 15000, 10)
    warehouse.add("Электроника", "Мышь", 500, 100)
    warehouse.add("Одежда", "Рубашка", 2500, 25)
    warehouse.add("Одежда", "Брюки", 3000, 20)

    # 2. Показываем начальный отчёт
    print("=== Начальный склад ===")
    warehouse.print_inventory()

    # 3. Делаем движения
    warehouse.move("Ноутбук", "Продажа", "Клиент А", 5)
    warehouse.move("Рубашка", "Возврат", "Поставщик", 3)
    warehouse.move("Брюки", "Внутреннее перемещение", "Склад Б", 2)

    # 4. Показываем изменения
    print("\n=== После движений ===")
    warehouse.print_inventory()

    # 5. Добавляем предупреждения
    warehouse.print_warnings()

    # 6. Генерируем отчёт
    warehouse.generate_report()

    # 7. Показываем историю
    warehouse.print_history()

    print("\n=== Демо завершено ===")
    return warehouse
