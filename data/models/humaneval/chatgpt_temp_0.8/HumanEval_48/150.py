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
    # Convert the input string to lowercase and remove whitespace
    text = text.lower().replace(" ", "")

    # Reverse the string
    reverse_text = text[::-1]

    # Check if the reversed string is equal to the original string
    if text == reverse_text:
        return True
    else:
        return False
