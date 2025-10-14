def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    """
    # Check if the supplied string is already a palindrome
    if is_palindrome(string):
        return string

    # Loop through the supplied string from the end
    for i in range(len(string) - 1, -1, -1):
        # Check if there is a palindromic suffix
        if is_palindrome(string[i:]):
            # Append the reverse of the prefix before the palindromic suffix to the end of the string
            return string + string[:i][::-1]
    
    # If no palindromic suffix is found, return the original string with the first character repeated
    return string + string[0]
