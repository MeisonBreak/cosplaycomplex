# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: WarehouseMini
import unittest, sys


class TestWarehouseMini(unittest.TestCase):
    def test_add_product(self):
        from warehouse import Warehouse
        w = Warehouse()
        w.add_product("A1", 100)
        self.assertEqual(len(w.products), 1)
        self.assertEqual(w.get_stock("A1"), 100)

    def test_move_and_deplete(self):
        from warehouse import Warehouse
        w = Warehouse()
        w.add_product("X", 50)
        w.move("X", "Y", 30)
        self.assertEqual(w.get_stock("X"), 20)
        self.assertGreaterEqual(w.get_stock("Y"), 30)

    def test_warn_low_stock(self):
        from warehouse import Warehouse, LowStockWarning
        w = Warehouse()
        w.add_product("Z", 5)
        warnings = list(w.check_warnings())
        self.assertTrue(any(isinstance(w, LowStockWarning) and w.product == "Z" for w in warnings))

    def test_history(self):
        from warehouse import Warehouse
        w = Warehouse()
        w.add_product("H", 10)
        w.move("H", "K", 3)
        history = w.get_history()
        self.assertEqual(len(history), 2)


if __name__ == "__main__":
    unittest.main()
