# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: WarehouseMini
import json, os

def load_data(filepath):
    if not os.path.exists(filepath):
        print(f"Файл {filepath} не найден.")
        return {}
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print("Данные успешно загружены из JSON.")
        return data
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON в {filepath}: {e}")
        return {}
    except Exception as e:
        print(f"Неожиданная ошибка при чтении файла: {e}")
        return {}

# Пример вызова (раскомментируй для работы):
# inventory = load_data('warehouse.json')
