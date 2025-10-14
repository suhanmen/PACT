def reverse_delete(s,c):
    no_match = ''
    for char in s:
        if char not in c:
            no_match += char
    
    is_palindrome = no_match == no_match[::-1]
    
    return (no_match, is_palindrome)
