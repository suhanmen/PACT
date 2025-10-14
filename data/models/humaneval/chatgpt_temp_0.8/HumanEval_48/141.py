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
    # Remove all spaces and convert to lowercase
    text = text.replace(' ', '').lower()
    # Check if the reversed string is equal to the original
    return text == text[::-1]
