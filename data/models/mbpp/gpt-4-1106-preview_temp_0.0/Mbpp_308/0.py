"""
Write a function to find the specified number of largest products from two given lists, selecting one factor from each list.
assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]
"""


import heapq

def large_product(list1, list2, n):
    # Generate all possible products
    products = [x * y for x in list1 for y in list2]
    # Find the n largest products
    largest_products = heapq.nlargest(n, products)
    return largest_products

# Example usage
# assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3) == [60, 54, 50]
