python
def digitSum(s):
    """
    Task: Write a function that takes a string as input and returns the sum of
    the ASCII codes of the upper case characters only.

    Args:
    - s: a string

    Returns:
    - The sum of the ASCII codes of the upper case characters in s

    Examples:
    digitSum("") => 0
    digitSum("abAB") => 131
    digitSum("abcCd") => 67
    digitSum("helloE") => 69
    digitSum("woArBld") => 131
    digitSum("aAaaaXa") => 153
    """
    # Initialize sum to 0
    sum = 0
    
    # Iterate through each character in s
    for c in s:
        # Check if the character is uppercase
        if c.isupper():
            # Add the ASCII code of the character to the sum
            sum += ord(c)
            
    return sum
