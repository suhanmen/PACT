def sort_numbers(numbers: str) -> str:
    number_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    number_dict = {word: i for i, word in enumerate(number_words)}
    numbers_list = numbers.split()
    numbers_list.sort(key=lambda x: number_dict[x])
    return ' '.join(numbers_list)
