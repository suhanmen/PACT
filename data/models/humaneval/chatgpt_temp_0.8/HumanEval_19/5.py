def sort_numbers(numbers: str) -> str:
    number_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    nums = [number_dict[num] for num in numbers.split()]
    sorted_nums = sorted(nums)
    sorted_strings = [list(number_dict.keys())[list(number_dict.values()).index(num)] for num in sorted_nums]
    return ' '.join(sorted_strings)
