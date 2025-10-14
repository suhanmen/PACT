python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.

    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """

    # Define a set of uppercase vowels
    vowels = {'A', 'E', 'I', 'O', 'U'}

    # Initialize count to 0
    count = 0

    # Loop through even indices of s
    for i in range(0, len(s), 2):
        # Check if s[i] is an uppercase vowel
        if s[i] in vowels and s[i].isupper():
            count += 1

    return count
