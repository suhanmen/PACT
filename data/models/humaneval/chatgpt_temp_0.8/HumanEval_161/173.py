def solve(s):
    letters = [char for char in s if char.isalpha()]
    if not letters:
        return s[::-1]
    else:
        new_str = ""
        for char in s:
            if char.isalpha():
                if char.isupper():
                    new_str += char.lower()
                else:
                    new_str += char.upper()
            else:
                new_str += char
        return new_str
