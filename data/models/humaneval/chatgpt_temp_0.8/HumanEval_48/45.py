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
    text = ''.join(char for char in text.lower() if char.isalnum())
    # Check if text is equal to its reverse
    return text == text[::-1]
