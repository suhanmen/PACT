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
    >>> vowels_count("bcdfg")
    0
    >>> vowels_count("python")
    1
    """
    count = 0
    if s[-1] in "yY":
        vowels = "aeiouyY"
    else:
        vowels = "aeiou"
    for ch in s:
        if ch in vowels:
            count += 1
    return count
