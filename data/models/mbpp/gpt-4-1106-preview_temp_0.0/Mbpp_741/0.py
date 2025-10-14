"""
Write a python function to check whether all the characters are same or not.
assert all_Characters_Same("python") == False
"""



def all_Characters_Same(s):
    return len(set(s)) == 1

# Example usage:
# assert all_Characters_Same("python") == False
