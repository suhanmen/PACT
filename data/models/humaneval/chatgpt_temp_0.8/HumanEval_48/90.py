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
    # Remove all non-alphanumeric characters and convert to lowercase
    text = ''.join(e for e in text if e.isalnum()).lower()
    
    # Compare original string with its reverse
    return text == text[::-1]
