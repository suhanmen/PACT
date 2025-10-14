# CANNOT PARSE CODE SNIPPET
def reverse_delete(s, c):
    """
    Task: We are given two strings s and c, you have to delete all the characters in s that are equal to any character in c
          then check if the result string is palindrome. A string is called palindrome if it reads the same backward as forward.
          You should return a tuple containing the result string and True/False for the check.
          
    Args:
    s: A string to be modified
    c: A string containing characters to be deleted from s
    
    Returns:
    A tuple containing the modified string and True/False for palindrome check.
    """
    # Delete characters in s that are in c
    s = ''.join([char for char in s if char not in c])
    
    # Check if modified string is palindrome
    is_palindrome = s == s[::-1]
    
    return s, is_palindrome
