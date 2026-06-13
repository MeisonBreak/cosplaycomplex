# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: WarehouseMini
import json
from datetime import datetime, timedelta
from typing import Optional

class WarehouseState:
    def __init__(self):
        self.products = {}  # id -> {name, sku, quantity}
        self.movements = []  # list of {timestamp, product_id, type, amount, note}
    
    def add_product(self, name: str, sku: str, initial_qty: int) -> None:
        if not name or not sku: raise ValueError("Name and SKU required")
        self.products[sku] = {"name": name, "sku": sku, "quantity": initial_qty}
    
    def record_movement(self, product_sku: str, movement_type: str, amount: int, note: Optional[str] = None) -> bool:
        if product_sku not in self.products: raise KeyError(f"Product {product_sku} not found")
        prod = self.products[product_sku]
        new_qty = prod["quantity"] + amount
        if new_qty < 0: raise ValueError("Negative stock balance not allowed")
        
        movement = {
            "timestamp": datetime.now().isoformat(),
            "product_id": product_sku,
            "type": movement_type,
            "amount": amount,
            "note": note or ""
        }
        self.movements.append(movement)
        prod["quantity"] = new_qty
        return True
    
    def get_stock(self, sku: str) -> Optional[int]:
        return self.products.get(sku, {}).get("quantity")

warehouse_db = WarehouseState()
