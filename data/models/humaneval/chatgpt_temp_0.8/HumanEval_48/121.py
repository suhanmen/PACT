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
    if len(text) < 2:
        # An empty string or string with only one character is a palindrome.
        return True
    else:
        # Compare the first and last characters of the string, then recursively check the rest.
        return text[0] == text[-1] and is_palindrome(text[1:-1])
