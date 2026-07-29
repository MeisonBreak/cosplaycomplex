# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: WarehouseMini
TEMPLATES = {
    "inbound": lambda d: (d.setdefault("type", "inbound"), None),
    "outbound": lambda d: (d.setdefault("type", "outbound"), None),
    "transfer": lambda d: (d.setdefault("type", "transfer"), None),
}

def add_template(name, fn):
    if name in TEMPLATES and callable(TEMPLATES[name]):
        return fn({"type": name, "warehouse_id": 1})
    raise ValueError(f"Unknown template: {name}")
