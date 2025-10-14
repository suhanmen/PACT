"""
Write a function to remove odd characters in a string.
assert remove_odd("python")==("yhn")
"""



def remove_odd(input_string):
    return ''.join(char for idx, char in enumerate(input_string) if idx % 2 == 1)

# Example usage:
# result = remove_odd("python")
# print(result)  # Output: "yhn"
