"""
Write a function to sort a given list of strings of numbers numerically. https://www.geeksforgeeks.org/python-sort-numeric-strings-in-a-list/
assert sort_numeric_strings( ['4','12','45','7','0','100','200','-12','-500'])==[-500, -12, 0, 4, 7, 12, 45, 100, 200]
"""



def sort_numeric_strings(list_of_numeric_strings):
    return sorted(list_of_numeric_strings, key=int)

# Example usage
sorted_list = sort_numeric_strings(['4','12','45','7','0','100','200','-12','-500'])
assert sorted_list == ['-500', '-12', '0', '4', '7', '12', '45', '100', '200']
