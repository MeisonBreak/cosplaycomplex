# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: WarehouseMini
class Reminder:
    def __init__(self, title, description='', due_date=None):
        self.title = title
        self.description = description
        self.due_date = due_date  # datetime.date or None
        self.done = False
    
    def is_overdue(self, today=None):
        if self.due_date and not self.done:
            return (today - self.due_date).days > 0
        return False
    
    def __repr__(self):
        status = '✅' if self.done else ('🔴' if self.is_overdue() else '⏳')
        date_str = '' if not self.due_date else f' ({self.due_date})'
        return f"{status} [{self.title}] {self.description}{date_str}"


def add_reminders(warehouse):
    warehouse.reminders = []

    def add(title, desc='', due=None):
        r = Reminder(title, desc, due)
        warehouse.reminders.append(r)
        return r
    
    def mark_done(idx):
        if 0 <= idx < len(warehouse.reminders):
            warehouse.reminders[idx].done = True
    
    def list_active():
        today = datetime.date.today()
        active = [r for r in warehouse.reminders if not r.done and r.is_overdue(today)]
        return active

    add.__doc__ = "Добавить напоминание"
    mark_done.__doc__ = "Отметить выполнено"
    list_active.__doc__ = "Получить просроченные напоминания"
