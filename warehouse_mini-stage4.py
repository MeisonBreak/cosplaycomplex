# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: WarehouseMini
def edit_record(record_id, updates):
    if record_id not in records:
        print(f"Ошибка: запись с ID {record_id} не найдена.")
        return False
    for key, value in updates.items():
        if hasattr(records[record_id], key):
            setattr(records[record_id], key, value)
        else:
            print(f"Ошибка: поле '{key}' недоступно для редактирования.")
            return False
    save_data()
    print(f"Запись {record_id} успешно обновлена.")
    return True

if __name__ == "__main__":
    # Пример использования функции редактирования
    if records:
        item = list(records.values())[0]
        print("Текущие данные товара:", item)
        
        # Редактируем товар (меняем название и цену)
        edit_record(item.id, {"name": "Новое название", "price": 150.0})
        
        if records:
            updated_item = list(records.values())[0]
            print("Обновленные данные товара:", updated_item)
    else:
        print("Нет данных для редактирования.")
