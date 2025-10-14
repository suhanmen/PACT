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

    Additional test cases:
    >>> vowels_count("aeiouy")
    6
    >>> vowels_count("hello")
    2
    >>> vowels_count("puzzle")
    2
    """
    count = 0
    for char in s:
        if char.lower() in ('a', 'e', 'i', 'o', 'u'):
            count += 1
    # check for 'y' only at the end of word
    if s[-1].lower() == 'y' and count > 0 and s[-2].lower() not in ('a', 'e', 'i', 'o', 'u'):
        count += 1
    return count
