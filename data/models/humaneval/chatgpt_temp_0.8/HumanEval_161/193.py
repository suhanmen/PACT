def solve(s):
    new_s = ''
    has_letters = False
    for char in s:
        if char.isalpha():
            new_s += char.swapcase()
            has_letters = True
        else:
            new_s += char
    if not has_letters:
        new_s = s[::-1]
    return new_s
