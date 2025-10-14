"""
Write a function to check whether the given string starts and ends with the same character or not.
assert check_char("abba") == "Valid"
"""



def check_char(s):
    return "Valid" if s[0] == s[-1] else "Invalid"

# Example usage
# result = check_char("abba")
# print(result)  # Output: Valid
