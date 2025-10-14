def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.

    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """

    # Define the vowels to check for
    vowels = ['A', 'E', 'I', 'O', 'U']

    # Keep a count of the uppercase vowels found
    count = 0

    # Loop through the even indices of the string
    for i in range(0, len(s), 2):
        # Check if the character is an uppercase vowel
        if s[i] in vowels and s[i].isupper():
            count += 1

    return count
