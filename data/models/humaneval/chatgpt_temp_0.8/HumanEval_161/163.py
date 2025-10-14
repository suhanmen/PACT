def solve(s):
    new_s = ''
    has_letter = False
    for char in s:
        if char.isalpha():
            has_letter = True
            new_s += char.swapcase()
        else:
            new_s += char
    if not has_letter:
        new_s = new_s[::-1]
    return new_s
