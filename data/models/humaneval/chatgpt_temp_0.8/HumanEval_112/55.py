# CANNOT PARSE CODE SNIPPET
def reverse_delete(s, c):
    # Remove all characters in s that are equal to any character in c
    result = "".join([char for char in s if char not in c])
    # Check if the result string is a palindrome
    is_palindrome = result == result[::-1]
    # Return the result string and whether it is a palindrome or not
    return (result, is_palindrome)
