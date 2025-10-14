def reverse_delete(s,c):
    # Delete all the characters in s that are equal to any character in c
    s = ''.join([char for char in s if char not in c])
    
    # Check if the result string is palindrome
    is_palindrome = s == s[::-1]
    
    # Return a tuple containing the result string and True/False for the palindrome check
    return (s, is_palindrome)
