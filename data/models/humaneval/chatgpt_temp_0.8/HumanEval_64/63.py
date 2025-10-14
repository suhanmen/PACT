# CANNOT PARSE
FIX = """
Add more test cases.
"""

def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    >>> vowels_count("Python")
    1
    >>> vowels_count("Hello World")
    3
    >>> vowels_count("sky")
    0
    """
    count = 0
    s = s.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(s)):
        if s[i] in vowels:
            count += 1
        if i == len(s)-1 and s[i] == 'y' and s[i-1] not in vowels:
            count += 1
    return count
