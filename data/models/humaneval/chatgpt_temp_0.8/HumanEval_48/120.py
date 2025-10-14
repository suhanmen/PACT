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
    # Base case: empty string or single character string is a palindrome
    if len(text) <= 1:
        return True
    
    # Recursive case: check if first and last characters match
    if text[0] == text[-1]:
        # Recurse on the substring without the first and last characters
        return is_palindrome(text[1:-1])
    else:
        return False
