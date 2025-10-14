def solve(s):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_str = ''
    for char in s:
        if char in letters:
            if char.islower():
                new_str += char.upper()
            else:
                new_str += char.lower()
        else:
            new_str += char
    if new_str.isalpha():
        return new_str[::-1]
    else:
        return new_str
