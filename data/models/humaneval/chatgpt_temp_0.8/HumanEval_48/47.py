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
    # check if text is empty or has one character
    if len(text) <= 1:
        return True
    
    # compare first and last characters
    if text[0] == text[-1]:
        # recursively check the substring without the first and last characters
        return is_palindrome(text[1:-1])
    else:
        return False
