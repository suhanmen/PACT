def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """

    # Define uppercase vowels
    vowels = "AEIOU"

    # Initialize count to 0
    count = 0

    # Iterate through even indices of string s
    for i in range(0, len(s), 2):
        if s[i] in vowels and s[i].isupper():
            count += 1

    return count
