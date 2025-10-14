def reverse_delete(s,c):
    # Remove characters in s that are in c
    result = ''.join([char for char in s if char not in c])
    
    # Check if the resulting string is a palindrome
    is_palindrome = result == result[::-1]
    
    # Return a tuple of the resulting string and the boolean value for palindrome check
    return (result, is_palindrome)
