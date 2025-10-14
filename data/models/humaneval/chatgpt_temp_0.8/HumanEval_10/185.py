def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    """
    if not string:
        return ''
    
    max_suffix = ''
    for i in range(len(string)):
        suffix = string[i:]
        if is_palindrome(suffix) and len(suffix) > len(max_suffix):
            max_suffix = suffix
    
    prefix = string[:len(string) - len(max_suffix)]
    return prefix + max_suffix + prefix[::-1]
