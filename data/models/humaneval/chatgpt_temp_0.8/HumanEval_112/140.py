# CANNOT PARSE CODE SNIPPET
def reverse_delete(s, c):
    """
    Task:
    We are given two strings s and c, you have to delete all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    
    Example:
    For s = "abcde", c = "ae", the result should be ('bcd', False)
    For s = "abcdef", c = "b",  the result should be ('acdef', False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc', True)
    """
    
    # Delete all characters in s that match any character in c
    for char in c:
        s = s.replace(char, "")
    
    # Check if the resulting string is a palindrome
    is_palindrome = s == s[::-1]
    
    # Return a tuple with the resulting string and the boolean value for is_palindrome
    return (s, is_palindrome)
