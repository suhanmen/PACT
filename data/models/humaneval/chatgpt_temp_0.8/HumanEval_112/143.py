# CANNOT PARSE CODE SNIPPET
def reverse_delete(s, c):
    # Deleting characters in s that are equal to any character in c
    for char in c:
        s = s.replace(char, "")
        
    # Checking if the result string is palindrome
    if s == s[::-1]:
        return s, True
    else:
        return s, False
