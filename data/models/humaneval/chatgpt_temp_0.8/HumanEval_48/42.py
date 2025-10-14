python
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
    # Convert the text to lower case and remove non-alphanumeric characters
    text = ''.join(c for c in text.lower() if c.isalnum())
    # Check if the text is the same forwards and backwards
    return text == text[::-1]
