def solve(s):
    result = ""
    count = 0
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].islower():
                result += s[i].upper()
            else:
                result += s[i].lower()
        else:
            result += s[i]
            count += 1
    if count == len(s):
        result = result[::-1]
    return result
