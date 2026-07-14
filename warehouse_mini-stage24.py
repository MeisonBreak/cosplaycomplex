# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: WarehouseMini
def print_record(rec):
    """Компактный вывод одной записи."""
    if isinstance(rec, dict):
        print(f"[{rec.get('id', '?')}] {rec.get('type', '')}: "
              f"{rec.get('name', rec.get('sku', ''))} | "
              f"количество={rec.get('qty', '—')} | "
              f"дата={rec.get('date', rec.get('ts', ''))}")
    elif hasattr(rec, '__dict__'):
        print(f"[{getattr(rec, 'id', '?')}] {getattr(rec, 'type', '')}: "
              f"{getattr(rec, 'name', getattr(rec, 'sku', ''))} | "
              f"количество={getattr(rec, 'qty', '—')} | "
              f"дата={getattr(rec, 'date', getattr(rec, 'ts', ''))}")
    else:
        print(repr(rec))
