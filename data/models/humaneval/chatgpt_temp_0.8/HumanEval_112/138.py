def reverse_delete(s,c):
    """
    Task: We are given two strings s and c, you have to delete all the characters in s that are equal to any character in c
          then check if the result string is palindrome.
          A string is called palindrome if it reads the same backward as forward.
          You should return a tuple containing the result string and True/False for the check.

    Inputs:
    s - a string
    c - a string

    Outputs:
    A tuple containing the modified string and a boolean value indicating whether the modified string is a palindrome or not.
    """

    # Delete all characters in s that are equal to any character in c
    for char in c:
        s = s.replace(char, "")

    # Check if modified string is a palindrome
    is_palindrome = s == s[::-1]

    # Return tuple containing modified string and boolean value indicating whether it is a palindrome or not
    return s, is_palindrome
