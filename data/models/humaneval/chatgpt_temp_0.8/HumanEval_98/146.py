def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """

    # Define a set of uppercase vowels
    vowels = set(['A', 'E', 'I', 'O', 'U'])

    # Initialize a count variable
    count = 0

    # Loop through the even indices of the string
    for i in range(0, len(s), 2):
        # Check if the character at the index is an uppercase vowel
        if s[i] in vowels and s[i].isupper():
            # If it is, increment the count
            count += 1

    # Return the count
    return count
