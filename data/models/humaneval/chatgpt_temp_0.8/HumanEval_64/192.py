# CANNOT PARSE
FIX = """
Add more test cases.
"""

def vowels_count(s):
    """
    Write a function vowels_count which takes a string representing a word as input
    and returns the number of vowels in the string. Vowels in this case are 'a', 'e',
    'i', 'o', 'u'. Here, 'y' is also a vowel, but only when it is at the end of the
    given word.

    Examples:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3

    Additional Test Cases:
    >>> vowels_count("hello world")
    3
    >>> vowels_count("xylophone")
    3
    >>> vowels_count("qwerty")
    1
    """

    vowel_count = 0
    s = s.lower()

    if s[-1] == 'y':
        vowel_count += 1

    for letter in s:
        if letter in ['a', 'e', 'i', 'o', 'u', 'y']:
            vowel_count += 1

    return vowel_count
