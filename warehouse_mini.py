# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: WarehouseMini
import sys
from datetime import datetime

# --- Базовая структура WarehouseMini (Этап 1) ---

class Product:
    def __init__(self, name, sku):
        self.name = name
        self.sku = sku
        self.quantity = 0

    def add(self, amount):
        self.quantity += amount

    def remove(self, amount):
        if self.quantity >= amount:
            self.quantity -= amount
            return True
        return False

class WarehouseMini:
    def __init__(self):
        self.products = {}
        self.movements = []

    def add_product(self, name, sku):
        if sku not in self.products:
            self.products[sku] = Product(name, sku)
            print(f"[INFO] Товар '{name}' (SKU: {sku}) добавлен.")
        else:
            print(f"[WARN] Товар со SKU '{sku}' уже существует.")

    def move(self, sku, amount, description):
        if sku in self.products:
            success = self.products[sku].remove(amount)
            if success:
                movement = {
                    "timestamp": datetime.now().isoformat(),
                    "sku": sku,
                    "product_name": self.products[sku].name,
                    "amount": amount,
                    "type": "OUT",
                    "description": description
                }
                self.movements.append(movement)
                print(f"[LOG] Убыль: {amount} шт. {self.products[sku].name} ({description}). Остаток: {self.products[sku].quantity}")
                return True
            else:
                print(f"[ERROR] Недостаточно остатков для товара '{self.products[sku].name}'.")
                return False
        else:
            print(f"[ERROR] Товар со SKU '{sku}' не найден.")
            return False

    def get_status(self):
        print("\n--- Текущий статус склада ---")
        for sku, prod in self.products.items():
            print(f"SKU: {sku}, Товар: {prod.name}, Остаток: {prod.quantity}")
        if not self.products:
            print("Склад пуст.")

# --- Точка входа и демонстрационные данные ---

if __name__ == "__main__":
    app = WarehouseMini()

    # Добавляем товары
    app.add_product("Ноутбук Pro", "NB-001")
    app.add_product("Мышь беспроводная", "MS-055")

    # Демонстрационные движения
    app.move("NB-001", 2, "Продажа клиенту А")
    app.move("MS-055", 5, "Продажа клиенту Б")
    
    # Попытка убыли больше остатка (тестирование обработки ошибок)
    app.move("NB-001", 100, "Ошибка: попытка продажи")

    # Вывод статуса
    app.get_status()
