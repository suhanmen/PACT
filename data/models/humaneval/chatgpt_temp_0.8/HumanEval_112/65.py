# CANNOT PARSE CODE SNIPPET
def reverse_delete(s, c):
    new_s = ""
    for char in s:
        if char not in c:
            new_s += char
    return (new_s, new_s == new_s[::-1])
