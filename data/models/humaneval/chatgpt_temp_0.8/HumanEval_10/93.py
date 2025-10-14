def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    """
    # If the string is already a palindrome, return it
    if is_palindrome(string):
        return string
    
    # Find the longest palindromic suffix
    for i in range(len(string)-1, -1, -1):
        if is_palindrome(string[i:]):
            break
    
    # Append the reverse of the prefix before the palindromic suffix
    return string + string[:i][::-1]

