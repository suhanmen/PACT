"""
Write a python function to check whether a list of numbers contains only one distinct element or not.
assert unique_Element([1,1,1]) == True
"""



def unique_element(numbers):
    return len(set(numbers)) == 1

# Example usage:
# assert unique_element([1,1,1]) == True
