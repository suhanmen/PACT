# CANNOT PARSE CODE SNIPPET
def reverse_delete(s, c):
    # Delete characters in s that are equal to any character in c
    s = ''.join([char for char in s if char not in c])
    
    # Check if the result string is palindrome
    is_palindrome = s == s[::-1]

    # Return the result string and True/False for the palindrome check
    return (s, is_palindrome)
