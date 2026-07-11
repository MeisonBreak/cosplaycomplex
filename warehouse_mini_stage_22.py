# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: WarehouseMini
def check_expired_reminders():
    now = datetime.now()
    expired = []
    for item in items:
        if item.reminder_date and item.reminder_date < now:
            if not any(m['item_id'] == item.id for m in moves):
                expired.append(item)
    return expired
