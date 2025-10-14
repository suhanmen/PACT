def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    # Check if the length of the string is 0 or 1, return True
    if len(text) <= 1:
        return True
    # Check if the first and last characters of the string are the same
    elif text[0] == text[-1]:
        # Recursively call the function on the substring without the first and last characters
        return is_palindrome(text[1:-1])
    else:
        return False
