def reverse_delete(s,c):
    # Delete all characters in s that are present in c
    for char in c:
        s = s.replace(char, '')
    
    # Check if the resulting string is a palindrome
    if s == s[::-1]:
        return (s, True)
    else:
        return (s, False)
