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
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    s = s.lower()  # Convert all characters to lowercase for easy comparison
    for i in range(len(s)):
        if s[i] in vowels:
            count += 1
        if i == len(s) - 1 and s[i] == 'y':  # Check if 'y' is at the end of the string
            count += 1
    return count
