# CANNOT PARSE CODE SNIPPET
def reverse_delete(s, c):
    # Delete characters in s that are equal to any character in c
    result_str = ''.join([char for char in s if char not in c])
    
    # Check if the resulting string is palindrome
    is_palindrome = result_str == result_str[::-1]
    
    # Return the result as a tuple
    return (result_str, is_palindrome)
