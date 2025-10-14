from typing import List

def sort_numbers(numbers: str) -> str:
    numbers_list = numbers.split()
    num_dict = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    sorted_nums = sorted(numbers_list, key=lambda x: num_dict[x])
    return ' '.join(sorted_nums)
