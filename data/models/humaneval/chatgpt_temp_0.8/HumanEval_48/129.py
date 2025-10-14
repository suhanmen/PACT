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
    # Get the length of the text
    n = len(text)
    
    # Iterate over the first half of the text
    for i in range(n // 2):
        # Check if the corresponding characters in the first half and last half of the text match
        if text[i] != text[n - i - 1]:
            # If they don't match, return False
            return False
    
    # If we've made it through the loop without returning False, the text is a palindrome
    return True
