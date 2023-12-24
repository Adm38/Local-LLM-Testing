def create_fake_whitelist():
    fake_whitelist = {
        "display_inventory":display_inventory,
        "greet_customer": greet_customer,
        "checkout_customer": checkout_customer
    }
    return fake_whitelist

def greet_customer():
    print("Hello there, valued customer!")

def display_inventory():
    print("Mango - $3 (4 available)")

def checkout_customer():
    print("Ka-ching!")