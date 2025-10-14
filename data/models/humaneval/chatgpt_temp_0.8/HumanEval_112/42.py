# CANNOT PARSE CODE SNIPPET
def reverse_delete(s, c):
    """
    Task:
    Given two strings s and c, delete all the characters in s that are equal to any character in c,
    then check if the resulting string is a palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.

    Example:
    For s = "abcde", c = "ae", the result should be ('bcd', False)
    For s = "abcdef", c = "b", the result should be ('acdef', False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc', True)
    """
    s = ''.join([char for char in s if char not in c])
    return (s, s == s[::-1])
