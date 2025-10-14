# Creating a dictionary to map the number words to their equivalent digits
number_dict = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def sort_numbers(numbers: str) -> str:
    # Splitting the input string into a list of individual numbers
    number_list = numbers.split()

    # Converting each number from word to digit using the number_dict
    number_list = [number_dict[number] for number in number_list]

    # Sorting the list of digits in ascending order
    number_list.sort()

    # Converting the sorted list of digits back to words
    word_list = [key for key, value in number_dict.items() if value in number_list]

    # Joining the list of words into a space-delimited string
    return ' '.join(word_list)
