# CANNOT PARSE CODE SNIPPET
def reverse_delete(s, c):
    """
    Task:
    We are given two strings s and c, you have to delete all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.

    Args:
    s (str): a string
    c (str): a string

    Returns:
    tuple: containing the result string and True/False for the check.
    """

    # Step 1: Delete all the characters in s that are equal to any character in c
    for char in c:
        s = s.replace(char, '')

    # Step 2: Check if the result string is palindrome
    if s == s[::-1]:
        return s, True
    else:
        return s, False
