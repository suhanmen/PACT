# CANNOT PARSE CODE SNIPPET
def reverse_delete(s, c):
    """
    Task: We are given two strings s and c, you have to delete all the characters in s that are equal to any character in c
    then check if the result string is palindrome. A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    """
    s = ''.join([i for i in s if i not in c]) # delete characters in s that are equal to any character in c
    is_palindrome = s == s[::-1] # check if the result string is a palindrome
    return (s, is_palindrome)
