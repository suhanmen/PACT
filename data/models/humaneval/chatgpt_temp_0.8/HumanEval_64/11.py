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
    >>> vowels_count("Hello")
    2
    >>> vowels_count("Python")
    2
    >>> vowels_count("Fly")
    1
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    s = s.lower()
    count = 0
    if s[-1] == 'y':
        vowels.append('y')
    for c in s:
        if c in vowels:
            count += 1
    return count
