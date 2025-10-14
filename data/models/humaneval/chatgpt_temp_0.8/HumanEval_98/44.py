def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # Define a list of uppercase vowels
    vowels = ['A', 'E', 'I', 'O', 'U']

    # Initialize a count variable to 0
    count = 0

    # Iterate over the even indices of the string
    for i in range(0, len(s), 2):
        # Check if the character at the current index is an uppercase vowel
        if s[i] in vowels:
            # Increment the count variable if it is
            count += 1

    # Return the count of uppercase vowels in even indices
    return count
