def sort_numbers(numbers: str) -> str:
    mapping = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }
    num_list = [mapping[num] for num in numbers.split()]
    num_list.sort()
    return ' '.join([key for key, value in mapping.items() if value in num_list])
