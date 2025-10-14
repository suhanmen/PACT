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
    # Check if the text is empty or has only one character
    if len(text) < 2:
        return True
    
    # Iterate over the first half of the string and compare it with the second half
    for i in range(len(text)//2):
        if text[i] != text[-1-i]:
            return False
    return True
