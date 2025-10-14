"""
Write a function to remove the parenthesis and what is inbetween them from a string.
assert remove_parenthesis(["python (chrome)"])==("python")
"""



def remove_parenthesis(strings):
    import re
    return [re.sub(r"\(.*?\)", "", string).strip() for string in strings]

# Example usage:
# result = remove_parenthesis(["python (chrome)"])
# print(result)  # Output: ['python']
