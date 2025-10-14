def sort_numbers(numbers: str) -> str:
    digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    num_list = numbers.split()
    num_list.sort(key=lambda x: digits.index(x))
    return ' '.join(num_list)
