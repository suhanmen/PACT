def reverse_delete(s,c):
    # Deleting all the characters in s that are equal to any character in c
    s = ''.join([i for i in s if i not in c])
    
    # Checking if the resulting string is palindrome
    if s == s[::-1]:
        return (s, True)
    else:
        return (s, False)
