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
    >>> vowels_count("aeiou")
    5
    >>> vowels_count("YUZ")
    0
    >>> vowels_count("happy")
    1
    """
    count = 0
    for i in s.lower():
        if i in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    if s[-1].lower() == 'y' and count == 0:
        count += 1
    return count
