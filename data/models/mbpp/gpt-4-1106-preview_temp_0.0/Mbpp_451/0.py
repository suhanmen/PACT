"""
Write a function to remove all whitespaces from the given string.
assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'
"""



def remove_whitespaces(input_string):
    return ''.join(input_string.split())

# Example usage:
# cleaned_string = remove_whitespaces(' Google    Flutter ')
# print(cleaned_string)  # Output: 'GoogleFlutter'
