def reverse_delete(s,c):
    """
    Task:
    We are given two strings s and c, you have to delete all the characters in s that are equal to any character in c,
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    
    Args:
    s (str): The string we are removing characters from and checking for palindrome.
    c (str): The string of characters we are removing from s.

    Returns:
    tuple: A tuple containing the result string and True/False for the palindrome check.
    
    Example:
    For s = "abcde", c = "ae", the result should be ('bcd',False)
    For s = "abcdef", c = "b", the result should be ('acdef',False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc',True)
    """
    
    # Removing all characters in c from s and storing the result in a new string called "result"
    result = ""
    for i in s:
        if i not
