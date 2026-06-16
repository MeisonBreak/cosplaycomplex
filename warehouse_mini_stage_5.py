# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: WarehouseMini
def delete_item(item_id: int) -> bool:
    if item_id not in items:
        print(f"Предупреждение: товар с ID {item_id} не найден.")
        return False
    del items[item_id]
    print(f"Товар с ID {item_id} успешно удалён из списка товаров.")
    return True

def delete_movement(movement_id: int) -> bool:
    if movement_id not in movements:
        print(f"Предупреждение: движение с ID {movement_id} не найдено.")
        return False
    del movements[movement_id]
    print(f"Движение с ID {movement_id} успешно удалено из истории операций.")
    return True

def delete_stock(stock_id: int) -> bool:
    if stock_id not in stocks:
        print(f"Предупреждение: остаток с ID {stock_id} не найден.")
        return False
    del stocks[stock_id]
    print(f"Остаток с ID {stock_id} успешно удалён из реестра складов.")
    return True

def delete_warning(warning_id: int) -> bool:
    if warning_id not in warnings:
        print(f"Предупреждение: уведомление с ID {warning_id} не найдено.")
        return False
    del warnings[warning_id]
    print(f"Уведомление с ID {warning_id} успешно удалено из списка предупреждений.")
    return True
