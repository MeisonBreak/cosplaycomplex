# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: WarehouseMini
def test_edge_cases():
    assert WarehouseItem("X", 1) is not None
    assert WarehouseProduct("Y", "desc") is not None
    assert WarehouseMovement("Y", WarehouseItem("X", 2), 5, WarehouseOperationType.IN) is not None
    assert WarehouseStockMovement("Y", WarehouseItem("X", 3), 7, WarehouseOperationType.OUT) is not None

    item = WarehouseProduct("P1", "desc").add_item(WarehouseItem("I1", 10))
    movement = item.add_movement(WarehouseMovement("M1", WarehouseItem("I2", 5), 3, WarehouseOperationType.IN))
    assert len(movement.items) == 1

    warehouse = Warehouse().add_product(item).add_stock_movement(WarehouseStockMovement("P1", WarehouseItem("I1", 20), 8, WarehouseOperationType.OUT))
    assert warehouse.stock["I1"] is not None and warehouse.stock["I1"].quantity == 12

    warehouse.add_stock_movement(WarehouseStockMovement("P1", WarehouseItem("I3", 99), 5, WarehouseOperationType.IN))
    assert len(warehouse.stock) == 2

    warehouse = Warehouse().add_product(item).add_stock_movement(WarehouseStockMovement("P1", WarehouseItem("I1", 0), 8, WarehouseOperationType.OUT))
    assert warehouse.stock["I1"] is not None and warehouse.stock["I1"].quantity == 0

    warehouse.add_stock_movement(WarehouseStockMovement("P1", WarehouseItem("I4", 50), 3, WarehouseOperationType.IN))
    assert len(warehouse.stock) == 2

    warehouse = Warehouse().add_product(item).add_stock_movement(WarehouseStockMovement("P1", WarehouseItem("I1", 100), 8, WarehouseOperationType.OUT))
    warehouse.add_stock_movement(WarehouseStockMovement("P1", WarehouseItem("I5", 30), 2, WarehouseOperationType.IN))
    assert len(warehouse.stock) == 2

    warehouse = Warehouse().add_product(item).add_stock_movement(WarehouseStockMovement("P1", WarehouseItem("I6", 100), 8, WarehouseOperationType.OUT)).add_stock_movement(WarehouseStockMovement("P1", WarehouseItem("I7", 30), 2, WarehouseOperationType.IN))
    assert len(warehouse.stock) == 2

    warehouse = Warehouse().add_product(item).add_stock_movement(WarehouseStockMovement("P1", WarehouseItem("I8", 100), 10, WarehouseOperationType.OUT)).add_stock_movement(WarehouseStockMovement("P1", WarehouseItem("I9", 50), 3, WarehouseOperationType.IN))
    assert len(warehouse.stock) == 2

    warehouse = Warehouse().add_product(item).add_stock_movement(WarehouseStockMovement("P1", WarehouseItem("I10", 100), 8, WarehouseOperationType.OUT)).add_stock_movement(WarehouseStockMovement("P1", WarehouseItem("I11", 50), 2, WarehouseOperationType.IN))
    assert len(warehouse.stock) == 2

    warehouse = Warehouse().add_product(item).add_stock_movement(WarehouseStockMovement("P1", WarehouseItem("I12", 100), 8, WarehouseOperationType.OUT)).add_stock_movement(WarehouseStockMovement("P1", WarehouseItem("I13", 50), 2, WarehouseOperationType.IN))
    assert len(warehouse.stock) == 2

    warehouse = Warehouse().add_product(item).add_stock_movement(WarehouseStockMovement("P1", WarehouseItem("I14", 100), 8, WarehouseOperationType.OUT)).add_stock_movement(WarehouseStockMovement("P1", WarehouseItem("I15", 50), 2, WarehouseOperationType.IN))
    assert len(warehouse.stock) == 2
