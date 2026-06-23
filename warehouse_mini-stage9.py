# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: WarehouseMini
import json, sys
from datetime import datetime

def load_initial_data(json_string: str) -> dict:
    try:
        data = json.loads(json_string)
        if not isinstance(data, list): raise ValueError("JSON должен содержать массив")
        
        inventory = {item['sku']: item for item in data}
        movements = []
        alerts = []
        
        now = datetime.now()
        for item in data:
            sku = item.get('sku')
            qty = int(item.get('quantity', 0))
            
            if qty < 5 and not inventory[sku].get('low_stock'):
                alert = {'type': 'LOW_STOCK', 'item': sku, 'qty': qty}
                alerts.append(alert)
                item['low_stock'] = True
            
            movements.append({
                'id': len(movements) + 1,
                'date': now.strftime('%Y-%m-%d %H:%M'),
                'type': 'INITIAL_LOAD',
                'sku': sku,
                'quantity': qty
            })
            
        return {
            'inventory': inventory,
            'movements': movements,
            'alerts': alerts
        }
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        sys.exit(1)

# Пример использования (раскомментируйте для теста):
if __name__ == "__main__":
    sample_json = '[{"sku":"ITEM001","name":"Гайка М6","quantity":4},{"sku":"ITEM002","name":"Шпилька M8","quantity":50}]'
    warehouse_data = load_initial_data(sample_json)
    print(f"Загружено товаров: {len(warehouse_data['inventory'])}")
    print(f"Предупреждений: {len(warehouse_data['alerts'])}")
