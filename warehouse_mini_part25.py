# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: WarehouseMini
def format_date(date_str):
    """Форматирует строку даты в формате ДД.ММ.ГГГГ или возвращает 'неизвестно' если формат не распознан."""
    formats = ['%d.%m.%Y', '%Y-%m-%d']
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    return None

def validate_date(date_str):
    """Проверяет корректность строки даты и возвращает отформатированную дату или сообщение об ошибке."""
    result = format_date(date_str)
    if result is not None:
        return result.strftime('%d.%m.%Y')
    return f"Ошибка: Некорректная дата '{date_str}'. Используйте формат ДД.ММ.ГГГГ или ГГГГ-ММ-ДД."

def safe_int(value, default=0):
    """Пытается преобразовать значение в целое число, возвращая дефолтное при ошибке."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

def safe_float(value, default=0.0):
    """Пытается преобразовать значение в вещественное число, возвращая дефолтное при ошибке."""
    try:
        return float(value)
    except (ValueError, TypeError):
        return default
