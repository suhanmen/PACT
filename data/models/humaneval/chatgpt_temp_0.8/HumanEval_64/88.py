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
    >>> vowels_count("yummy")
    1
    >>> vowels_count("python")
    1
    """
    s = s.lower()  # convert the string into lowercase
    vowels = ['a', 'e', 'i', 'o', 'u']  # list of vowels
    count = 0  # initialize the count of vowels to be 0
    if s[-1] == 'y':  # if last character is 'y'
        for i in range(len(s) - 1):  # iterate over the string except the last character
            if s[i] in vowels:  # if the character is a vowel
                count += 1  # increment the count of vowels
        count += 1  # add 1 to the count for 'y' at the end
    else:  # if last character is not 'y'
        for i in range(len(s)):  # iterate over the string
            if s[i] in vowels:  # if the character is a vowel
                count += 1  # increment the count of vowels
    return count  # return the count of vowels in the string.
