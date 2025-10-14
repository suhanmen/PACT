python
def choose_num(x, y):
    biggest_even_num = -1
    for num in range(x, y+1):
        if num % 2 == 0 and num > biggest_even_num:
            biggest_even_num = num
    return biggest_even_num
