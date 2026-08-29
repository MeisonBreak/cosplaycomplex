# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: WarehouseMini
import sys

def colorize(text, color, bold=False):
    """Apply ANSI color codes to text. Returns (text, enabled)."""
    if not sys.stdout.isatty():
        return text, False
    codes = {"red": "\033[31m", "green": "\033[32m", "yellow": "\033[33m",
             "blue": "\033[34m", "magenta": "\033[35m", "cyan": "\033[36m",
             "white": "\033[37m", "reset": "\033[0m", "bold": "\033[1m"}
    prefix = codes.get(color, "")
    if bold:
        prefix += codes["bold"]
    return f"{prefix}{text}{codes['reset']}", True
