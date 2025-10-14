def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    """
    if is_palindrome(string):
        # If the string is already a palindrome, return it as is
        return string
    
    # Find longest palindromic suffix of the string
    for i in range(len(string), 0, -1):
        suffix = string[i-1:]
        if is_palindrome(suffix):
            break
    
    # Find prefix that comes before the palindromic suffix
    prefix = string[:i-1]
    
    # Append reverse of prefix to the end of the string
    palindrome = string + prefix[::-1]
    
    return palindrome
