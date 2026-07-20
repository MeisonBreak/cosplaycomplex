# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: WarehouseMini
def print_metrics():
    if not products:
        return
    total_value = sum(p['price'] * p.get('stock', 0) for p in products.values())
    low_stock = [p for p in products.values() if p.get('stock', 0) <= LOW_STOCK_THRESHOLD]
    out_of_stock = [p for p in products.values() if p.get('stock', 0) == 0]
    total_moves = sum(len(m['items']) for m in moves)

    print(f"=== Сводка по складу ===")
    print(f"Всего товаров: {len(products)}")
    print(f"Общая стоимость на складе: {total_value:.2f}")
    print(f"Движений за все время: {total_moves}")
    if low_stock:
        print(f"⚠️  Низкий запас ({LOW_STOCK_THRESHOLD} шт):")
        for p in low_stock:
            print(f"   - {p['name']}: остаток {p.get('stock', 0)}")
    if out_of_stock:
        print("🔴 Товары без остатка:")
        for p in out_of_stock:
            print(f"   - {p['name']}")
