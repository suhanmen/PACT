"""
Write a function to find the n most expensive items in a given dataset.
assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)==[{'name': 'Item-2', 'price': 555.22}]
"""


import heapq

def expensive_items(items, n):
    # Use nlargest to find the n most expensive items
    return heapq.nlargest(n, items, key=lambda x: x['price'])

# Example usage
# expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}], 1)
# Output: [{'name': 'Item-2', 'price': 555.22}]
