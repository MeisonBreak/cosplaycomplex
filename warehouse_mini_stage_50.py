# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: WarehouseMini
def format_balance_report(current: dict, low_stock: list, out_of_stock: list) -> str:
    """Сформировать итоговый отчёт о балансе склада."""
    lines = ["=" * 60, "ОТЧЁТ БАЛАНСА СЛАДА", "=" * 60]
    if not current and not low_stock and not out_of_stock:
        return "\n".join(lines) + "\nСклад пуст."
    if current:
        lines.append("\n[Текущие остатки]")
        for name, qty in current.items():
            lines.append(f"  {name:20s} : {qty:>6d} шт.")
    if low_stock:
        lines.append("\n[Низкий остаток]")
        for name, qty in low_stock:
            lines.append(f"  {name:20s} : {qty:>6d} шт.")
    if out_of_stock:
        lines.append("\n[Отсутствует]")
        for name, qty in out_of_stock:
            lines.append(f"  {name:20s} : {qty:>6d} шт.")
    lines.append("=" * 60)
    return "\n".join(lines)

def format_movement_log(movements: list) -> str:
    """Сформировать историю движений."""
    lines = ["=" * 60, "ИСТОРИЯ ДВИЖЕНИЙ", "=" * 60]
    if not movements:
        return "\n".join(lines) + "\nДвижений не записано."
    for date, action, item, qty in movements:
        lines.append(f"  [{date}] {action:10s} {item:20s} : {qty:>6d} шт.")
    lines.append("=" * 60)
    return "\n".join(lines)

def print_summary(current: dict, low_stock: list, out_of_stock: list, movements: list) -> None:
    """Вывести отчёты в консоль."""
    print(format_balance_report(current, low_stock, out_of_stock))
    print(format_movement_log(movements))
