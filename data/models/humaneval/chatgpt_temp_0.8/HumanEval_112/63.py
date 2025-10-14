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
    
    # Remove characters in s that are in c
    filtered_s = "".join([char for char in s if char not in c])
    
    # Check if filtered_s is a palindrome
    is_palindrome = filtered_s == filtered_s[::-1]
    
    # Return tuple with filtered_s and is_palindrome
    return (filtered_s, is_palindrome)
