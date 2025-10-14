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
    # Remove whitespaces and make all letters lowercase
    text = text.replace(" ", "").lower()
    # Reverse the string
    reversed_text = text[::-1]
    # Check if the original text and the reversed text are the same
    if text == reversed_text:
        return True
    else:
        return False
