# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: WarehouseMini
class ValidationError(Exception):
    pass

def validate_product_name(name: str) -> str:
    if not name or len(name.strip()) < 2:
        raise ValidationError("Название товара должно быть не пустым и содержать минимум 2 символа.")
    return name.strip()

def validate_quantity(qty: int, min_qty: int = 0) -> int:
    if not isinstance(qty, int) or qty < min_qty:
        raise ValidationError(f"Количество должно быть целым числом >= {min_qty}.")
    return qty

def validate_date(date_str: str) -> str:
    try:
        from datetime import datetime
        datetime.strptime(date_str, "%Y-%m-%d")
        return date_str
    except ValueError:
        raise ValidationError("Дата должна быть в формате YYYY-MM-DD.")

def validate_sku(sku: str) -> str:
    if not sku or len(sku) < 4:
        raise ValidationError("SKU должен содержать минимум 4 символа.")
    return sku.upper()
