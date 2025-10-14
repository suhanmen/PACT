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
    # Remove all white spaces from the text and convert to lowercase
    text = text.replace(" ", "").lower()
    
    # Check if the text is equal to its reverse
    return text == text[::-1]
