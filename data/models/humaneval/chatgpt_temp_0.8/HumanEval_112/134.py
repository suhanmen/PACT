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
    # deleting all characters in s that are equal to any character in c
    new_str = ""
    for char in s:
        if char not in c:
            new_str += char
    
    # checking if the resulting string is a palindrome
    is_palindrome = new_str == new_str[::-1]
    
    # returning the result as a tuple
    return (new_str, is_palindrome)
