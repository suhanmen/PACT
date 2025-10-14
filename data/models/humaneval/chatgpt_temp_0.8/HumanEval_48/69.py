# CANNOT PARSE CODE SNIPPET
def is_palindrome(text: str) -> bool:
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
    # Special case: empty string is a palindrome
    if not text:
        return True
    # Check if string is equal to its reverse
    return text == text[::-1]
