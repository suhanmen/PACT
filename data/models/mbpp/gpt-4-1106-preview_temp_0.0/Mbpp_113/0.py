"""
Write a function to check if a string represents an integer or not.
assert check_integer("python")==False
"""



def check_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# Example usage:
# assert check_integer("python")==False
