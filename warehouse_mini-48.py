# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: WarehouseMini
def _format_qty(q):
    if q is None:
        return ''
    if isinstance(q, float) and q == int(q):
        return str(int(q))
    return str(q)

def _format_date(d):
    if d is None:
        return ''
    return str(d)

def _format_amount(a):
    if a is None:
        return ''
    return f'{a:,.2f}'

def _format_bool(b):
    if b is None:
        return ''
    return b

def _format_alert(a):
    if a is None:
        return ''
    return a

def _format_stock(s):
    return (
        f'  {s.name} | {s.code}\n'
        f'  {s.quantity} шт. | {s.min_qty} мин.\n'
        f'  {s.last_update}\n'
        f'  {s.alert}'
    )

def _format_inventory(i):
    return (
        f'  {i.product} | {i.quantity} шт.\n'
        f'  {i.last_update}\n'
        f'  {i.total_cost:.2f} руб.\n'
        f'  {i.alert}'
    )

def _format_movement(m):
    return (
        f'  {m.date} | {m.type}\n'
        f'  {m.product} | {m.quantity} шт.\n'
        f'  {m.comment}'
    )

def _format_stats(stats):
    return (
        f'  Товаров: {stats.products}\n'
        f'  Движений: {stats.movements}\n'
        f'  Ошибок: {stats.errors}\n'
        f'  {stats.last_update}'
    )

def _format_settings(s):
    return (
        f'  {s.name} | {s.code}\n'
        f'  {s.quantity} шт.\n'
        f'  {s.last_update}'
    )

def _format_report(r):
    return (
        f'  {r.title}\n'
        f'  {r.date}\n'
        f'  {r.summary}'
    )
