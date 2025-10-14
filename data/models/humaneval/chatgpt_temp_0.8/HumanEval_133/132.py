def sum_squares(lst):
    """
    You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int (ceiling) first.
    """
    return sum([int(num)**2 for num in lst if num > 0]) # Use list comprehension to square each positive integer in the list, round it up to the next integer, and sum the resulting values.
