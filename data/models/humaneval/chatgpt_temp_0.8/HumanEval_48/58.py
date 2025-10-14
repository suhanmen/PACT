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
    # If text is empty, it is a palindrome
    if len(text) == 0:
        return True
    
    # Check if the text is equal to its reverse
    return text == text[::-1]
