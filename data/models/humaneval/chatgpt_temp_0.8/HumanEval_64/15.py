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
    >>> vowels_count("The quick brown fox jumps over the lazy dog")
    11
    >>> vowels_count("Python programming is fun")
    6
    >>> vowels_count("Why are you running?")
    4
    """
    vowel_count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    s = s.lower()
    for i in range(len(s)):
        if s[i] in vowels:
            vowel_count += 1
        if i == len(s) - 1 and s[i] == 'y':
            vowel_count += 1
    return vowel_count
