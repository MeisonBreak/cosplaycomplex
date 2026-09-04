# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: WarehouseMini
def get_data_version():
    """Возвращает текущую версию структуры данных для миграции."""
    return 1

def migrate_data(data, version):
    """Миграция: если версия < 1, добавляем поле version в data."""
    if version < get_data_version():
        data["version"] = get_data_version()
    return data
