def reverse_delete(s,c):
    # Remove characters in s that are in c
    result = ''.join([char for char in s if char not in c])
    # Check if the result string is palindrome
    is_palindrome = result == result[::-1]
    # Return the result string and the boolean flag for palindrome check
    return (result, is_palindrome)
