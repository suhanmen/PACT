# CANNOT PARSE CODE SNIPPET
def reverse_delete(s, c):
    # Delete all characters in c from s
    for char in c:
        s = s.replace(char, '')

    # Check if resulting string is palindrome
    is_palindrome = s == s[::-1]

    # Return tuple with resulting string and palindrome check
    return (s, is_palindrome)
