# CANNOT PARSE
FIXED:

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
    # Initializing a variable to keep track of vowel count
    count = 0
    # Converting the given word to lowercase for ease of matching
    s = s.lower()
    # Checking each character in the word
    for i in range(len(s)):
        # If the character is a vowel, increase the count
        if s[i] in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    # Checking if the last character is 'y' and the second last character is not a vowel
    if s[-1] == 'y' and s[-2] not in ['a', 'e', 'i', 'o', 'u']:
        count += 1
    return count
