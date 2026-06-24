# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: WarehouseMini
def export_to_json():
    import json
    from datetime import datetime
    data = {
        "timestamp": datetime.utcnow().isoformat(),
        "products": products,
        "movements": movements,
        "alerts": alerts
    }
    return json.dumps(data, ensure_ascii=False, indent=2)
