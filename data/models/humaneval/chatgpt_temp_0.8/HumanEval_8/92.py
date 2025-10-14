from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    sum_numbers = 0
    product_numbers = 1
    for number in numbers:
        sum_numbers += number
        product_numbers *= number
    return sum_numbers, product_numbers

