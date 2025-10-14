# CANNOT PARSE CODE SNIPPET
def reverse_delete(s, c):
    # Delete all characters in s that are present in c
    s = "".join([char for char in s if char not in c])
    
    # Check if the result string is a palindrome
    is_palindrome = s == s[::-1]
    
    return (s, is_palindrome)
