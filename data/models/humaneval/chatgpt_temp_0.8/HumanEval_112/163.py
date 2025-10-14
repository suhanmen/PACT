# CANNOT PARSE CODE SNIPPET
def reverse_delete(s, c):
    # deleting all the characters in s that are equal to any character in c
    result = ''.join([char for char in s if char not in c])

    # checking if the result string is palindrome
    is_palindrome = result == result[::-1]

    # returning a tuple containing the result string and True/False for the check
    return (result, is_palindrome)
