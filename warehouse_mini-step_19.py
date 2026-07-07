# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: WarehouseMini
def archive_records(records, days=365):
    """Archive records older than `days` days into a separate list."""
    cutoff = time.time() - days * 86400
    active = []
    archived = []
    for r in records:
        if isinstance(r, dict) and "created_at" in r:
            ts = datetime.fromisoformat(r["created_at"]).timestamp()
            if ts < cutoff:
                archived.append(r.copy())
            else:
                active.append(r)
        else:
            active.append(r)
    return active, archived
