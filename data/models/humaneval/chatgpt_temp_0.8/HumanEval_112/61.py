def reverse_delete(s,c):
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
    # Delete characters from s that are present in c
    for char in c:
        s = s.replace(char, "")
    
    # Check if result string is palindrome
    is_palindrome = True
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            is_palindrome = False
            break
    
    return s, is_palindrome
