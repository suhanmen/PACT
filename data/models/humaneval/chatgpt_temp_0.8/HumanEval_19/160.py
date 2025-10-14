# Define a dictionary to map number words to their corresponding numeric values
num_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

def sort_numbers(numbers: str) -> str:
    # Split the input string into a list of number words
    num_words = numbers.split()
    # Map the number words to their numeric values and sort the list
    sorted_nums = sorted([num_dict[word] for word in num_words])
    # Map the sorted numeric values back to their corresponding number words
    sorted_words = [key for value, key in sorted(zip(sorted_nums, num_dict.keys()))]
    # Join the sorted number words into a string and return it
    return ' '.join(sorted_words)
