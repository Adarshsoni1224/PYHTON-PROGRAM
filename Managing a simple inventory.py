# Managing a simple inventory

# Create an initial inventory dictionary
inventory = {
    'apples': 50,
    'bananas': 20,
    'oranges': 35
}
print(f"Initial Inventory: {inventory}")

# Add a new item to the dictionary
inventory['grapes'] = 15
print(f"After adding grapes: {inventory}")

# Update the value of an existing item
inventory['apples'] = 40
print(f"After updating apples: {inventory}")

# Iterate through the dictionary and print each item using the .items() method
print("\nCurrent Inventory Details:")
for item, quantity in inventory.items():
    print(f"- {item.capitalize()}: {quantity} units")
