class CharacterBase:
    def __init__(self):
        # Properties
        self.system_prompt = ""
        self.message_history = []
        self.important_notes = []
        self.inventory = ""

    def set_system_prompt(self, prompt):
        self.system_prompt = prompt

    def add_to_message_history(self, message):
        self.message_history.append(message)

    def add_important_note(self, note):
        self.important_notes.append(note)

    def set_inventory(self, inventory):
        self.inventory = inventory

    def display_character_info(self):
        print("Character Information:")
        print(f"System Prompt: {self.system_prompt}")
        print(f"Message History: {self.message_history}")
        print(f"Important Notes: {self.important_notes}")
        print(f"Inventory: {self.inventory}")