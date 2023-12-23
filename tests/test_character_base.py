import io
import unittest
from unittest.mock import patch
#from context import sourcecode
#from context import inventory
from sourcecode.character_classes.character_base import CharacterBase
from sourcecode.inventory.inventory_item import InventoryItem

class TestCharacterBase(unittest.TestCase):

    def setUp(self):
        self.character = CharacterBase()

    def test_set_system_prompt(self):
        prompt = "Welcome to the game!"
        self.character.set_system_prompt(prompt)
        self.assertEqual(self.character.system_prompt, prompt)

    def test_add_to_message_history(self):
        message = "You found a hidden treasure!"
        self.character.add_to_message_history(message)
        self.assertIn(message, self.character.message_history)

    def test_add_important_note(self):
        note = "Remember the secret code: XYZ123"
        self.character.add_important_note(note)
        self.assertIn(note, self.character.important_notes)

    def test_set_inventory(self):
        self.reset_for_new_test()

        inventory = [InventoryItem(item_id=1, item_name="Sword", description="Sharp", quantity=3)]
        self.character.set_inventory(inventory)
        self.assertEqual(self.character.inventory, inventory)

    def test_find_matching_items(self):
        self.reset_for_new_test()
        item = InventoryItem(item_id=1, item_name="Sword", description="Sharp", quantity=3)
        self.character.add_to_inventory(item)

        matching_item = self.character.find_matching_items(item)

        self.assertEqual(matching_item, item)

    def test_add_to_inventory(self):
        self.reset_for_new_test()
        item1 = InventoryItem(item_id=1, item_name="Sword", description="Sharp", quantity=3)
        item2 = InventoryItem(item_id=1, item_name="Sword", description="Sharp", quantity=2)

        self.character.add_to_inventory(item1)
        self.character.add_to_inventory(item2)

        self.assertEqual(self.character.inventory[0].quantity, 5)

    def test_remove_from_inventory(self):
        self.reset_for_new_test()
        item = InventoryItem(item_id=1, item_name="Sword", description="Sharp", quantity=3)
        self.character.add_to_inventory(item)

        self.character.remove_from_inventory(item)

        self.assertEqual(self.character.inventory, [])

    def test_get_inventory_as_string(self):
        self.reset_for_new_test()
        item = InventoryItem(item_id=1, item_name="Sword", description="Sharp", quantity=3)
        self.character.add_to_inventory(item)

        expected_output = "ItemID: 1, Name: Sword, Description: Sharp, Quantity: 3"
        self.assertEqual(self.character.get_inventory_as_string(), expected_output)

    def test_register_function(self):
        def example_function():
            return "Example"
        self.character.register_function("example", example_function, "Example function")
        self.assertIn("example", self.character.whitelisted_functions)
        self.assertEqual(self.character.whitelisted_functions["example"]["func"](), "Example")

    def test_display_character_info(self):
        # Redirect stdout to capture print output
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.character.display_character_info()
            expected_output = "Character Information:\nSystem Prompt: \nMessage History: []\nImportant Notes: []\nInventory: \n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def reset_for_new_test(self):
        """Reset the character so we can run a fresh test."""
        self.character.inventory = []


if __name__ == '__main__':
    unittest.main()
