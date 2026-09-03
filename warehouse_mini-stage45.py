# === Stage 45: Добавь восстановление из резервной копии ===
# Project: WarehouseMini
def restore_backup(backup_path):
    """Восстановление базы данных из резервной копии."""
    if not backup_path or not os.path.exists(backup_path):
        print("Файл резервной копии не найден.")
        return False
    try:
        with open(backup_path, 'r') as f:
            data = json.load(f)
        if 'warehouse_db' not in data:
            print("Неверный формат резервной копии.")
            return False
        db = WarehouseDB()
        db.products = data['warehouse_db']['products']
        db.movements = data['warehouse_db']['movements']
        db.alerts = data['warehouse_db']['alerts']
        db.alerts_processed = data['warehouse_db']['alerts_processed']
        db.last_sync = data['warehouse_db']['last_sync']
        print(f"Базу данных успешно восстановлена из {backup_path}")
        return True
    except Exception as e:
        print(f"Ошибка восстановления: {e}")
        return False
