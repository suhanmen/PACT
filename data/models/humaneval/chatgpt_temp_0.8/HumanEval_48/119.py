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
    # Reverse the string
    reversed_text = text[::-1]
    
    # Compare the original with reversed string
    if text == reversed_text:
        return True
    else:
        return False
