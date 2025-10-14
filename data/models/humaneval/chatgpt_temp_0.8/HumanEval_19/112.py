# Create a dictionary to lookup the numerical value of each string
number_lookup = {
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

def sort_numbers(numbers: str) -> str:
    # Convert the string of numbers to a list of strings
    numbers_list = numbers.split()

    # Convert the list of strings to a list of tuples with the numerical value as the first element
    numbers_tuples = [(number_lookup[number], number) for number in numbers_list]

    # Sort the list of tuples by the numerical value
    sorted_tuples = sorted(numbers_tuples)

    # Convert the list of tuples back to a list of strings
    sorted_numbers_list = [number for _, number in sorted_tuples]

    # Join the list of strings back into a single string
    sorted_numbers = ' '.join(sorted_numbers_list)

    return sorted_numbers
