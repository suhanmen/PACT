python
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
    # Define two pointers, one starting from the beginning and one from the end
    left = 0
    right = len(text) - 1
    # Iterate while the pointers do not overlap
    while left < right:
        # If the characters at the pointers are not the same, the string is not a palindrome
        if text[left] != text[right]:
            return False
        # Move the pointers closer to the center
        left += 1
        right -= 1
    # If we have reached this point, the string is a palindrome
    return True
