def sort_numbers(numbers: str) -> str:
    number_dict = {
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

    # Convert the input string to a list of numbers
    num_list = [number_dict[num] for num in numbers.split()]

    # Sort the list of numbers and convert back to string
    sorted_list = sorted(num_list)
    sorted_str_list = [list(number_dict.keys())[list(number_dict.values()).index(num)] for num in sorted_list]
    return ' '.join(sorted_str_list)
