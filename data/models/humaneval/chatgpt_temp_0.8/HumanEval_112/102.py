def reverse_delete(s,c):
    # Delete characters in s that are in c
    s = ''.join([char for char in s if char not in c])
    # Check if s is a palindrome
    is_palindrome = s == s[::-1]
    # Return the resulting string and whether it is a palindrome
    return (s, is_palindrome)
