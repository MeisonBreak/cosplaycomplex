# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: WarehouseMini
def print_table(headers, rows):
    """Компактная функция для отрисовки таблицы в консоль."""
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            if len(cell) > col_widths[i]:
                col_widths[i] = len(cell)

    sep = '─' * sum(col_widths + [3]) + '┘'
    fmt = '│'.join(f'{{:<{w}}}' for w in col_widths)

    print(sep.replace('┘', ''))  # верхняя граница
    print(fmt.format(*headers).replace('─', '┬'))
    for row in rows:
        print(('├' + fmt.replace('─', '│')).format(*row))
    print((sep.replace('┘', '')).replace('─', '└'))

print_table(['Товар', 'Остаток', 'Последнее движение'],
            [['Гайка М8', 150, '2024-03-15'], ['Шестигранник', 7, '2024-03-16']])
