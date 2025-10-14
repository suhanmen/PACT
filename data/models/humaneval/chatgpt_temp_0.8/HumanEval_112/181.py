# CANNOT PARSE CODE SNIPPET
def reverse_delete(s, c):
    """Task
    We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    Example
    For s = "abcde", c = "ae", the result should be ('bcd',False)
    For s = "abcdef", c = "b"  the result should be ('acdef',False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc',True)
    """
    # Delete all characters in s that are equal to any character in c
    s_filtered = "".join([char for char in s if char not in c])

    # Check if the filtered string is a palindrome
    is_palindrome = s_filtered == s_filtered[::-1]

    return (s_filtered, is_palindrome)
