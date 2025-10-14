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
    # Convert the string to lowercase and remove any non-alphanumeric characters
    text = ''.join(e for e in text.lower() if e.isalnum())

    # Compare the string with its reversed version
    return text == text[::-1]
