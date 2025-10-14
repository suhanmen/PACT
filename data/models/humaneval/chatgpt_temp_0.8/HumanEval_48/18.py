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
    # check if the length of the text is 0 or 1
    if len(text) <= 1:
        return True

    # compare the first and last characters of the text
    if text[0] == text[-1]:
        # recursively call the function on the middle of the text
        return is_palindrome(text[1:-1])
    else:
        return False
