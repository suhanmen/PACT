def reverse_delete(s,c):
    # Delete all characters in s that are in c
    s = ''.join([char for char in s if char not in c])
    # Check if the result string is a palindrome
    is_palindrome = s == s[::-1]
    # Return a tuple containing the result string and True/False for the palindrome check
    return (s, is_palindrome)
