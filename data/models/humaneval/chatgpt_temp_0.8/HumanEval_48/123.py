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
    # Convert the text to lowercase and remove spaces
    text = text.lower().replace(' ', '')

    # Check if the text is equal to its reverse
    return text == text[::-1]
