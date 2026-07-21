# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: WarehouseMini
APP_CONFIG = {
    "app_name": "WarehouseMini",
    "version": "0.1",
    "default_qty_threshold": 5,
    "auto_warn_on_low_stock": True,
    "log_level": "INFO",
}


def get_config():
    return APP_CONFIG
