from typing import List


def below_zero(operations: List[int]) -> bool:
    balance = 0  # initialize balance to zero
    for operation in operations:
        balance += operation  # update balance with each operation
        if balance < 0:  # check if balance falls below zero
            return True
    return False  # if balance never falls below zero, return False

