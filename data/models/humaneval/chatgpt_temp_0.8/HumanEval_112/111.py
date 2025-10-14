def reverse_delete(s,c):
    # Delete all characters in s that are equal to any character in c
    result = ""
    for char in s:
        if char not in c:
            result += char
    
    # Check if the result string is palindrome
    is_palindrome = result == result[::-1]
    
    # Return the result string and True/False for the check
    return (result, is_palindrome)
