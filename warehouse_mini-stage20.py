# === Stage 20: Добавь восстановление записей из архива ===
# Project: WarehouseMini
def restore_from_archive(self, archive_path):
        """Восстанавливает записи из архива."""
        if not os.path.exists(archive_path):
            raise FileNotFoundError(f"Архив не найден: {archive_path}")
        with open(archive_path, 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) < 4:
                    continue
                try:
                    self.items[parts[0]] = {'name': parts[1], 'quantity': int(parts[2]), 'price': float(parts[3])}
                    self.movements.append({'product_id': parts[0], 'type': 'restored', 'date': parts[4] if len(parts) > 4 else datetime.now().isoformat(), 'quantity': int(parts[2])})
                except Exception:
                    continue
