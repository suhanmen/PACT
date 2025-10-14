def solve(s):
    if not any(c.isalpha() for c in s):
        return s[::-1]
    else:
        return ''.join(c.swapcase() if c.isalpha() else c for c in s)
