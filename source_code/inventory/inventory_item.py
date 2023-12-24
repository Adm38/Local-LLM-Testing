class InventoryItem:
    def __init__(self, item_id, item_name, description="", quantity=1):
        self.item_id = item_id
        self.item_name = item_name
        self.description = description
        self.quantity = quantity

    def __str__(self):
        return f"ItemID: {self.item_id}, Name: {self.item_name}, Description: {self.description}, Quantity: {self.quantity}"