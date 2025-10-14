"""
Write a function that takes in an array and element and returns a tuple containing a boolean that indicates if the element is in the array and the index position of the element (or -1 if the element is not found).
assert sequential_search([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)
"""



def sequential_search(arr, elem):
    for index, item in enumerate(arr):
        if item == elem:
            return True, index
    return False, -1

assert sequential_search([11,23,58,31,56,77,43,12,65,19], 31) == (True, 3)
