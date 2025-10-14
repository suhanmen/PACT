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

    # Split the input string into a list of words
    words = numbers.split()

    # Convert the list of words into a list of numbers using the number_dict
    numbers_list = [number_dict[word] for word in words]

    # Sort the list of numbers in ascending order
    sorted_numbers = sorted(numbers_list)

    # Convert the list of numbers back into a string of words using the number_dict
    sorted_words = [key for value, key in number_dict.items() if value in sorted_numbers]
    sorted_string = " ".join(sorted_words)

    return sorted_string
