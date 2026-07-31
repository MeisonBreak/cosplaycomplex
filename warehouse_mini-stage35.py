# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: WarehouseMini
def suggest_next_action(state):
    """Generate a short recommendation based on current warehouse state."""
    actions = []
    
    # Check for low stock warnings
    if "low_stock" in state:
        items = state["low_stock"]
        for item, qty in items.items():
            actions.append(f"⚠️ {item}: остаток {qty} — докупить")
    
    # Check recent movements
    if "recent_movements" in state and state["recent_movements"]:
        last = state["recent_movements"][-1]
        if last.get("type") == "inbound":
            actions.append(f"📦 Поступление: {last['product']} ({last['quantity']}) учтено")
        elif last.get("type") == "outbound":
            actions.append(f"🚚 Отгрузка: {last['product']} ({last['quantity']}) учтена")
    
    # Check for stale items (not moved in a while)
    if "stale_products" in state and state["stale_products"]:
        actions.append("📋 Есть товары без движений — проверить актуальность")

    if not actions:
        return "✅ Склад в порядке. Следующее действие — ваше."
    
    return "\n".join(actions)


# Пример вызова (замените на реальные данные):
# print(suggest_next_action({
#     "low_stock": {"Шпильки M8": 5, "Гайки M10": 2},
#     "recent_movements": [{"type": "outbound", "product": "Булавки", "quantity": 10}],
#     "stale_products": []
# }))
