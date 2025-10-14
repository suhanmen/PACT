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
    >>> vowels_count("hello")
    2
    >>> vowels_count("Python")
    2
    >>> vowels_count("Happy")
    1
    """
    count = 0
    for c in s:
        if c in "aeiouyAEIOUY":
            count += 1
    if s[-1] in "yY" and count > 0 and s[-2] not in "aeiouAEIOU":
        count -= 1
    return count
