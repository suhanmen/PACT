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

    Additional Test Cases:
    >>> vowels_count("")
    0
    >>> vowels_count("hmm")
    0
    >>> vowels_count("xyz")
    0
    >>> vowels_count("aeiouy")
    6
    >>> vowels_count("aeiouyAEIOUY")
    10
    """
    s = s.lower()
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    count = 0
    for i in range(len(s)):
        if s[i] in vowels:
            if i == len(s)-1 and s[i] == 'y':
                count += 1
            elif s[i] != 'y':
                count += 1
    return count
