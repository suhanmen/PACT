# CANNOT PARSE CODE SNIPPET
def reverse_delete(s, c):
    # Remove characters in s that are in c
    s = "".join([char for char in s if char not in c])
    
    # Check if s is palindrome
    is_palindrome = s == s[::-1]
    
    return (s, is_palindrome)
