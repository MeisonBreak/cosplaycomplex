# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: WarehouseMini
import shutil, os, datetime

def backup_data(data_file: str, backup_dir: str = "backups") -> str:
    """Создаёт резервную копию файла данных и возвращает путь к копии."""
    os.makedirs(backup_dir, exist_ok=True)
    if not os.path.isfile(data_file):
        raise FileNotFoundError(f"Файл данных не найден: {data_file}")
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"{os.path.basename(data_file)}.bak_{ts}")
    shutil.copy2(data_file, backup_path)
    return backup_path
