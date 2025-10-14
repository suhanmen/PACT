def reverse_delete(s,c):
    new_s = ""
    for char in s:
        if char not in c:
            new_s += char
    palindrome = new_s == new_s[::-1]
    return (new_s, palindrome)
