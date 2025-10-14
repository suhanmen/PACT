from typing import List


def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account falls below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    """
    
    # initialize balance to 0
    balance = 0
    
    # iterate through operations and update balance
    for operation in operations:
        balance += operation
        
        # if balance falls below zero, return True
        if balance < 0:
            return True
    
    # if balance never falls below zero, return False
    return False
