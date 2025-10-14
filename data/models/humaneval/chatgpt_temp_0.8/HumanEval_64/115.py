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
    >>> vowels_count("python")
    1
    >>> vowels_count("HELLO")
    2
    >>> vowels_count("")
    0
    """

    # Initialize a set of vowels
    vowels = set(['a', 'e', 'i', 'o', 'u', 'y'])

    # Convert the given string to lowercase to handle cases when the string has capital letters
    s = s.lower()

    # Check if the last character of the string is 'y' and add it to the set of vowels if it is
    if s.endswith('y'):
        vowels.add('y')

    # Count the number of vowels in the given string
    count = 0
    for char in s:
        if char in vowels:
            count += 1

    return count
