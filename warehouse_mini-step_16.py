# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: WarehouseMini
def calc_month_stats(start_date, end_date):
    stats = {"in": 0, "out": 0, "balance_start": {}, "balance_end": {}}
    for item in items:
        if start_date <= item["created_at"] <= end_date:
            if item["type"] == "IN":
                stats["in"] += item["qty"]
            elif item["type"] == "OUT":
                stats["out"] += item["qty"]
    for item in items:
        if item["id"] not in stats["balance_start"]:
            stats["balance_start"][item["id"]] = 0
        if start_date <= item["created_at"] < end_date:
            stats["balance_start"][item["id"]] += item["qty"] * (1 if item["type"] == "IN" else -1)
    for item in items:
        if item["id"] not in stats["balance_end"]:
            stats["balance_end"][item["id"]] = 0
        if start_date <= item["created_at"] < end_date:
            stats["balance_end"][item["id"]] += item["qty"] * (1 if item["type"] == "IN" else -1)
    return stats
