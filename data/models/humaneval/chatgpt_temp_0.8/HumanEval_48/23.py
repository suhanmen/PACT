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
    # The following line of code is used to remove any spaces or punctuation marks from the text string
    text = ''.join(e for e in text if e.isalnum()).lower()
    # Check if the reversed string is same as the original string
    return text == text[::-1]
