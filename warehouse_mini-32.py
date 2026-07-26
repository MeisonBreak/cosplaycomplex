# === Stage 32: Добавь журнал действий пользователя ===
# Project: WarehouseMini
class ActionLogger:
    def __init__(self):
        self.actions = []

    def log(self, action_type, description, timestamp=None):
        if timestamp is None:
            from datetime import datetime
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        record = {"type": action_type, "description": description, "timestamp": timestamp}
        self.actions.append(record)

    def show_recent(self, limit=5):
        return "\n".join(f"[{r['timestamp']}] {r['type']}: {r['description']}" for r in reversed(self.actions[-limit:]))


logger = ActionLogger()


def log_action(action_type, description):
    logger.log(action_type, description)
