def reverse_delete(s,c):
    # Deleting characters in s that are equal to any character in c
    result = ''.join([char for char in s if char not in c])
    
    # Checking if result is palindrome
    is_palindrome = result == result[::-1]
    
    # Returning tuple containing result string and boolean value for palindrome check
    return (result, is_palindrome)
