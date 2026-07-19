# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: WarehouseMini
def reset_demo():
    """Сбросить демо-данные: очистить все сущности."""
    global products, stock_levels, movements, alerts, settings
    products = []
    stock_levels = {}
    movements = []
    alerts = []
    settings = {
        "currency": "₽",
        "warehouse_name": "Склад Mini",
        "low_stock_threshold": 10,
        "expired_days_warning": 365,
        "auto_alert_low_stock": True,
        "auto_alert_expired": False,
    }
