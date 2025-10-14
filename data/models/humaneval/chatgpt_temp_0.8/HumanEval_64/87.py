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
    """
    vowel_count = 0
    vowels = "aeiouy"
    for i in range(len(s)):
        if s[i].lower() in vowels:
            if s[i].lower() == 'y' and i == len(s)-1:
                vowel_count += 1
            elif s[i].lower() != 'y':
                vowel_count += 1
    return vowel_count
