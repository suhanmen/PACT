# CANNOT PARSE CODE SNIPPET
def reverse_delete(s, c):
    # Remove all characters in s that are equal to any character in c
    new_s = ''.join([char for char in s if char not in c])
    
    # Check if the new string is palindrome
    is_palindrome = new_s == new_s[::-1]
    
    # Return the result as a tuple
    return (new_s, is_palindrome)
