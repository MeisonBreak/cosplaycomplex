# === Stage 17: Добавь группировку записей по категориям ===
# Project: WarehouseMini
def group_by_category(records):
    from collections import defaultdict
    grouped = defaultdict(list)
    for rec in records:
        cat = rec.get('category', 'Uncategorized')
        grouped[cat].append(rec)
    return dict(sorted(grouped.items()))
