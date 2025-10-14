# CANNOT PARSE CODE SNIPPET
def reverse_delete(s, c):
    # Delete all characters in s that are equal to any character in c
    new_s = ""
    for char in s:
        if char not in c:
            new_s += char
    
    # Check if the resulting string is a palindrome
    is_palindrome = new_s == new_s[::-1]
    
    # Return a tuple containing the resulting string and whether it is a palindrome
    return (new_s, is_palindrome)
