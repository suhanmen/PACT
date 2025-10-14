"""
Write a function to replace whitespaces with an underscore and vice versa in a given string.
assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'
"""



def replace_spaces(input_string):
    return input_string.replace(' ', '_') if ' ' in input_string else input_string.replace('_', ' ')

# Example usage:
# replaced_string = replace_spaces('Jumanji The Jungle')
# print(replaced_string)  # Output: Jumanji_The_Jungle

# Test case
assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'
