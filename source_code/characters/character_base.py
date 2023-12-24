from typing import List
#from context import sourcecode, inventory
#from sourcecode.inventory.inventory_item import InventoryItem
from ..inventory.inventory_item import InventoryItem

class CharacterBase:
    def __init__(self):
        # Properties
        self.system_prompt = ""
        self.message_history = []
        self.important_notes = []

        self.inventory: List[InventoryItem] = []

        self.whitelisted_functions = {}

    def set_system_prompt(self, prompt):
        self.system_prompt = prompt

    def add_to_message_history(self, message):
        self.message_history.append(message)

    def add_important_note(self, note):
        self.important_notes.append(note)

    def set_inventory(self, inventory: List[InventoryItem]):
        if not inventory or not isinstance(inventory[0], InventoryItem):
            raise TypeError("Object passed to `set_inventory` must be a non-empty list with elements of type InventoryItem.")
        self.inventory = inventory
    
    def find_matching_items(self, inventory_item: InventoryItem) -> InventoryItem:
        if not isinstance(inventory_item, InventoryItem):
            raise TypeError(f"Object passed to `find_matching_items` must be of type InventoryItem. Received {type(inventory_item)}")
        
        matching_items = list(filter(lambda item: item.item_id == inventory_item.item_id, self.inventory))
        if matching_items is None or len(matching_items) == 0:
            return None

        if len(matching_items) > 1:
            raise ValueError(f"Duplicate items with ItemID '{inventory_item.item_id}' found in inventory.")

        return matching_items[0]

    def add_to_inventory(self, inventory_item: InventoryItem):
        if not isinstance(inventory_item, InventoryItem):
            raise TypeError(f"Object passed to `add_to_inventory` must be of type InventoryItem. Received {type(inventory_item)}")
        
        existing_inventory_item = self.find_matching_items(inventory_item)
        if existing_inventory_item is None:
            self.inventory.append(inventory_item)
        else:
            existing_inventory_item.quantity += inventory_item.quantity
    
    def remove_from_inventory(self, inventory_item: InventoryItem):
        if not isinstance(inventory_item, InventoryItem):
            raise TypeError(f"Object passed to `remove_from_inventory` must be of type InventoryItem. Received {type(inventory_item)}")
    
        existing_inventory_item = self.find_matching_items(inventory_item)
        if not existing_inventory_item:
            raise ValueError(f"Item with ItemID '{inventory_item.item_id}' not found in inventory.")

        if existing_inventory_item.quantity >= inventory_item.quantity:
            existing_inventory_item.quantity -= inventory_item.quantity
            if existing_inventory_item.quantity == 0:
                self.inventory.remove(existing_inventory_item)
        else:
            raise ValueError(f"Not enough quantity ({existing_inventory_item.quantity}) to remove {inventory_item.quantity}.")

    def get_inventory_as_string(self):
        return "\n".join(str(item) for item in self.inventory)

    def register_function(self, func_name, func, description="", properties=None) -> None:
        if properties is None:
            properties = []
        
        self.whitelisted_functions[func_name] = {
            "func":func,
            "description":description,
            "properties":properties
        }

    def display_character_info(self):
        print("Character Information:")
        print(f"System Prompt: {self.system_prompt}")
        print(f"Message History: {self.message_history}")
        print(f"Important Notes: {self.important_notes}")
        print(f"Inventory: {self.get_inventory_as_string()}")


if __name__ == "__main__":
    character = CharacterBase()
    print(f"exiting {__name__}")