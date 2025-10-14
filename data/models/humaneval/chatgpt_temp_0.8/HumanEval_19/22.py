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
        'nine': 9,
    }
    nums = [num_dict[num] for num in numbers.split()]
    nums.sort()
    return ' '.join([key for key, value in num_dict.items() if value in nums])
