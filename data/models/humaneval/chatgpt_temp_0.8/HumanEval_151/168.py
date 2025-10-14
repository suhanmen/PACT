python
def double_the_difference(lst):
    odd_nums = [n for n in lst if isinstance(n, int) and n >= 0 and n % 2 != 0]
    return sum([n**2 for n in odd_nums]) * 2
