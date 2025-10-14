def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Create a dictionary to map number words to their corresponding digits
    num_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    
    # Split the input string into a list of number words
    num_words = numbers.split()
    
    # Convert the number words to digits using the dictionary
    num_digits = [num_dict[word] for word in num_words]
    
    # Sort the digits in ascending order
    sorted_digits = sorted(num_digits)
    
    # Convert the sorted digits back to number words using the dictionary
    sorted_words = [key for key, value in num_dict.items() if value in sorted_digits]
    
    # J
