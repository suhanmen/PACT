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
    # Remove all non-alphanumeric characters and convert to lowercase
    text = ''.join(filter(str.isalnum, text)).lower()
    # Check if the text is the same forwards and backwards
    return text == text[::-1]
