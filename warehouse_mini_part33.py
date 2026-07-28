# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: WarehouseMini
class UndoableAction:
    def __init__(self, fn, args=(), kwargs=None):
        self.fn = fn
        self.args = args
        self.kwargs = kwargs or {}

    def undo(self):
        return self.fn(*reversed(self.args), **{k[::-1]: v for k, v in reversed(list(self.kwargs.items()))})

def undo_last_action(actions_stack):
    if not actions_stack:
        raise RuntimeError("Нет действий для отката")
    action = actions_stack.pop()
    return action.undo()
