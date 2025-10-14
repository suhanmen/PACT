def reverse_delete(s,c):
    # Delete all characters in s that are equal to any character in c
    for char in c:
        s = s.replace(char, "")
    
    # Check if the resulting string is a palindrome
    is_palindrome = s == s[::-1]
    
    # Return the resulting string and whether or not it is a palindrome
    return (s, is_palindrome)
