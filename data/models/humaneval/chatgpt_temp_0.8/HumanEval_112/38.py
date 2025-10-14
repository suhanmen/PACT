# CANNOT PARSE CODE SNIPPET
def reverse_delete(s, c):
    # Delete characters in s that are in c
    s = "".join([char for char in s if char not in c])
    # Check if the resulting string is palindrome
    is_palindrome = s == s[::-1]
    # Return tuple of the resulting string and whether it is palindrome
    return (s, is_palindrome)
