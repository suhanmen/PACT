def sort_numbers(numbers: str) -> str:
    numberals = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    mapping = {n: i for i, n in enumerate(numberals)}
    nums = [mapping[n] for n in numbers.split()]
    nums.sort()
    sorted_numbers = ' '.join(numberals[n] for n in nums)
    return sorted_numbers
