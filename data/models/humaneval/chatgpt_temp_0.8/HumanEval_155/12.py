def even_odd_count(num):
    even_count = 0
    odd_count = 0

    # convert the integer to a string to iterate through each digit
    str_num = str(num)

    # iterate through each digit and count even and odd digits
    for digit in str_num:
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return (even_count, odd_count)
