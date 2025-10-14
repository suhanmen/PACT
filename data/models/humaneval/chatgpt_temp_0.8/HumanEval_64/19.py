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
    # Initialize vowel count to zero
    count = 0

    # Iterate through each character in the string
    for char in s:
        # If the character is a vowel, increment the count
        if char in ['a', 'e', 'i', 'o', 'u', 'y']:
            # If 'y' is in the middle of the word, do not count it as vowel
            if char == 'y' and s.index(char) != len(s) - 1:
                continue
            count += 1

    # Return the vowel count
    return count
