# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: WarehouseMini
def check_and_repair_data():
    """Проверка целостности данных и минимальный ремонт проблем."""
    issues = []
    
    # Проверка: каждый товар существует в movements
    for item_id, item in items.items():
        if not any(m["item"] == item_id for m in movements):
            issues.append(f"[WARN] Товар '{item['name']}' не имеет истории движений. Добавлен начальный записи.")
            movements.append({"id": len(movements)+1, "type": "ADD", "item": item_id, 
                              "quantity": 0, "date": str(datetime.now().date()), "warehouse": warehouse_name})

    # Проверка: остатки согласованы с движениями
    for item_id in items:
        current = sum(m["quantity"] * (1 if m["type"]=="ADD" else -1) 
                      for m in movements if m["item"] == item_id and "balance" not in m)
        expected = items[item_id].get("balance", 0)
        if abs(current - expected) > 0.001:
            issues.append(f"[ERROR] Остаток товара '{items[item_id]['name']}' расчисляется как {current:.2f}, но в данных хранится {expected}. Игнорируем расхождение.")

    # Проверка: предупреждения актуальны
    for w in warehouse_warnings:
        if w["date"] < str(datetime.now().date()):
            issues.append(f"[WARN] Предупреждение от {w['date']} устарело, но оставлено.")

    if not issues:
        print("[OK] Данные целы и не требуют ремонта.")
        return []
    
    print("\n[REPAIR LOG]")
    for i in issues:
        print(f"  {i}")
    return issues

if __name__ == "__main__":
    run_warehouse()
