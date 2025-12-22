# 1. Create a list
fruits = ["apple", "banana", "cherry"]

# 2. Add an item to the end
fruits.append("orange")

# 3. Access items using an index (starts at 0)
first_fruit = fruits[0]
print(f"First fruit: {first_fruit}")

# 4. Change an item
fruits[1] = "blueberry"

# 5. Remove an item by value
fruits.remove("cherry")

# 6. Get the number of items (length)
list_length = len(fruits)

# 7. Print the final list and its size
print(f"Updated list: {fruits}")
print(f"The list now has {list_length} items.")
