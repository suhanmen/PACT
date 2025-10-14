def solve(s):
    letters = [char for char in s if char.isalpha()]
    if not letters:
        return s[::-1]
    else:
        result = ""
        for char in s:
            if char.isalpha():
                if char.islower():
                    result += char.upper()
                else:
                    result += char.lower()
            else:
                result += char
        return result
