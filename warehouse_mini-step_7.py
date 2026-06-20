# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: WarehouseMini
def sort_records(records, key='date', reverse=False):
    if not records: return []
    def get_sort_key(r):
        val = r.get(key)
        try:
            return (0, val) if isinstance(val, str) else (1, val)
        except TypeError:
            return (2, '')
    return sorted(records, key=get_sort_key, reverse=reverse)

def get_priority_level(priority):
    levels = {'critical': 0, 'high': 1, 'medium': 2, 'low': 3}
    return levels.get(str(priority).lower(), 4)

def sort_by_date(records):
    records.sort(key=lambda x: x.get('date') or '', reverse=True)
    return records

def sort_by_priority(records):
    records.sort(key=get_priority_level)
    return records

def sort_by_name(records, case_sensitive=False):
    key = str.lower if not case_sensitive else str
    records.sort(key=lambda x: (0, key(x.get('name', ''))) or (1, ''))
    return records

# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: WarehouseMini
def sort_records(records, key='date', reverse=False):
    if not records: return []
    def get_sort_key(item):
        val = item.get(key)
        try:
            return (0, val) if isinstance(val, datetime.date) else (1, str(val))
        except Exception:
            return (2, '')
    priority_map = {'critical': 0, 'high': 1, 'medium': 2, 'low': 3}
    def get_priority(item):
        p = item.get('priority', 'low')
        try: return priority_map[p.lower()] if isinstance(p, str) else float('inf')
        except Exception: return float('inf')
    name_key = item.get('name', '') or ''
    sort_keys = [lambda x: get_sort_key(x), lambda x: get_priority(x)]
    sorted_records = sorted(records, key=lambda r: (get_sort_key(r), get_priority(r), str(name_key)), reverse=reverse)
    return sorted_records
