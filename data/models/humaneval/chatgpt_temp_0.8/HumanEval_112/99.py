def reverse_delete(s,c):
    # Delete all characters in s that are equal to any character in c
    s = ''.join([char for char in s if char not in c])
    
    # Check if the resulting string is palindrome
    is_palindrome = s == s[::-1]
    
    # Return a tuple containing the resulting string and True/False for the check
    return (s, is_palindrome)
