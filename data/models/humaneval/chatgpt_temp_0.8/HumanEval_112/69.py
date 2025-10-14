python
def reverse_delete(s,c):
    """
    Task: Given two strings s and c, delete all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    
    Parameters:
    s (str): The input string
    c (str): The characters to be deleted from s
    
    Returns:
    Tuple: A tuple containing the result string and True/False for the palindrome check
    """
    
    # Delete all the characters in s that are equal to any character in c
    for char in c:
        s = s.replace(char, "")

    # Check if the resulting string is a palindrome
    is_palindrome = s == s[::-1]
    
    # Return the result string and the True/False value for the palindrome check
    return (s, is_palindrome)
