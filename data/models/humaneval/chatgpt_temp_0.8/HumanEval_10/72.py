def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    """
    if string == '':
        return ''
    suffix = ''
    for i in range(len(string), 0, -1):
        if is_palindrome(string[i-1:]):
            suffix = string[i-1:]
            break
    prefix = string[:len(string)-len(suffix)]
    return prefix + suffix[::-1] + string[len(string)-len(suffix):]
