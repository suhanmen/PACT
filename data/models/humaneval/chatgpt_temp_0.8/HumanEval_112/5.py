# CANNOT PARSE CODE SNIPPET
def reverse_delete(s, c):
    """
    Task: We are given two strings s and c. You have to delete all the characters in s that are equal to any character in c,
    then check if the result string is palindrome. A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.

    Example: 
    For s = "abcde", c = "ae", the result should be ('bcd',False)
    For s = "abcdef", c = "b", the result should be ('acdef',False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc',True)
    """

    # Delete characters in s that are equal to any character in c
    s = ''.join([char for char in s if char not in c])

    # Check if the result string is palindrome
    is_palindrome = s == s[::-1]

    # Return the result string and True/False for the palindrome check
    return s, is_palindrome
