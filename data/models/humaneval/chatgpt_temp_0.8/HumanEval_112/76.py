# CANNOT PARSE CODE SNIPPET
def reverse_delete(s, c):
    # remove all characters in s that are equal to any character in c
    s = ''.join([i for i in s if i not in c])
    # check if the result string is palindrome
    if s == s[::-1]:
        return (s, True)
    else:
        return (s, False)
