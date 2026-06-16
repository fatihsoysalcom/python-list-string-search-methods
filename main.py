def find_string_in_list(data_list, search_string):
    """Demonstrates various methods to find a string within a Python list."""

    print(f"--- Searching for '{search_string}' in {data_list} ---")

    # Method 1: Using a for loop and equality check
    print("\nMethod 1: For loop with equality check")
    found_loop = False
    for item in data_list:
        if item == search_string: # Direct comparison
            print(f"  Found '{search_string}' at index {data_list.index(item)} using loop.")
            found_loop = True
            break # Stop after first find
    if not found_loop:
        print(f"  '{search_string}' not found using loop.")

    # Method 2: Using the 'in' operator (most Pythonic for existence check)
    print("\nMethod 2: Using the 'in' operator")
    if search_string in data_list: # Checks for existence efficiently
        print(f"  '{search_string}' is present in the list.")
        # To get the index, we can use .index() after confirming existence
        print(f"  First occurrence at index: {data_list.index(search_string)}")
    else:
        print(f"  '{search_string}' is not present in the list.")

    # Method 3: Using list comprehension to find all occurrences
    print("\nMethod 3: List comprehension for all occurrences")
    indices_comprehension = [i for i, item in enumerate(data_list) if item == search_string] # Creates a list of indices
    if indices_comprehension:
        print(f"  '{search_string}' found at indices: {indices_comprehension}")
    else:
        print(f"  '{search_string}' not found using list comprehension.")

    # Method 4: Using filter() and lambda for a functional approach
    print("\nMethod 4: Using filter() and lambda")
    # This finds items that match, not indices directly, but we can adapt
    matching_items = list(filter(lambda item: item == search_string, data_list))
    if matching_items:
        print(f"  Found matching items: {matching_items}")
        # To get indices, we'd still need enumerate or .index() on the original list
        first_index_filter = data_list.index(search_string) if search_string in data_list else -1
        if first_index_filter != -1:
            print(f"  First occurrence index (using .index()): {first_index_filter}")
    else:
        print(f"  No matching items found using filter().")

# --- Example Usage ---
data = ["apple", "banana", "cherry", "date", "banana", "fig"]

# Search for an existing string
find_string_in_list(data, "banana")

# Search for a non-existing string
find_string_in_list(data, "grape")

# Search for a case-sensitive string
find_string_in_list(data, "Apple")
