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
    # Remove spaces and convert to lowercase to ignore case
    text = text.replace(' ', '').lower()
    # Compare the first half with the reversed second half
    return text == text[::-1]
