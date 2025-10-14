"""
Write a function that takes in a dictionary and integer n and filters the dictionary to only include entries with values greater than or equal to n.
assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},170)=={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
"""

def dict_filter(input_dict, n):
    return {k: v for k, v in input_dict.items() if v >= n}

# Example usage
# filtered_dict = dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}, 170)
# print(filtered_dict) # Output: {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}