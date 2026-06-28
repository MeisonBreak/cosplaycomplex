# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: WarehouseMini
def search_inventory(query: str) -> list[dict]:
    query = query.lower().strip()
    if not query:
        return []
    
    results = []
    for item in inventory_items:
        searchable_text = f"{item['name']} {item['sku']} {item['category']}".lower()
        if query in searchable_text:
            results.append(item)
    
    movements_query = query.lower().strip()
    recent_movements = [m for m in all_movements 
                        if (movements_query in f"{m['type']} {m['product_name']} {m['quantity_change']}".lower())]
    
    alerts_query = query.lower().strip()
    low_stock_alerts = [a for a in stock_alerts 
                         if (alerts_query in f"Товар: {a['name']} Остаток: {a['current_quantity']}".lower())]
    
    return results + recent_movements + low_stock_alerts
