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
    >>> vowels_count("hello")
    2
    >>> vowels_count("aeiouy")
    6
    >>> vowels_count("why")
    0
    >>> vowels_count("syzygy")
    0
    >>> vowels_count("rhythm")
    0
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    s = s.lower()
    count = 0
    if s[-1] == 'y':
        vowels.append('y')
    for letter in s:
        if letter in vowels:
            count += 1
    return count
