def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Create a dictionary to map number words to their numerical value
    number_map = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    
    # Split the input string into a list of number words
    number_words = numbers.split()
    
    # Convert the number words to numerical values using the dictionary
    numbers = [number_map[word] for word in number_words]
    
    # Sort the numerical values
    numbers.sort()
    
    # Convert the sorted numerical values back to number words
    sorted_number_words = [word for word
