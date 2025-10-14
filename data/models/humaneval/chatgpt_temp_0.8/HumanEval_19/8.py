def sort_numbers(numbers: str) -> str:
    num_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
                'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    # split the string into a list of numberals
    num_list = numbers.split()
    # convert numberals to their corresponding integer values and sort them
    sorted_nums = sorted([num_dict[num] for num in num_list])
    # convert integer values back to numberals and join them into a string
    sorted_num_str = ' '.join([list(num_dict.keys())[list(num_dict.values()).index(num)] for num in sorted_nums])
    return sorted_num_str
