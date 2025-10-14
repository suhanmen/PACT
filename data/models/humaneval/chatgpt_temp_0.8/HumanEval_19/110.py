def sort_numbers(numbers: str) -> str:
    digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    number_list = numbers.split()
    number_indices = [digits.index(n) for n in number_list]
    sorted_indices = sorted(number_indices)
    sorted_numbers = [digits[i] for i in sorted_indices]
    return ' '.join(sorted_numbers)
