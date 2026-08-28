# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: WarehouseMini
def dry_run(operation, data, dry_store=None):
    if dry_store is None:
        dry_store = {}
    dry_store[operation] = data
    return data

def get_dry_store():
    return {}

def set_dry_store(store):
    global _dry_store
    _dry_store = store

def is_dry_run():
    return bool(_dry_store)
