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
    # reverse the string
    reversed_text = text[::-1]
    
    # check if the original string and reversed string are equal
    if text == reversed_text:
        return True
    else:
        return False
