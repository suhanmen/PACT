"""
Write a function that takes two lists and returns true if they have at least one common element.
assert common_element([1,2,3,4,5], [5,6,7,8,9])==True
"""



def common_element(list1, list2):
    return any(element in list2 for element in list1)

assert common_element([1,2,3,4,5], [5,6,7,8,9])==True
