# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: WarehouseMini
def generate_summary():
    if not warehouse_items: return "Склад пуст."
    total_value = sum(item['price'] * item['quantity'] for item in warehouse_items.values())
    low_stock = [name for name, data in warehouse_items.items() if data['quantity'] < 10]
    print(f"Всего товаров: {len(warehouse_items)}")
    print(f"Общая стоимость остатков: {total_value:.2f}")
    if low_stock: print(f"Товары с низким запасом (<10): {', '.join(low_stock)}")
