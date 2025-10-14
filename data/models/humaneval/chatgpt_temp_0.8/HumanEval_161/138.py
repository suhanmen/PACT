def solve(s):
    letters = [i for i in s if i.isalpha()]
    if not letters:
        return s[::-1]
    else:
        result = ""
        for i in s:
            if i.isalpha():
                if i.islower():
                    result += i.upper()
                else:
                    result += i.lower()
            else:
                result += i
        return result
