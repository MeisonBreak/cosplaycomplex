# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: WarehouseMini
def calculate_weekly_stats(data):
    from datetime import date, timedelta
    if not data: return {}
    today = date.today()
    week_start = today - timedelta(days=today.weekday())
    end_date = week_start + timedelta(weeks=1)
    stats = {"in": 0, "out": 0, "balance_change": 0}
    for d in data:
        if isinstance(d["date"], str): d["date"] = date.fromisoformat(d["date"])
        if week_start <= d["date"] < end_date:
            stats["in"] += d.get("qty_in", 0)
            stats["out"] += d.get("qty_out", 0)
    return stats
