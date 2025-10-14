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
    # Convert input string to lowercase for easier comparison
    s = s.lower()
    # Check if the last character is 'y' and if it is a vowel
    if s[-1] == 'y':
        if s[-2] in ['a', 'e', 'i', 'o', 'u']:
            return len([char for char in s if char in ['a', 'e', 'i', 'o', 'u', 'y']])
        else:
            return len([char for char in s[:-1] if char in ['a', 'e', 'i', 'o', 'u']])            
    else:
        return len([char for char in s if char in ['a', 'e', 'i', 'o', 'u']])
