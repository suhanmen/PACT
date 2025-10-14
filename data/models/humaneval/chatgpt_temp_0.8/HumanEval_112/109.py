# CANNOT PARSE CODE SNIPPET
def reverse_delete(s, c):
    """
    We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.

    :param s: string to be modified and checked
    :param c: string containing characters to be removed from s
    :return: a tuple containing the modified string and True/False for whether it is a palindrome
    """
    # Remove characters from s that are present in c
    modified_s = ''.join([char for char in s if char not in c])

    # Check if modified_s is a palindrome
    is_palindrome = modified_s == modified_s[::-1]

    # Return the modified string and whether it is a palindrome as a tuple
    return modified_s, is_palindrome
