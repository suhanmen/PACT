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
    # Convert text to lowercase and remove non-alphanumeric characters
    text = ''.join(c for c in text.lower() if c.isalnum())
    # Check if the reversed string is equal to the original string
    return text == text[::-1]
