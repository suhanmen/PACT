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
    s = s.lower() # convert the string to lowercase
    
    # define the set of vowels
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    # count the number of vowels in the string
    count = sum(1 for char in s if char in vowels)
    
    # check if the last character of the string is 'y' and increase count by 1 if True
    if s[-1] == 'y' and count > 0:
        count += 1
        
    return count
