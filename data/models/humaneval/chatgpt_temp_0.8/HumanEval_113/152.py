def odd_count(lst):
    """Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "the number of odd elements in the
    string i of the input." where all the i's should be replaced by the number
    of odd digits in the i'th string of the input.

    >>> odd_count(['1234567'])
    ["the number of odd elements in the string 1 of the input."]
    >>> odd_count(['3',"11111111"])
    ["the number of odd elements in the string 1 of the input.",
     "the number of odd elements in the string 8 of the input."]
    """
    # Create an empty list to store our results
    result = []
    
    # Loop through each string in the input list
    for string in lst:
        # Initialize a counter for the number of odd digits
        odd_count = 0
        # Loop through each digit in the string
        for digit in string:
            # If the digit is odd, increment the counter
            if int(digit) % 2 == 1:
                odd_count += 1
      
