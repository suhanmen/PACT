def sort_numbers(numbers: str) -> str:
    number_dict = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    # Convert the input to a list of integers using the number_dict
    num_list = [number_dict[num] for num in numbers.split()]
    # Sort the list
    sorted_list = sorted(num_list)
    # Convert the sorted list back to a space-delimited string of numberals
    sorted_string = " ".join([key for key, value in number_dict.items() if value in sorted_list])
    return sorted_string
