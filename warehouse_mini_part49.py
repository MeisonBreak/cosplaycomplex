# === Stage 49: Добавь финальную самопроверку приложения и отчёт о готовности ===
# Project: WarehouseMini
import sys, os, json, datetime, random

def run_self_check():
    """Финальная самопроверка: проверка структуры, типов, данных и отчёт."""
    errors = []
    warnings = []

    # Проверка, что файл существует и не пустой
    if not os.path.exists(__file__):
        errors.append("Файл проекта не найден")
        sys.exit(1)

    with open(__file__, "r", encoding="utf-8") as f:
        code = f.read()

    if len(code.strip()) < 100:
        errors.append("Код слишком мал — вероятно, файл незаполнен")

    # Проверка импортов
    for cls_name in ("Item", "Stock", "Movement", "Alert"):
        if cls_name not in code:
            warnings.append(f"Класс {cls_name} не найден — возможно, ещё не добавлен")

    # Имитация создания объектов для проверки типов
    try:
        item = Item("Тест", 100, "ед")
        stock = Stock(item, 50)
        mv = Movement("Вход", stock, 20)
        alert = Alert(stock, "Низкий остаток")
        if not (isinstance(item, Item) and isinstance(stock, Stock) and isinstance(mv, Movement) and isinstance(alert, Alert)):
            errors.append("Объекты не создаются корректно")
    except Exception as e:
        errors.append(f"Ошибка при создании объектов: {e}")

    # Проверка методов
    for obj, expected in [(stock, "add_item"), (stock, "remove_item"), (stock, "get_stock"), (stock, "get_stock_value"), (stock, "get_stock_value_by_id")]:
        if not hasattr(obj, expected):
            warnings.append(f"Метод {expected} отсутствует в {type(obj).__name__}")

    for obj, expected in [(item, "add_item"), (item, "remove_item"), (item, "get_item"), (item, "get_items_by_id")]:
        if not hasattr(obj, expected):
            warnings.append(f"Метод {expected} отсутствует в {type(obj).__name__}")

    for obj, expected in [(alert, "check_stock"), (alert, "check_item")]:
        if not hasattr(obj, expected):
            warnings.append(f"Метод {expected} отсутствует в {type(obj).__name__}")

    # Проверка, что Alert работает
    try:
        alert.check_stock(stock, 10)
        alert.check_item(item, 10)
    except Exception as e:
        errors.append(f"Ошибка в Alert: {e}")

    # Вывод отчёта
    print("=" * 60)
    print("SELF-CHECK REPORT")
    print("=" * 60)
    if errors:
        print(f"❌ ERRORS ({len(errors)}):")
        for e in errors:
            print(f"  - {e}")
    if warnings:
        print(f"⚠️ WARNINGS ({len(warnings)}):")
