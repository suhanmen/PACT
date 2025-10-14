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
    # Define two pointers, one at the beginning and one at the end of the string
    left = 0
    right = len(text) - 1

    # While the two pointers don't meet in the middle
    while left < right:
        # If the characters at the two pointers are not the same, return False
        if text[left] != text[right]:
            return False
        # Move the pointers towards the middle
        left += 1
        right -= 1
    # If we've made it to the middle of the string, return True
    return True
