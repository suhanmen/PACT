# CANNOT PARSE CODE SNIPPET
def reverse_delete(s, c):
    new_str = ""
    for char in s:
        if char not in c:
            new_str += char
    is_palindrome = new_str == new_str[::-1]
    return (new_str, is_palindrome)
