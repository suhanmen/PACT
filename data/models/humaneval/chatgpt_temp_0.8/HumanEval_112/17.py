# CANNOT PARSE CODE SNIPPET
def reverse_delete(s, c):
    # Remove all characters in s that are in c
    s = ''.join([char for char in s if char not in c])
    # Check if the resulting string is a palindrome
    if s == s[::-1]:
        return s, True
    else:
        return s, False
