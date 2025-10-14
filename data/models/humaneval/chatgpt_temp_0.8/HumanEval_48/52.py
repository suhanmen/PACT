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
    
    if text == "":
        return True
    
    # Convert to lowercase and remove non-alpha characters
    text = ''.join(e for e in text if e.isalpha()).lower()
    
    # Check if the string is equal to its reverse
    return text == text[::-1]
