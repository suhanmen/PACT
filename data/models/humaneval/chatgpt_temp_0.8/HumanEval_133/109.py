def sum_squares(lst):
    sum = 0
    for num in lst:
        rounded_num = int(num + 0.5) # round each number to the nearest integer
        sum += rounded_num ** 2 # square the rounded number and add to sum
    return sum
