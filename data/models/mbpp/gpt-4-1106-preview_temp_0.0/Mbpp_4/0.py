"""
Write a function to find the n largest integers from a given list of numbers, returned in descending order.
assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)==[85, 75, 65]
"""


import heapq

def heap_queue_largest(numbers, n):
    return heapq.nlargest(n, numbers)

# Example usage:
# largest_three = heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 3)
# print(largest_three)  # Output: [85, 75, 65]
