def reverse_delete(s,c):
    result_str = ""
    for char in s:
        if char not in c:
            result_str += char
    is_palindrome = result_str == result_str[::-1]
    return (result_str, is_palindrome)
