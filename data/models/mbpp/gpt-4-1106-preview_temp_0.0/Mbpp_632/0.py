"""
Write a python function to move all zeroes to the end of the given list.
assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]
"""



def move_zero(lst):
    non_zeroes = [x for x in lst if x != 0]
    zeroes = [0] * (len(lst) - len(non_zeroes))
    return non_zeroes + zeroes

assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]
