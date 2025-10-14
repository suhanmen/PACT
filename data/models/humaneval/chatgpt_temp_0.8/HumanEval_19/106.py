def sort_numbers(numbers: str) -> str:
    words_to_numbers = {
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
    numbers_list = [words_to_numbers[word] for word in numbers.split()]
    sorted_numbers = sorted(numbers_list)
    sorted_words = [key for key, value in words_to_numbers.items() if value in sorted_numbers]
    return ' '.join(sorted_words)
