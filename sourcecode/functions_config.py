from functions import print_to_console, add_two_numbers, hello_world, retrieve_inventory

whitelisted_functions = {
    "hello_world": {
        "func": hello_world,
        "description": "Say hello to the world!",
        "properties": [],
    },
    "print_to_console": {
        "func": print_to_console,
        "description": "",
        "properties": [
            {
                "property_name": "output_str",
                "description": "The string to print to the console",
                "type": "str",
                "default_value": None
            }
        ]
    },
    "add_two_numbers": {
        "func": add_two_numbers,
        "description": "",
        "properties": [
            {
                "property_name": "num1",
                "description": "The first number to add. Must be an int.",
                "type": "int",
                "default_value": None
            },
            {
                "property_name": "num2",
                "description": "The second number to add. Must be an int.",
                "type": "int",
                "default_value": None
            }
        ]
    },
        "retrieve_inventory": {
        "func": retrieve_inventory,
        "description": "Retrieve the current inventory",
        "properties": []  # No properties for this function
    },
}
