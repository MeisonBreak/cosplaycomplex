# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: WarehouseMini
def main():
    import argparse
    parser = argparse.ArgumentParser(description="WarehouseMini CLI")
    sub = parser.add_subparsers(dest="cmd")
    sub.add_parser("list", help="list all items")
    sub.add_parser("add", help="add a new item")
    sub.add_parser("move", help="record a stock movement")
    sub.add_parser("alerts", help="show low-stock alerts")
    sub.add_parser("summary", help="print warehouse summary")
    args = parser.parse_args()
    if args.cmd == "list":
        for item in items:
            print(f"{item.name}: {item.quantity} pcs")
    elif args.cmd == "add":
        print("Usage: add --name <name> --quantity <qty>")
    elif args.cmd == "move":
        print("Usage: move --item <name> --quantity <qty> [--in|--out]")
    elif args.cmd == "alerts":
        for item in items:
            if item.quantity < 10:
                print(f"WARNING: {item.name} has only {item.quantity} pcs left")
    elif args.cmd == "summary":
        total = sum(item.quantity for item in items)
        print(f"Total items: {len(items)}, Total stock: {total} pcs")
    else:
        parser.print_help()
