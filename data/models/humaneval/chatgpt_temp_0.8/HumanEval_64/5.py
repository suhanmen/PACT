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
    >>> vowels_count("hello")
    2
    >>> vowels_count("rhythm")
    0
    >>> vowels_count("way")
    1
    """
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in range(len(s)):
        if s[i].lower() in vowel_list:
            count += 1
        if i == len(s) - 1 and s[i].lower() == 'y' and s[i-1] not in vowel_list:
            count += 1
    return count
