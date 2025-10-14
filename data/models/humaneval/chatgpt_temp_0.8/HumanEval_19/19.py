def sort_numbers(numbers: str) -> str:
    num_dict = {
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

    # Convert the space-delimited string of numbers to a list of numberals
    num_list = numbers.split()

    # Sort the list of numberals based on their numeric value
    num_list.sort(key=lambda x: num_dict[x])

    # Convert the sorted list of numberals back to a space-delimited string
    sorted_numbers = " ".join(num_list)

    return sorted_numbers
