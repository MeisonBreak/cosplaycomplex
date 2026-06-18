# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: WarehouseMini
def filter_records(records, filters=None):
    if not filters: return records
    result = []
    for r in records:
        match_status = 'status' not in filters or str(r.get('status')) == str(filters['status'])
        match_category = 'category' not in filters or str(r.get('category', '')) == str(filters['category'])
        match_tags = 'tags' not in filters or any(str(f) in str(t) for f in (filters.get('tags') or []) for t in r.get('tags', []))
        if match_status and match_category and match_tags: result.append(r)
    return result

def get_filtered_products(products, status=None, category=None, tags=None):
    filters = {'status': status, 'category': category, 'tags': tags} if any([status, category, tags]) else None
    return filter_records(products, filters)
