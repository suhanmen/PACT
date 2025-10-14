def solve(s):
    result = ""
    has_letters = False
    for ch in s:
        if ch.isalpha():
            result += ch.swapcase()
            has_letters = True
        else:
            result += ch
    if not has_letters:
        result = result[::-1]
    return result
