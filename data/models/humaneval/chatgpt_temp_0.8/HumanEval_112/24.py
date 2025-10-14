# CANNOT PARSE CODE SNIPPET
def reverse_delete(s, c):
    """
    We are given two strings s and c, and we need to delete all the characters in s that are equal to any character in c.
    Then we will check if the result string is a palindrome.
    A string is called palindrome if it reads the same backward as forward.
    We will return a tuple containing the result string and True/False for the check.
    """
    # delete characters in s that are equal to any character in c
    for ch in c:
        s = s.replace(ch, "")
    
    # check if the result string is a palindrome
    if s == s[::-1]:
        return s, True
    else:
        return s, False
