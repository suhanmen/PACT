# CANNOT PARSE
FIX = """
Add more test cases.
"""

def vowels_count(s):
    count = 0
    s = s.lower()
    for i in range(len(s)):
        if s[i] in ['a', 'e', 'i', 'o', 'u']:
            count += 1
        elif i == len(s) - 1 and s[i] == 'y':
            count += 1
    return count
    



