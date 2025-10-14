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
    >>> vowels_count("yes")
    1
    >>> vowels_count("YES")
    1
    >>> vowels_count("hi")
    1
    >>> vowels_count("AAEIOUY")
    7
    """
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    end_vowels = ['y']

    for i in range(len(s)):
        if s[i].lower() in vowels:
            count += 1
        elif s[i].lower() in end_vowels and i == len(s)-1:
            count += 1

    return count
